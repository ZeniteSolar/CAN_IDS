#!/bin/python

from operator import mod
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
    def convert_string(self) -> str:
        if not isinstance(self, str):
            raise TypeError("`string` needs to be an integer type!")

        self = self.upper()
        self = self.replace(' ', '_')
        self = normalize('NFKD', self)
        self = self.encode('ASCII', 'ignore')
        self = self.decode('ASCII')
        self = re.sub('[^A-Z0-9_]+', '', self)

        return self

    def validate_byte(self) -> bool:
        if (self < 0) | (self > 8):
            print("Byte number MUST be between 0 and 7 to be described.")
            return False
        return True

    def validate_bit(self) -> bool:
        if (self < 0) | (self > 8):
            print("Bit number MUST be between 0 and 7 to be described.")
            return False
        return True

    class topic:
        def __init__(self, msg: str, id: int,frequency: int, description: str):
            self.name = Can.convert_string(msg)

            if not isinstance(id, int):
                raise TypeError("`id` must be an integer type!")
            self.id = id

            if not isinstance(description, str):
                raise TypeError("`description` must be a string type!")
            self.description = description

            self.bytes = [None] * 8

            self.frequency = frequency

            self.frame_length = 47

            self.describe_byte(
                "signature", 0, "Senders signature", "uint8_t", "")

        def get(self) -> dict:
            return {
                "name": str(self.name),
                "description": self.description,
                "id": self.id,
                "bytes": self.bytes,
                "frequency": self.frequency,
                "frame_length": self.frame_length
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
            
        def get_length(self):
            return len(list(filter(lambda x: x is not None, self.bytes)))

        def get_frame_length(self):
            return 44 + 8 * self.get_length()

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

            self.frame_length += 8

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

        def get_total_load(self, bitrate):
            return sum(topic.get_load(bitrate) for topic in self.topics)
            
        def __str__(self) -> str:
            return json.dumps(self.get(), indent=4)

        def add_topic(self, topic):
            for t in self.topics:
                if t['name'] == dict(topic.get()).get('name'):
                    raise ValueError("topic field `name` must be unique!")

            self.topics.append(topic.get())

    def __init__(self, version: str, bitrate: int):
        self.version = version
        self.modules = []
        self.bitrate = bitrate

    def get(self) -> dict:
        return {
            "version": self.version,
            "modules": self.modules,
            "bitrate": self.bitrate,
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
            self.version = data["version"]
            for module in data["modules"]:
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

    def export_csv(self, filename: str):
        import pandas as pd

        modules = []
        signature = []
        ids = []
        names = []
        frequency = []
        load = []
        frame_length = []
        description = []

        for module in self.modules:
            for topic in module["topics"]:
                modules.append(module["name"])
                signature.append(module["signature"])
                ids.append(topic["id"])
                names.append(topic["name"])
                frequency.append(round(topic["frequency"],3))
                load.append(round(self.get_topic_load(topic),3))
                frame_length.append(topic["frame_length"])
                description.append(topic["description"])

        df = pd.DataFrame({
            "modules":modules,
            "signature": signature,
            "name": names,
            "ids": ids,
            "frequency": frequency,
            "load": load,
            "frame_length": frame_length,
            "description": description,
            })

        df.to_csv(filename)
        

                


    def get_can_load_by_topic(self):
        load = {}
        for module in self.modules:
            for topic in module["topics"]:
                if topic["id"] not in load:
                    load[topic["id"]] = []
                load[topic["id"]].append(self.get_topic_load(topic))
        return load
    

    def get_can_load(self):
        load = 0
        for module in self.modules:
            for topic in module["topics"]:
                load += self.get_topic_load(topic)
        return load

    def get_topic_load(self, topic: dict):
        frame_length = topic["frame_length"]
        frame_period = (1/self.bitrate) * frame_length
        return frame_period * topic["frequency"] * 100     
        # load = period for 1 msg *  frequency * 100% 
        # Reference:
        # https://support.vector.com/kb?id=kb_article_view&sysparm_article=KB0012332&sys_kb_id=99354e281b2614148e9a535c2e4bcb6d&spa=1

    def plot_load(self):
        import matplotlib.pyplot as plt
        import numpy as np
        fig, axes = plt.subplots(nrows= 2, ncols=2,figsize=(9, 6))
        plt.figtext(.5, .9, "Can Load ", fontsize=15, ha='center')

        ### Ids x Load
        ids = {}
        for module in self.modules:
            for topic in module["topics"]:
                if topic["id"] not in ids:
                    ids[topic["id"]] = 0
                ids[topic["id"]] += self.get_topic_load(topic)

        id = sorted(ids.keys())
        load = [ids[i] for i in id]
        axes[0][0].bar(range(len(id)), load, align='center', color='royalblue')
        axes[0][0].set_xticks(range(len(id)))
        axes[0][0].set_xticklabels(list(id), fontsize = 9, rotation = 90)
        axes[0][0].set_title("Load x Id")
        axes[0][0].set_ylabel("Load [%]")
        axes[0][0].set_xlabel("Ids")
        axes[0][0].invert_xaxis()
        axes[0][0].grid()

        id.append("free")
        load.append(100 - sum(load))
        cmap = plt.cm.prism
        colors = cmap(np.linspace(0.2, 0.8, len(id)))
        axes[0][1].set_title("Load x Id")
        axes[0][1].pie(load, labels=id,
                       textprops={'size': 'smaller'}, radius=1.5,colors=colors, labeldistance=1.1, startangle=-45)

        #### Modules X Load
        load = []
        modules = {}
        for module in self.modules:
            for topic in module["topics"]:
                if module["name"] not in modules:
                    modules[module["name"]] = 0
                modules[module["name"]] += self.get_topic_load(topic)
        load = list(modules.values())
        modules = list(modules.keys())
        axes[1][0].set_title("Load x Module")
        axes[1][0].bar(range(len(modules)), load)
        axes[1][0].set_xticks(range(len(modules)))
        axes[1][0].set_xticklabels(modules, fontsize = 9, rotation=90)
        axes[1][0].set_ylabel("Load [%]")

        modules.append("free")
        load.append(100.0 - sum(load))
        axes[1][1].set_title("Load x Module")
        axes[1][1].pie(load, labels=modules,
                       textprops={'size': 'smaller'}, radius=1.5, labeldistance=1.1,startangle=-45)



        plt.show()

        


if __name__ == '__main__':
    t1 = Can.topic("motor", 9, 100, "Motor controller parameters")
    t1.describe_byte("motor", 1, "Switches and states", "bitfield", "")
    t1.describe_bit("motor on", 1, 0)
    t1.describe_byte("D raw", 2, "Motor Duty Cycle", "uint8_t", "%")
    t1.describe_byte("I raw", 3, "Motor Soft Start", "uint8_t", "%")
    t2 = Can.topic("motor2", 19, 10, "Motor controller parameters")
    t2.describe_byte("motor", 1, "Switches and states", "bitfield", "")
    t2.describe_bit("motor on", 1, 0)
    t2.describe_byte("D raw", 2, "Motor Duty Cycle", "uint8_t", "%")
    t2.describe_byte("I raw", 3, "Motor Soft Start", "uint8_t", "%")
    # print(t1)

    m1 = Can.module("mic17", 10, "Modulo de Interface de Controle")
    m1.add_topic(t1)
    m1.add_topic(t2)
    m2 = Can.module("mam21", 10, "Mamm")

    # print(m1)

    c1 = Can("0.0.0", 500e3)
    c1.add_module(m1)
    # print(c1)
    c1.export_json("sample.json")
    print(c1.get_can_load())
    print(c1.get_topic_load(t1.get()))
    c1.plot_load()
    c1.export_csv("a")
    # c2 = Can()
    # c2.import_json("sample.json")
    # print(c2)

    # c2.export_ids_h("sample.h")

    
