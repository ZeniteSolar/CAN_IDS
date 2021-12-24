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

    def validate_byte(byte) -> bool:
        if (byte < 0) | (byte > 8):
            print("Byte number MUST be between 0 and 7 to be described.")
            return False
        return True

    def validate_bit(bit) -> bool:
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

            self.describe_byte("signature", 0, "Senders signature", "u8", "")

        def get(self) -> dict:
            return {
                "name": str(self.name),
                "description": self.description,
                "id": self.id,
                "bytes": self.bytes
            }

        def print(self):
            print(json.dumps(self.get(), indent=4))

        def validate_byte(self, byte: int):
            if not isinstance(byte, int):
                raise TypeError("`byte` needs to be an integer type!")

            if (byte < 0) or (byte > 7):
                raise ValueError("`byte` number MUST be between 0 and 7 to be described.")

        def validate_bit(self, bit: int) -> bool:
            if not isinstance(bit, int):
                raise TypeError("`bit` needs to be an integer type!")

            if (bit < 0) or (bit > 7):
                raise ValueError("`bit` number MUST be between 0 and 7 to be described.")

        def validate_byte_name(self, name: str):
            if not isinstance(name, str):
                raise TypeError("byte field `name` must be a string type!")

        def validate_bit_name(self, byte: int, name: str):
            if not isinstance(name, str):
                raise TypeError("bit field `name` must be a string type!")

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
                "units": units
            }

        def describe_bit(self, name: str, byte: int, bit: int):
            self.validate_byte(byte)
            self.validate_bit(bit)

            if "bits" not in self.bytes[byte].keys():
                self.bytes[byte].update({ "bits": [None]*8 })
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

        def print(self):
            print(json.dumps(self.get(), indent=4))

        def add_topic(self, topic):
            self.topics.append(dict(topic.get()))

    def __init__(self):
        self.modules = []

    def get(self) -> str:
        return {
            "modules": self.modules
        }

    def print(self):
        print(json.dumps(self.get(), indent=4))

    def add_module(self, module):
        self.modules.append(dict(module.get()))

    def import_json(self, filename: str):
        with open(filename, 'r') as file:
            data = dict(json.load(file))
            for moduleslist in data.values():
                for module in moduleslist:
                    self.modules.append(dict(module))
        return self

    def export_json(self, filename: str):
        with open(filename, 'w') as file:
            json.dump(dict(self.get()), file, indent=4)

    def export_h(self, filename: str):
        template = Template(filename="can_ids.h.mako")
        rendered = template.render(db=dict(self.get()))
        with open(filename, 'w') as file:
            file.write(rendered)


if __name__ == '__main__':
    t1 = Can.topic("motor", 9, "Motor controller parameters")
    t1.describe_byte("motor", 1, "Switches and states", "bitfield", "")
    t1.describe_bit("motor on", 1, 0)
    t1.describe_byte("D raw", 2, "Motor Duty Cycle", "u8", "%")
    t1.describe_byte("I raw", 3, "Motor Soft Start", "u8", "%")
    # t1.print()

    m1 = Can.module("mic17", 10, "Modulo de Interface de Controle")
    m1.add_topic(t1)
    # m1.print()

    c1 = Can()
    c1.add_module(m1)
    # c1.print()
    c1.export_json("sample.json")

    c2 = Can()
    c2.import_json("sample.json")
    c2.print()

    c2.export_h("sample.h")

