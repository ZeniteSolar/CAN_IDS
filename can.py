#!/bin/python

from unicodedata import normalize
import json
import re

class Can:
    def convert_string(string: str) -> str:
        string = string.upper()
        string = string.replace(' ', '_')
        string = normalize('NFKD', string).encode('ASCII', 'ignore').decode('ASCII')
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

        def subscribe_topic(self, topic):
            self.topics.append(dict(topic.get()))


if __name__ == '__main__':
    a = Can.topic("motor", 9)
    a.describe_byte("motor", 1)
    a.describe_bit("motor on", 1, 0)
    a.describe_byte("D raw", 2)
    a.describe_byte("I raw", 3)
    #a.print()

    m = Can.module("mic17", 10)
    m.subscribe_topic(a)
    m.print()


