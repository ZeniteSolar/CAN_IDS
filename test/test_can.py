#!/bin/python

import unittest
from can import Can

class test_can_topic(unittest.TestCase):
    def setUp(self):
        self.can = Can

    def test_topic(self):
        t = self.can.topic("motor", 9)
        expected = {
            "name": "CAN_FILTER_MSG_MOTOR",
            "id": 9,
            "bytes": [
                {"name": "SIGNATURE" },
                *[None]*7
            ]
        }

        self.assertEqual(
            dict(t.get()),
            expected
        )

    def test_describe_byte(self):
        t = self.can.topic("motor", 9)
        t.describe_byte("motor", 1)

        expected = {
            "name": "CAN_FILTER_MSG_MOTOR",
            "id": 9,
            "bytes": [
                {"name": "SIGNATURE" },
                {"name": "MOTOR"},
                *[None]*6
            ]
        }

        self.assertEqual(
            dict(t.get()),
            expected
        )

    def test_describe_bit(self):
        t = self.can.topic("motor", 9)
        t.describe_byte("motor", 1)
        t.describe_bit("motor on", 1, 0)

        expected = {
            "name": "CAN_FILTER_MSG_MOTOR",
            "id": 9,
            "bytes": [
                {"name": "SIGNATURE" },
                {"name": "MOTOR", "bits": ["MOTOR_ON", *[None]*7],},
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
        m = self.can.module("mic17", 10)

        expected = {
            "name": "MIC17",
            "signature": 10,
            "topics": []
        }

        self.assertEqual(
            dict(m.get()),
            expected
        )

    def test_add_topic(self):
        m = self.can.module("mic17", 10)
        t = self.can.topic("motor", 9)

        m.add_topic(t)

        expected = {
            "name": "MIC17",
            "signature": 10,
            "topics": [
                {
                    "name": "CAN_FILTER_MSG_MOTOR",
                    "id": 9,
                    "bytes": [
                        {"name": "SIGNATURE" },
                        *[None]*7
                    ]
                }
            ]
        }

        self.assertEqual(
            dict(m.get()),
            expected
        )


class test_can(unittest.TestCase):
    def setUp(self):
        self.can = Can

    def test_add_module(self):
        m = self.can.module("mic17", 10)
        c = Can()
        c.add_module(m)

        expected = {
            "modules": [
                {
                    "name": "MIC17",
                    "signature": 10,
                    "topics": []
                }
            ]
        }

        self.assertEqual(
            dict(c.get()),
            expected
        )


if __name__ == '__main__':
    unittest.main()
