#!/bin/python

from can import Can
can = Can()


### MODULE: MIC19
module_mic19 = can.module(
    name = "mic19",
    signature = 240,
    description = "Modulo de Interface de Controle"
)
#### TOPIC: STATE
topic_state = can.topic(
    msg = "state",
    id = 0b1000,
    description = "Module state report"
)
topic_state.describe_byte(
    name = "state",
    byte = 1,
    description = "State code",
    type = "u8",
    units = ""
)
topic_state.describe_byte(
    name = "error",
    byte = 2,
    description = "Error code",
    type = "u8",
    units = ""
)
#### TOPIC: MOTOR
topic_motor = can.topic(
    msg = "motor",
    id = 0b1001,
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
topic_motor.describe_bit(
    name = "dms on",
    byte = 1,
    bit = 1
)
topic_motor.describe_byte(
    name = "D",
    byte = 2,
    description = "Motor Duty Cycle",
    type = "u8",
    units = "%"
)
topic_motor.describe_byte(
    name = "I",
    byte = 3,
    description = "Motor Soft Start",
    type = "u8",
    units = "%"
)
#### TOPIC: PUMPS
topic_pumps = can.topic(
    msg = "pumps",
    id = 0b1010,
    description = "Pumps controller parameters"
)
topic_pumps.describe_byte(
    name = "pumps",
    byte = 1,
    description = "Pumps state",
    type = "bitfield",
    units = ""
)
topic_pumps.describe_bit(
    name = "pump1",
    byte = 1,
    bit = 0
)
topic_pumps.describe_bit(
    name = "pump2",
    byte = 1,
    bit = 1
)
topic_pumps.describe_bit(
    name = "pump3",
    byte = 1,
    bit = 2
)
#### TOPIC: MPPTS
topic_mppts = can.topic(
    msg = "mptts",
    id = 0b1011,
    description = "Mppts controller parameters"
)
topic_mppts.describe_byte(
    name = "mppts on",
    byte = 1,
    description = "MPPTs state",
    type = "bitfield",
    units = ""
)
topic_mppts.describe_bit(
    name = "mppts on",
    byte = 1,
    bit = 0
)
topic_mppts.describe_byte(
    name = "POT",
    byte = 2,
    description = "MPPTs maximum power limitation",
    type = "u8",
    units = "%"
)
#### TOPIC: MCS
topic_mcs = can.topic(
    msg = "mcs",
    id = 0b1100,
    description = "MCS controller parameters"
)
topic_mcs.describe_byte(
    name = "boat on",
    byte = 1,
    description = "Boat state",
    type = "bitfield",
    units = ""
)
topic_mcs.describe_bit(
    name = "boat on",
    byte = 1,
    bit = 0
)

module_mic19.add_topic(topic_state)
module_mic19.add_topic(topic_motor)
module_mic19.add_topic(topic_pumps)
module_mic19.add_topic(topic_mppts)
module_mic19.add_topic(topic_mcs)
can.add_module(module_mic19)


### MODULE: MAM19
module_mam19 = can.module(
    name = "mam19",
    signature = 190,
    description = "Modulo de Acionamento do Motor"
)
#### TOPIC: STATE
topic_state = can.topic(
    msg = "state",
    id = 0b10000,
    description = "Module state report"
)
topic_state.describe_byte(
    name = "state",
    byte = 1,
    description = "State code",
    type = "u8",
    units = ""
)
topic_state.describe_byte(
    name = "error",
    byte = 2,
    description = "Error code",
    type = "u8",
    units = ""
)
#### TOPIC: MOTOR
topic_motor = can.topic(
    msg = "motor",
    id = 0b10001,
    description = "Motor controller parameters"
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

module_mam19.add_topic(topic_state)
module_mam19.add_topic(topic_motor)
can.add_module(module_mam19)

### MODULE: MAB19
module_mab19 = can.module(
    name = "mab19",
    signature = 230,
    description = "Modulo de Acionamento das Bombas de Porao"
)

can.add_module(module_mab19)


### MODULE: MSC19
module_msc19 = can.module(
    name = "msc19",
    signature = 250,
    description = "Modulo de Sensores CAN"
)
#### TOPIC: STATE
topic_state = can.topic(
    msg = "state",
    id = 0b100000,
    description = "Module state report"
)
topic_state.describe_byte(
    name = "state",
    byte = 1,
    description = "State code",
    type = "u8",
    units = ""
)
topic_state.describe_byte(
    name = "error",
    byte = 2,
    description = "Error code",
    type = "u8",
    units = ""
)
#### TOPIC: ADC
topic_adc = can.topic(
    msg = "ADC",
    id = 0b100001,
    description = "ADC values"
)
topic_adc.describe_byte(
    name = "AVG_L",
    byte = 1,
    description = "Avg byte low",
    type = "u8",
    units = ""
)
topic_adc.describe_byte(
    name = "AVG_H",
    byte = 2,
    description = "Avg byte high",
    type = "u8",
    units = ""
)
topic_adc.describe_byte(
    name = "MIN_L",
    byte = 3,
    description = "Min byte low",
    type = "u8",
    units = ""
)
topic_adc.describe_byte(
    name = "MIN_H",
    byte = 4,
    description = "Min byte high",
    type = "u8",
    units = ""
)
topic_adc.describe_byte(
    name = "MAX_L",
    byte = 5,
    description = "Max byte low",
    type = "u8",
    units = ""
)
topic_adc.describe_byte(
    name = "MAX_H",
    byte = 6,
    description = "Max byte low",
    type = "u8",
    units = ""
)

module_msc19.add_topic(topic_state)
module_msc19.add_topic(topic_adc)
can.add_module(module_msc19)



### MODULE: MCS19
module_mcs19 = can.module(
    name = "mcs19",
    signature = 200,
    description = "Modulo de Carregamento do Sistema"
)
#### TOPIC: STATE
topic_state = can.topic(
    msg = "state",
    id = 0b00100000000,
    description = "Module state report"
)
topic_state.describe_byte(
    name = "state",
    byte = 1,
    description = "State code",
    type = "u8",
    units = ""
)
topic_state.describe_byte(
    name = "error",
    byte = 2,
    description = "Error code",
    type = "u8",
    units = ""
)

#### TOPIC: Start stages
topic_start_stages = can.topic(
    msg = "start_stages",
    id = 0b001000000100,
    description = "Boat charging // Boat on"
)
topic_start_stages.describe_byte(
    name = "main_relay",
    byte = 1,
    description = "Boat on/off",
    type = "bitfield",
    units = ""
)
topic_start_stages.describe_bit(
    name = "main_relay",
    byte = 1,
    bit = 0
)

topic_start_stages.describe_byte(
    name = "charge_relay",
    byte = 2,
    description = "Boat Charging",
    type = "bitfield",
    units = ""
)
topic_start_stages.describe_bit(
    name = "charge_relay",
    byte = 2,
    bit = 0
)


#### TOPIC: BATTERY
topic_bat = can.topic(
    msg = "BAT",
    id = 0b00100000010,
    description = "battery voltage values"
)
topic_bat.describe_byte(
    name = "AVG_L",
    byte = 1,
    description = "Avg byte low",
    type = "u8",
    units = ""
)
topic_bat.describe_byte(
    name = "AVG_H",
    byte = 2,
    description = "Avg byte high",
    type = "u8",
    units = ""
)
topic_bat.describe_byte(
    name = "MIN_L",
    byte = 3,
    description = "Min byte low",
    type = "u8",
    units = ""
)
topic_bat.describe_byte(
    name = "MIN_H",
    byte = 4,
    description = "Min byte high",
    type = "u8",
    units = ""
)
topic_bat.describe_byte(
    name = "MAX_L",
    byte = 5,
    description = "Max byte low",
    type = "u8",
    units = ""
)
topic_bat.describe_byte(
    name = "MAX_H",
    byte = 6,
    description = "Max byte low",
    type = "u8",
    units = ""
)


#### TOPIC: CAPACITOR
topic_cap = can.topic(
    msg = "CAP",
    id = 0b00100000011,
    description = "capacitor bank voltage values"
)
topic_cap.describe_byte(
    name = "AVG_L",
    byte = 1,
    description = "Avg byte low",
    type = "u8",
    units = ""
)
topic_cap.describe_byte(
    name = "AVG_H",
    byte = 2,
    description = "Avg byte high",
    type = "u8",
    units = ""
)
topic_cap.describe_byte(
    name = "MIN_L",
    byte = 3,
    description = "Min byte low",
    type = "u8",
    units = ""
)
topic_cap.describe_byte(
    name = "MIN_H",
    byte = 4,
    description = "Min byte high",
    type = "u8",
    units = ""
)
topic_cap.describe_byte(
    name = "MAX_L",
    byte = 5,
    description = "Max byte low",
    type = "u8",
    units = ""
)
topic_cap.describe_byte(
    name = "MAX_H",
    byte = 6,
    description = "Max byte low",
    type = "u8",
    units = ""
)



module_mcs19.add_topic(topic_state)
module_mcs19.add_topic(topic_start_stages)
module_mcs19.add_topic(topic_bat)
module_mcs19.add_topic(topic_cap)
can.add_module(module_mcs19)

### MODULE: MT19
module_mt19 = can.module(
    name = "mt19",
    signature = 255,
    description = "Modulo Tacometro"
)


can.add_module(module_mt19)



### EXPORT
can.export_json("can_ids.json")
can.export_h("can_ids.h")
