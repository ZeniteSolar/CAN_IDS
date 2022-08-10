#!/bin/python

from unicodedata import normalize
import json
import re
from mako.template import Template

# TODO: escrever funções para facilitar a edição e criação de variações:
#   - criar uma cópia do modulo, mensagem, byte ou bit
#   - atualizar um campo do modulo
#   - atualizar um campo de um topico do modulo
#   - atualizar um campo de um byte de um topico do modulo
#   - atualizar um campo de um bit de um byte de um topico do modulo


class Can:
    def convert_string(string: str) -> str:
        if not isinstance(string, str):
            raise TypeError("`string` needs to be an integer type!")

        string = string.upper()
        string = string.replace(' ', '_')
        string = normalize('NFKD', string)
        string = string.encode('ASCII', 'ignore')
        string = string.decode('ASCII')
        string = re.sub('[^A-Z0-9_]+', '', string)

        return string

    def validate_byte(byte: int) -> bool:
        if (byte < 0) | (byte > 8):
            print("Byte number MUST be between 0 and 7 to be described.")
            return False
        return True

    def validate_bit(bit: int) -> bool:
        if (bit < 0) | (bit > 8):
            print("Bit number MUST be between 0 and 7 to be described.")
            return False
        return True

    class topic:
        def __init__(self, msg: str, id: int, description: str):
            self.name = Can.convert_string(msg)

            if not isinstance(id, int):
                raise TypeError("`id` must be an integer type!")
            self.id = id

            if not isinstance(description, str):
                raise TypeError("`description` must be a string type!")
            self.description = description

            self.bytes = [None] * 8

            self.describe_byte(
                "signature", 0, "Senders signature", "uint8_t", "")

        def get(self) -> dict:
            return {
                "name": str(self.name),
                "description": self.description,
                "id": self.id,
                "bytes": self.bytes
            }

        def __str__(self) -> str:
            return json.dumps(self.get(), indent=4)

        def validate_byte(self, byte: int):
            if not isinstance(byte, int):
                raise TypeError("`byte` needs to be an integer type!")

            if (byte < 0) or (byte > 7):
                raise ValueError(
                    "`byte` number MUST be between 0 and 7 to be described.")

        def validate_bit(self, bit: int) -> bool:
            if not isinstance(bit, int):
                raise TypeError("`bit` needs to be an integer type!")

            if (bit < 0) or (bit > 7):
                raise ValueError(
                    "`bit` number MUST be between 0 and 7 to be described.")

        def validate_byte_name(self, name: str):
            if not isinstance(name, str):
                raise TypeError("byte field `name` must be a string type!")

            for byte in filter(None, self.bytes):
                if byte.get('name') == Can.convert_string(name):
                    raise ValueError("byte field `name` must be unique!")

        def validate_bit_name(self, byte: int, name: str):
            if not isinstance(name, str):
                raise TypeError("bit field `name` must be a string type!")

            if self.bytes[byte] is not None:
                for bit in filter(None, self.bytes[byte].get('bits')):
                    if bit == Can.convert_string(name):
                        raise ValueError("bit field `name` must be unique!")

        def describe_byte(self,
                          name: str,
                          byte: int,
                          description: str,
                          btype: str,
                          units: str = None):
            self.validate_byte_name(name)
            self.validate_byte(byte)

            if not isinstance(description, str):
                raise TypeError("`description` must a string type!")

            if not isinstance(btype, str):
                raise TypeError("`type` must a string type!")

            if units is not None and not isinstance(units, str):
                raise TypeError("`units` must a string type!")

            name = Can.convert_string(name)

            self.bytes[byte] = {
                "name": name,
                "description": description,
                "type": btype,
                "units": units,
            }

            if self.bytes[byte]["type"] == "bitfield":
                self.bytes[byte]["bits"] = [None]*8

        def describe_bit(self, name: str, byte: int, bit: int):
            self.validate_byte(byte)
            self.validate_bit(bit)

            if self.bytes[byte]["type"] != "bitfield":
                raise ValueError("`type` must a `bitfield`")

            self.validate_bit_name(byte, name)

            name = Can.convert_string(name)

            self.bytes[byte]["bits"][bit] = name

    class module:
        def __init__(self, name: str, signature: int, description: str):

            self.validate_name(name)

            self.name = Can.convert_string(name)

            if not isinstance(signature, int):
                raise TypeError("`signature` must be an int type!")
            self.signature = signature

            if not isinstance(description, str):
                raise TypeError("`description` must be a string type!")
            self.description = description

            self.topics = []

        def validate_name(self, name: str):
            if not isinstance(name, str):
                raise TypeError("byte field `name` must be a string type!")

        def get(self) -> dict:
            return {
                "name": self.name,
                "description": self.description,
                "signature": self.signature,
                "topics": self.topics
            }

        def __str__(self) -> str:
            return json.dumps(self.get(), indent=4)

        def add_topic(self, topic):
            for t in self.topics:
                if t['name'] == dict(topic.get()).get('name'):
                    raise ValueError("topic field `name` must be unique!")

            self.topics.append(topic.get())

    def __init__(self, version: str):
        self.version = version
        self.modules = []

    def get(self) -> dict:
        return {
            "version": self.version,
            "modules": self.modules,
        }

    def __str__(self) -> str:
        return json.dumps(self.get(), indent=4)

    def add_module(self, module):
        for m in self.modules:
            if m['name'] == dict(module.get()).get('name'):
                raise ValueError("module field `name` must be unique!")

        self.modules.append(module.get())

    def import_json(self, filename: str):
        with open(filename, 'r') as file:
            data = dict(json.load(file))
            for moduleslist in data.values():
                for module in moduleslist:
                    self.add_module(Can.module(
                        name=module.get('name'),
                        signature=module.get('signature'),
                        description=module.get('description')
                    ))
        return self

    def export_json(self, filename: str = "can_ids.json"):
        with open(filename, 'w') as file:
            json.dump(dict(self.get()), file, indent=4)

    def export_h(self, filename: str):
        template = Template(filename=f"{filename}.mako")
        rendered = template.render(db=dict(self.get()))
        with open(filename, 'w') as file:
            file.write(rendered)

    def export_c_library(self, filename: str = "can_ids.h"):
        self.export_h("can_ids.h")
        self.export_h("can_parser_types.h")


if __name__ == '__main__':
    t1 = Can.topic("motor", 9, "Motor controller parameters")
    t1.describe_byte("motor", 1, "Switches and states", "bitfield", "")
    t1.describe_bit("motor on", 1, 0)
    t1.describe_byte("D raw", 2, "Motor Duty Cycle", "uint8_t", "%")
    t1.describe_byte("I raw", 3, "Motor Soft Start", "uint8_t", "%")
    # print(t1)

    m1 = Can.module("mic17", 10, "Modulo de Interface de Controle")
    m1.add_topic(t1)
    # print(m1)

    c1 = Can()
    c1.add_module(m1)
    # print(c1)
    c1.export_json("sample.json")

    c2 = Can()
    c2.import_json("sample.json")
    print(c2)

    c2.export_ids_h("sample.h")
