#!/bin/python

import unittest
from can import Can

class test_can_topic(unittest.TestCase):
    def setUp(self):
        self.can = Can

    def test_topic(self):
        t = self.can.topic("motor", 9, "topic description text here")
        expected = {
            "name": "MOTOR",
            "description": "topic description text here",
            "id": 9,
            "bytes": [
                {
                    "name": "SIGNATURE",
                    "description": "Senders signature",
                    "type": "u8",
                    "units": ""
                },
                *[None]*7
            ]
        }

        self.assertEqual(
            dict(t.get()),
            expected
        )

    def test_describe_byte(self):
        t = self.can.topic("motor", 9, "topic description text here")
        t.describe_byte("motor", 1, "byte description text here", "bitfield", "")

        expected = {
            "name": "MOTOR",
            "description": "topic description text here",
            "id": 9,
            "bytes": [
                {
                    "name": "SIGNATURE",
                    "description": "Senders signature",
                    "type": "u8",
                    "units": "",
                },
                {
                    "name": "MOTOR",
                    "description": "byte description text here",
                    "type": "bitfield",
                    "units": "",
                },
                *[None]*6
            ]
        }

        self.assertEqual(
            dict(t.get()),
            expected
        )

    def test_describe_bit(self):
        t = self.can.topic("motor", 9, "topic description text here")
        t.describe_byte("motor", 1, "byte description text here", "bitfield", "")
        t.describe_bit("motor on", 1, 0)

        expected = {
            "name": "MOTOR",
            "description": "topic description text here",
            "id": 9,
            "bytes": [
                {
                    "name": "SIGNATURE",
                    "description": "Senders signature",
                    "type": "u8",
                    "units": "",
                },
                {
                    "name": "MOTOR",
                    "description": "byte description text here",
                    "type": "bitfield",
                    "units": "",
                    "bits": ["MOTOR_ON", *[None]*7],
                },
                *[None]*6
            ]
        }

        self.assertEqual(
            dict(t.get()),
            expected
        )


class test_can_module(unittest.TestCase):
    def setUp(self):
        self.can = Can

    def test_module(self):
        m = self.can.module("mic17", 10, "module description text here")

        expected = {
            "name": "MIC17",
            "description": "module description text here",
            "signature": 10,
            "topics": [],
        }

        self.assertEqual(
            dict(m.get()),
            expected
        )

    def test_add_topic(self):
        m = self.can.module("mic17", 10, "module description text here")
        t = self.can.topic("motor", 9, "topic description text here")

        m.add_topic(t)

        expected = {
            "name": "MIC17",
            "description": "module description text here",
            "signature": 10,
            "topics": [
                {
                    "name": "MOTOR",
                    "description": "topic description text here",
                    "id": 9,
                    "bytes": [
                        {
                            "name": "SIGNATURE",
                            "description": "Senders signature",
                            "type": "u8",
                            "units": ""
                        },
                        *[None]*7,
                    ],
                },
            ],
        }

        self.assertEqual(
            dict(m.get()),
            expected
        )


class test_can(unittest.TestCase):
    def setUp(self):
        self.can = Can

    def test_add_module(self):
        m = self.can.module("mic17", 10, "module description text here")
        c = Can()
        c.add_module(m)

        expected = {
            "modules": [
                {
                    "name": "MIC17",
                    "description": "module description text here",
                    "signature": 10,
                    "topics": [],
                },
            ],
        }

        self.assertEqual(
            dict(c.get()),
            expected
        )

    def test_export_and_import_json(self):
        m = self.can.module("mic17", 10, "module description text here")
        c1 = Can()
        c1.add_module(m)
        c1.export_json("test/test.json")

        c2 = Can()
        c2.import_json("test/test.json")

        self.assertEqual(
            dict(c1.get()),
            dict(c2.get())
        )


if __name__ == '__main__':
    unittest.main()
