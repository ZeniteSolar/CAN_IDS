#!/bin/python

from can import Can
can = Can()

### MODULE: MIC17
module_mic17 = can.module(
    name = "mic17",
    signature = 9,
    description = "Modulo de Interface de Controle"
)
topic_motor = can.topic(
    msg = "motor",
    id = 10,
    description = "Motor controller parameters"
)
topic_motor.describe_byte(
    name = "motor",
    byte = 1,
    description = "Motor state",
    type = "bitfield",
    units = ""
)
topic_motor.describe_bit(
    name = "motor on",
    byte = 1,
    bit = 0
)
topic_motor.describe_byte(
    name = "D",
    byte = 1,
    description = "Motor Duty Cycle",
    type = "u8",
    units = "%"
)
topic_motor.describe_byte(
    name = "I",
    byte = 2,
    description = "Motor Soft Start",
    type = "u8",
    units = "%"
)

module_mic17.add_topic(topic_motor)
can.add_module(module_mic17)


### MODULE: MAM17

### MODULE: MAB19

### MODULE: MSC19

### MODULE: MCS19

### EXPORT
can.export_json("can_ids.json")
can.export_h("can_ids.h")

