#!/bin/python

from unicodedata import normalize
import json
import re

class Can:
    def convert_string(string: str) -> str:
        string = string.upper()
        string = string.replace(' ', '_')
        string = normalize('NFKD', string)
        string = string.encode('ASCII', 'ignore')
        string = string.decode('ASCII')
        string = re.sub('[^A-Z0-9_]+', '', string)
        return string

    class topic:
        name_prefix = "CAN_FILTER_MSG_"

        def __init__(self, msg: str, id: int):
            self.name = Can.convert_string(msg)
            self.id = id
            self.bytes = [None] * 8
            self.describe_byte("signature", 0)

        def get(self) -> str:
            return {
                "name": str(self.name_prefix + self.name),
                "id": self.id,
                "bytes": self.bytes
            }

        def print(self):
            print(json.dumps(self.get(), indent=4))

        def describe_byte(self, name: str, byte: int):
            name = Can.convert_string(name)
            if (byte < 0) | (byte > 8):
                print("Byte number MUST be between 0 and 7 to be described.")
                return

            self.bytes[byte] = {"name": name}

        def describe_bit(self, name: str, byte: int, bit: int):
            name = Can.convert_string(name)
            if (bit < 0) | (bit > 8):
                print("Byte number MUST be between 0 and 7 to be described.")
                return
            if (bit < 0) | (bit > 8):
                print("bit number MUST be between 0 and 7 to be described.")
                return

            if "bits" not in self.bytes[byte].keys():
                self.bytes[byte].update({ "bits": [None]*8 })

            self.bytes[byte]["bits"][bit] = name

    class module:
        name_prefix = ""

        def __init__(self, name: str, signature: int):
            self.name = Can.convert_string(name)
            self.signature = signature
            self.topics = []

        def get(self) -> str:
            return {
                "name": str(self.name_prefix + self.name),
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


if __name__ == '__main__':
    t1 = Can.topic("motor", 9)
    t1.describe_byte("motor", 1)
    t1.describe_bit("motor on", 1, 0)
    t1.describe_byte("D raw", 2)
    t1.describe_byte("I raw", 3)
    # t1.print()

    m1 = Can.module("mic17", 10)
    m1.add_topic(t1)
    # m1.print()

    c1 = Can()
    c1.add_module(m1)
    # c1.print()
    c1.export_json("test.json")

    c2 = Can()
    c2.import_json("test.json")
    c2.print()

