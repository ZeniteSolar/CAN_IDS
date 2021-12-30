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

    def test_validate_byte(self):
        t = self.can.topic("motor", 9, "topic description text here")

        # Trying to add using wrong type on the byte should raise TypeError:
        with self.assertRaises(TypeError):
            t.describe_byte("some byte", "1", "byte description text here", 'u8')

        # Trying to add byte with a value less than zero should raise ValueError:
        with self.assertRaises(ValueError):
            t.describe_byte("some byte", -1, "byte description text here", 'u8')

        # Trying to add byte with a value greater than 7 should raise ValueError:
        with self.assertRaises(ValueError):
            t.describe_byte("some byte", 8, "byte description text here", 'u8')

        # But using the correct type and range should run with no errors:
        t.describe_byte("some byte", 1, "byte description text here", 'u8')

    def test_validate_bit(self):
        t = self.can.topic("motor", 9, "topic description text here")
        t.describe_byte("some byte", 1, "byte description text here",
                        'bitfield')

        # Trying to add using wrong type on the bit should raise TypeError:
        with self.assertRaises(TypeError):
            t.describe_bit(0, 1, "0")

        # Trying to add bit with a value less than zero should raise ValueError:
        with self.assertRaises(ValueError):
            t.describe_bit("some bit", 1, -1)

        # Trying to add bit with a value greater than 7 should raise ValueError:
        with self.assertRaises(ValueError):
            t.describe_bit("some bit", 1, 8)

        # But using the correct type and range should run with no errors:
        t.describe_bit("some bit", 1, 0)

    def test_validate_byte_name(self):
        t = self.can.topic("motor", 9, "topic description text here")

        # Trying to add using wrong type on the name should raise TypeError:
        with self.assertRaises(TypeError):
            t.describe_byte(0, 1, "byte description text here", 'u8')

        t.describe_byte("some byte", 1, "byte description text here", 'u8')

        # Trying to add the same name should raise ValueError:
        with self.assertRaises(ValueError):
            t.describe_byte("some byte", 1, "byte description text here", 'u8')

    def test_validate_bit_name(self):
        t = self.can.topic("motor", 9, "topic description text here")
        t.describe_byte("some byte", 1, "byte description text here",
                        'bitfield')

        # Trying to add using wrong type on the name should raise TypeError:
        with self.assertRaises(TypeError):
            t.describe_bit(0, 1, 0)

        t.describe_bit("some bit", 1, 0)

        # Trying to add the same name should raise ValueError:
        with self.assertRaises(ValueError):
            t.describe_bit("some bit", 1, 1)


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

        # But trying to add the same topic twice should raise ValueError:
        with self.assertRaises(ValueError):
            m.add_topic(t)


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

        # But trying to add the same module twice should raise ValueError:
        with self.assertRaises(ValueError):
            c.add_module(m)

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
