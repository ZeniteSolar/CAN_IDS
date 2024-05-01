import semver
import os
from can import Can

SEMVER_FILENAME = ".semver"

if os.path.exists(SEMVER_FILENAME):
    content = open(SEMVER_FILENAME, "r").readline()
    version = semver.VersionInfo.parse(content)
else:
    raise FileNotFoundError(
        f"File {SEMVER_FILENAME} not found. It should contain the version in semver standard.")

can = Can(version=f"{version}", bitrate=500e3)

################################################################################
### MODULE: GENERIC
module_generic = can.Module(
    name="generic",
    signature=0,
    description="Modulo generico para facilitar implementacoes genericas"
)
#### TOPIC: STATE
topic_state = can.Topic(
    msg="state",
    id=50,
    frequency=0,
    description="Module state report"
)
topic_state.describe_byte(
    name="state",
    byte=1,
    description="State code",
    btype="uint8_t",
    units=""
)
topic_state.describe_byte(
    name="error",
    byte=2,
    description="Error code",
    btype="uint8_t",
    units=""
)
#### TOPIC: GENERIC
topic_generic = can.Topic(
    msg="generic",
    id=51,
    frequency=0,
    description="Generic topic"
)

module_generic.add_topic(topic_state)
module_generic.add_topic(topic_generic)
can.add_module(module_generic)

################################################################################
### MODULE: MIC19
module_mic19 = can.Module(
    name="mic19",
    signature=240,
    description="Modulo de Interface de Controle"
)
#### TOPIC: STATE
topic_state = can.Topic(
    msg="state",
    id=30,
    description="Module state report",
    frequency = 5,
)
topic_state.describe_byte(
    name="state",
    byte=1,
    description="State code",
    btype="uint8_t",
    units=""
)
topic_state.describe_byte(
    name="error",
    byte=2,
    description="Error code",
    btype="uint8_t",
    units=""
)
#### TOPIC: MOTOR
topic_motor = can.Topic(
    msg="motor",
    id=31,
    description="Motor controller parameters",
    frequency = 50
)
topic_motor.describe_byte(
    name="motor",
    byte=1,
    description="Motor state",
    btype="bitfield",
    units=""
)
topic_motor.describe_bit(
    name="motor on",
    byte=1,
    bit=0
)
topic_motor.describe_bit(
    name="dms on",
    byte=1,
    bit=1
)
topic_motor.describe_bit(
    name="reverse",
    byte=1,
    bit=2
)
topic_motor.describe_byte(
    name="D",
    byte=2,
    description="Motor Duty Cycle",
    btype="uint8_t",
    units="%"
)
topic_motor.describe_byte(
    name="I",
    byte=3,
    description="Motor Soft Start",
    btype="uint8_t",
    units="%"
)
#### TOPIC: PUMPS
topic_pumps = can.Topic(
    msg="pumps",
    id=41,
    frequency = 4,
    description="Pumps controller parameters",
)
topic_pumps.describe_byte(
    name="pumps",
    byte=1,
    description="Pumps state",
    btype="bitfield",
    units=""
)
topic_pumps.describe_bit(
    name="pump1",
    byte=1,
    bit=0
)
topic_pumps.describe_bit(
    name="pump2",
    byte=1,
    bit=1
)
topic_pumps.describe_bit(
    name="pump3",
    byte=1,
    bit=2
)
#### TOPIC: MPPTS
topic_mppts = can.Topic(
    msg="mppts",
    id=200,
    frequency = 4, 
    description="Mppts controller parameters",
)
topic_mppts.describe_byte(
    name="mppts on",
    byte=1,
    description="MPPTs state",
    btype="bitfield",
    units=""
)
topic_mppts.describe_bit(
    name="mppts on",
    byte=1,
    bit=0
)
topic_mppts.describe_byte(
    name="POT",
    byte=2,
    description="MPPTs maximum power limitation",
    btype="uint8_t",
    units="%"
)
#### TOPIC: MCS
topic_mcs = can.Topic(
    msg="mcs",
    id=32,
    frequency = 50,
    description="MCS controller parameters",
)
topic_mcs.describe_byte(
    name="boat on",
    byte=1,
    description="Boat state",
    btype="bitfield",
    units=""
)
topic_mcs.describe_bit(
    name="boat on",
    byte=1,
    bit=0
)
#### TOPIC: MDE
topic_mde = can.Topic(
    msg="mde",
    id=33,
    frequency = 50,
    description="Steereing wheel controls",
)
topic_mde.describe_byte(
    name="position_l",
    byte=1,
    description="Steering wheel position, byte LOW",
    btype="uint16_t",
    units="°/100"
)
topic_mde.describe_byte(
    name="position_h",
    byte=2,
    description="Steering wheel position, byte HIGH",
    btype="uint16_t",
    units="°/100"
)

module_mic19.add_topic(topic_state)
module_mic19.add_topic(topic_motor)
module_mic19.add_topic(topic_pumps)
module_mic19.add_topic(topic_mppts)
module_mic19.add_topic(topic_mcs)
module_mic19.add_topic(topic_mde)
can.add_module(module_mic19)

################################################################################
### MODULE: MDE22
module_mde22 = can.Module(
    name="mde22",
    signature=170,
    description="Modulo da Direção Elétrica"
)
### TOPIC: STATE
topic_state = can.Topic(
    msg="state",
    id=100,
    frequency=1,
    description="Module state report"
)
topic_state.describe_byte(
    name="state",
    byte=1,
    description="State code",
    btype="uint8_t",
    units=""
)
topic_state.describe_byte(
    name="error",
    byte=2,
    description="Error code",
    btype="uint8_t",
    units=""
)
# TOPIC: STEERING MODULE MEASUREMENTS
topic_measurements = can.Topic(
    msg="steeringbat_measurements",
    id=201,
    frequency=10,
    description="Auxiliar Battery Voltage"
)
topic_measurements.describe_byte(
    name="batvoltage_l",
    byte=1,
    description="Battery Voltage, byte low",
    btype="uint16_t",
    units="V/100"
)
topic_measurements.describe_byte(
    name="batvoltage_h",
    byte=2,
    description="Battery Voltage, byte high",
    btype="uint16_t",
    units="V/100"
)
topic_measurements.describe_byte(
    name="position_l",
    byte=3,
    description="Tail Poisition, byte low",
    btype="uint16_t",
    units="°/100"
)
topic_measurements.describe_byte(
    name="position_h",
    byte=4,
    description="Tail Poisition, byte high",
    btype="uint16_t",
    units="°/100"
)
topic_measurements.describe_byte(
    name="batcurrent_l",
    byte=5,
    description="Battery Current, byte low",
    btype="uint16_t",
    units="A/100"
)
topic_measurements.describe_byte(
    name="batcurrent_h",
    byte=6,
    description="Battery Current, byte high",
    btype="uint16_t",
    units="A/100"
)

module_mde22.add_topic(topic_state)
module_mde22.add_topic(topic_measurements)
can.add_module(module_mde22)

################################################################################
### MODULE: MVC19
module_mvc19 = can.Module(
    name="mvc19",
    signature=210,
    description="Modulo de voltimetro"
)
### TOPIC: STATE
topic_state = can.Topic(
    msg="state",
    id=101,
    frequency=1,
    description="Module state report"
)
topic_state.describe_byte(
    name="state",
    byte=1,
    description="State code",
    btype="uint8_t",
    units=""
)
topic_state.describe_byte(
    name="error",
    byte=2,
    description="Error code",
    btype="uint8_t",
    units=""
)

module_mvc19.add_topic(topic_state)
can.add_multiple_modules(module_mvc19, 2)

################################################################################
### MODULE: MCC23
module_mcc23 = can.Module(
    name="mcc23",
    signature=225,
    description="Modulo controlador de carga"
)
#### TOPIC: STATE
topic_state = can.Topic(
    msg="state",
    id=103,
    frequency=1,
    description="Module state report"
)
topic_state.describe_byte(
    name="state",
    byte=1,
    description="State code",
    btype="uint8_t",
    units=""
)
topic_state.describe_byte(
    name="error",
    byte=2,
    description="Error code",
    btype="uint8_t",
    units=""
)
topic_state.describe_byte(
    name="control",
    byte=2,
    description="Control flags for operating point",
    btype="bitfield",
    units=""
)
topic_state.describe_bit(
    name="enable",
    byte=2,
    bit=0
)
topic_state.describe_bit(
    name="vi_safe_range",
    byte=2,
    bit=1
)
topic_state.describe_bit(
    name="vo_safe_range",
    byte=2,
    bit=2
)
topic_state.describe_bit(
    name="vi_stable",
    byte=2,
    bit=3
)
topic_state.describe_bit(
    name="dt_safe_range",
    byte=2,
    bit=4
)

### TOPIC: MEASUREMENTS
topic_measurements = can.Topic(
    msg="measurements",
    id=202,
    frequency=10,
    description="All measurements from the converter"
)
topic_measurements.describe_byte(
    name="output_voltage_l",
    byte=1,
    description="Average output voltage, byte low",
    btype="uint16_t",
    units="V/100"
)
topic_measurements.describe_byte(
    name="output_voltage_h",
    byte=2,
    description="Average output voltage, byte high",
    btype="uint16_t",
    units="V/100"
)
topic_measurements.describe_byte(
    name="input_current_l",
    byte=3,
    description="Average input current, byte low",
    btype="uint16_t",
    units="A/100"
)
topic_measurements.describe_byte(
    name="input_current_h",
    byte=4,
    description="Average input current, byte high",
    btype="uint16_t",
    units="A/100"
)
topic_measurements.describe_byte(
    name="input_voltage_l",
    byte=5,
    description="Average input voltage, byte low",
    btype="uint16_t",
    units="V/100"
)
topic_measurements.describe_byte(
    name="input_voltage_h",
    byte=6,
    description="Average input voltage, byte high",
    btype="uint16_t",
    units="V/100"
)
topic_measurements.describe_byte(
    name="dt",
    byte=7,
    description="converter's duty cycle",
    btype="uint8_t",
    units="%/255"
)

### TOPIC: AUXILIARY MEASUREMENTS
topic_aux_measurements = can.Topic(
    msg="aux_measurements",
    id=225,
    frequency=10,
    description="Auxiliary measurements from the converter"
)
topic_aux_measurements.describe_byte(
    name="output_current_l",
    byte=1,
    description="Average output current, byte low",
    btype="uint16_t",
    units="A/100"
)
topic_aux_measurements.describe_byte(
    name="output_current_h",
    byte=2,
    description="Average output current, byte high",
    btype="uint16_t",
    units="A/100"
)
topic_aux_measurements.describe_byte(
    name="mosfet_temp",
    byte=3,
    description="MOSFET temperature",
    btype="uint8_t",
    units="°C"
)
topic_aux_measurements.describe_byte(
    name="diode_temp",
    byte=4,
    description="Diode temperature",
    btype="uint8_t",
    units="°C"
)

module_mcc23.add_topic(topic_state)
module_mcc23.add_topic(topic_measurements)
module_mcc23.add_topic(topic_aux_measurements)
can.add_multiple_modules(module_mcc23, 9)


################################################################################
### MODULE: MCB19
module_mcb19 = can.Module(
    name="mcb19",
    signature=220,
    description="Modulo de carregamento das baterias auxiliares"
)
#### TOPIC: STATE
topic_state = can.Topic(
    msg="state",
    id=118,
    frequency=1,
    description="Module state report"
)
topic_state.describe_byte(
    name="state",
    byte=1,
    description="State code",
    btype="uint8_t",
    units=""
)
topic_state.describe_byte(
    name="error",
    byte=2,
    description="Error code",
    btype="uint8_t",
    units=""
)
topic_state.describe_byte(
    name="control",
    byte=2,
    description="Control flags for operating point",
    btype="bitfield",
    units=""
)
topic_state.describe_bit(
    name="enable",
    byte=2,
    bit=0
)
topic_state.describe_bit(
    name="vi_safe_range",
    byte=2,
    bit=1
)
topic_state.describe_bit(
    name="vo_safe_range",
    byte=2,
    bit=2
)
topic_state.describe_bit(
    name="vi_stable",
    byte=2,
    bit=3
)
topic_state.describe_bit(
    name="dt_safe_range",
    byte=2,
    bit=4
)

### TOPIC: MEASUREMENTS
topic_measurements = can.Topic(
    msg="measurements",
    id=222,
    frequency=10,
    description="All measurements from the converter"
)
topic_measurements.describe_byte(
    name="output_voltage_l",
    byte=1,
    description="Average output voltage, byte low",
    btype="uint16_t",
    units="V/100"
)
topic_measurements.describe_byte(
    name="output_voltage_h",
    byte=2,
    description="Average output voltage, byte high",
    btype="uint16_t",
    units="V/100"
)
topic_measurements.describe_byte(
    name="output_current_l",
    byte=3,
    description="Average output current, byte low",
    btype="uint16_t",
    units="A/100"
)
topic_measurements.describe_byte(
    name="output_current_h",
    byte=4,
    description="Average output current, byte high",
    btype="uint16_t",
    units="A/100"
)
topic_measurements.describe_byte(
    name="input_voltage_l",
    byte=5,
    description="Average input voltage, byte low",
    btype="uint16_t",
    units="V/100"
)
topic_measurements.describe_byte(
    name="input_voltage_h",
    byte=6,
    description="Average input voltage, byte high",
    btype="uint16_t",
    units="V/100"
)
topic_measurements.describe_byte(
    name="dt",
    byte=7,
    description="converter's duty cycle",
    btype="uint8_t",
    units="%/255"
)

module_mcb19.add_topic(topic_state)
module_mcb19.add_topic(topic_measurements)
can.add_multiple_modules(module_mcb19, 2) 

################################################################################
### MODULE: MAC22
module_mac22 = can.Module(
    name="mac22",
    signature=180,
    description="Modulo de Acionamento da Contatora"
)
#### TOPIC: STATE
topic_state = can.Topic(
    msg="state",
    id=35,
    frequency=5,
    description="Module state report",
)
topic_state.describe_byte(
    name="state",
    byte=1,
    description="State code",
    btype="uint8_t",
    units=""
)
topic_state.describe_byte(
    name="error",
    byte=2,
    description="Error code",
    btype="uint8_t",
    units=""
)
#### TOPIC: CONTACTOR
topic_contactor = can.Topic(
    msg="contactor",
    id=34,
    frequency=50,
    description="Contactor task response",
)
topic_contactor.describe_byte(
    name="response",
    byte=1,
    description="Contactor task response",
    btype="uint8_t",
    units=""
)

module_mac22.add_topic(topic_state)
module_mac22.add_topic(topic_contactor)
can.add_module(module_mac22)


################################################################################
### MODULE: MAM19
module_mam19 = can.Module(
    name="mam19",
    signature=190,
    description="Modulo de Acionamento do Motor"
)
#### TOPIC: STATE
topic_state = can.Topic(
    msg="state",
    id=0b1100011,
    frequency=5,
    description="Module state report"
)
topic_state.describe_byte(
    name="state",
    byte=1,
    description="State code",
    btype="uint8_t",
    units=""
)
topic_state.describe_byte(
    name="error",
    byte=2,
    description="Error code",
    btype="uint8_t",
    units=""
)
#### TOPIC: MOTOR
topic_motor = can.Topic(
    msg="motor",
    id=0b1100010,
    frequency=50,
    description="Motor controller parameters"
)
topic_motor.describe_byte(
    name="D",
    byte=1,
    description="Motor Duty Cycle",
    btype="uint8_t",
    units="%"
)
topic_motor.describe_byte(
    name="I",
    byte=2,
    description="Motor Soft Start",
    btype="uint8_t",
    units="%"
)
#### TOPIC: CONTACTOR
topic_contactor = can.Topic(
    msg="contactor",
    id=0b100100,
    frequency=5,
    description="Contactor requests"
)
topic_contactor.describe_byte(
    name="request",
    byte=1,
    description="Control the Contactor State",
    btype="uint8_t",
    units=""
)

module_mam19.add_topic(topic_state)
module_mam19.add_topic(topic_motor)
module_mam19.add_topic(topic_contactor)
can.add_module(module_mam19)


################################################################################
### MODULE: MAB19
module_mab19 = can.Module(
    name="mab19",
    signature=235,
    description="Modulo de Acionamento das Bombas de Porao"
)

#### TOPIC: STATE
topic_state = can.Topic(
    msg="state",
    id=120,
    frequency=0,
    description="Module state report"
)
topic_state.describe_byte(
    name="state",
    byte=1,
    description="State code",
    btype="uint8_t",
    units=""
)
topic_state.describe_byte(
    name="error",
    byte=2,
    description="Error code",
    btype="uint8_t",
    units=""
)

#### TOPIC: PUMPS
topic_pumps = can.Topic(
    msg="pumps",
    id=224,
    frequency=0,
    description="Pumps state",
)
topic_pumps.describe_byte(
    name="pumps",
    byte=1,
    description="Pumps state",
    btype="bitfield",
    units=""
)
topic_pumps.describe_bit(
    name="pump1",
    byte=1,
    bit=0
)
topic_pumps.describe_bit(
    name="pump2",
    byte=1,
    bit=1
)
topic_pumps.describe_bit(
    name="pump3",
    byte=1,
    bit=2
)

module_mab19.add_topic(topic_state)
module_mab19.add_topic(topic_pumps)
can.add_module(module_mab19)


################################################################################
### MODULE: MSC19
module_msc19_1 = can.Module(
    name="msc19_1",
    signature=250,
    description="Main Battery Voltage Sensor"
)
#### TOPIC: STATE
topic_state = can.Topic(
    msg="state",
    id=0b1110000,
    frequency=1,
    description="Module state report"
)
topic_state.describe_byte(
    name="state",
    byte=1,
    description="State code",
    btype="uint8_t",
    units=""
)
topic_state.describe_byte(
    name="error",
    byte=2,
    description="Error code",
    btype="uint8_t",
    units=""
)
#### TOPIC: ADC
topic_adc = can.Topic(
    msg="ADC",
    id=0b11010011,
    frequency=10,
    description="Voltage measurements"
)
topic_adc.describe_byte(
    name="AVG_L",
    byte=1,
    description="Average, byte low",
    btype="uint16_t",
    units="V/100"
)
topic_adc.describe_byte(
    name="AVG_H",
    byte=2,
    description="Average, byte high",
    btype="uint16_t",
    units="V/100"
)
topic_adc.describe_byte(
    name="MIN_L",
    byte=3,
    description="Min byte low",
    btype="uint16_t",
    units="V/100"
)
topic_adc.describe_byte(
    name="MIN_H",
    byte=4,
    description="Min byte high",
    btype="uint16_t",
    units="V/100"
)
topic_adc.describe_byte(
    name="MAX_L",
    byte=5,
    description="Max byte low",
    btype="uint16_t",
    units="V/100"
)
topic_adc.describe_byte(
    name="MAX_H",
    byte=6,
    description="Max byte low",
    btype="uint16_t",
    units="V/100"
)

module_msc19_1.add_topic(topic_state)
module_msc19_1.add_topic(topic_adc)
can.add_module(module_msc19_1)


################################################################################
### MODULE: MSC19_2
module_msc19_2 = can.Module(
    name="msc19_2",
    signature=251,
    description="Auxilliary Battery Voltage Sensor"
)
#### TOPIC: STATE
topic_state = can.Topic(
    msg="state",
    id=0b1110001,
    frequency=1,
    description="Module state report"
)
topic_state.describe_byte(
    name="state",
    byte=1,
    description="State code",
    btype="uint8_t",
    units=""
)
topic_state.describe_byte(
    name="error",
    byte=2,
    description="Error code",
    btype="uint8_t",
    units=""
)
#### TOPIC: ADC
topic_adc = can.Topic(
    msg="ADC",
    id=0b11010100,
    frequency=10,
    description="Voltage measurements"
)
topic_adc.describe_byte(
    name="AVG_L",
    byte=1,
    description="Average, byte low",
    btype="uint16_t",
    units="V/100"
)
topic_adc.describe_byte(
    name="AVG_H",
    byte=2,
    description="Average, byte high",
    btype="uint16_t",
    units="V/100"
)
topic_adc.describe_byte(
    name="MIN_L",
    byte=3,
    description="Min byte low",
    btype="uint16_t",
    units="V/100"
)
topic_adc.describe_byte(
    name="MIN_H",
    byte=4,
    description="Min byte high",
    btype="uint16_t",
    units="V/100"
)
topic_adc.describe_byte(
    name="MAX_L",
    byte=5,
    description="Max byte low",
    btype="uint16_t",
    units="V/100"
)
topic_adc.describe_byte(
    name="MAX_H",
    byte=6,
    description="Max byte low",
    btype="uint16_t",
    units="V/100"
)

module_msc19_2.add_topic(topic_state)
module_msc19_2.add_topic(topic_adc)
can.add_module(module_msc19_2)


################################################################################
### MODULE: MSC19_3
module_msc19_3 = can.Module(
    name="msc19_3",
    signature=252,
    description="Extra Battery Voltage Sensor"
)
#### TOPIC: STATE
topic_state = can.Topic(
    msg="state",
    id=0b1110010,
    frequency=1,
    description="Module state report"
)
topic_state.describe_byte(
    name="state",
    byte=1,
    description="State code",
    btype="uint8_t",
    units=""
)
topic_state.describe_byte(
    name="error",
    byte=2,
    description="Error code",
    btype="uint8_t",
    units=""
)
#### TOPIC: ADC
topic_adc = can.Topic(
    msg="ADC",
    id=0b11010101,
    frequency=10,
    description="Voltage measurements"
)
topic_adc.describe_byte(
    name="AVG_L",
    byte=1,
    description="Average, byte low",
    btype="uint16_t",
    units="V/100"
)
topic_adc.describe_byte(
    name="AVG_H",
    byte=2,
    description="Average, byte high",
    btype="uint16_t",
    units="V/100"
)
topic_adc.describe_byte(
    name="MIN_L",
    byte=3,
    description="Min byte low",
    btype="uint16_t",
    units="V/100"
)
topic_adc.describe_byte(
    name="MIN_H",
    byte=4,
    description="Min byte high",
    btype="uint16_t",
    units="V/100"
)
topic_adc.describe_byte(
    name="MAX_L",
    byte=5,
    description="Max byte low",
    btype="uint16_t",
    units="V/100"
)
topic_adc.describe_byte(
    name="MAX_H",
    byte=6,
    description="Max byte low",
    btype="uint16_t",
    units="V/100"
)

module_msc19_3.add_topic(topic_state)
module_msc19_3.add_topic(topic_adc)
can.add_module(module_msc19_3)


################################################################################
### MODULE: MSC19_4
module_msc19_4 = can.Module(
    name="msc19_4",
    signature=253,
    description="Main Battery Input Current Sensor"
)
#### TOPIC: STATE
topic_state = can.Topic(
    msg="state",
    id=0b1110011,
    frequency=1,
    description="Module state report"
)
topic_state.describe_byte(
    name="state",
    byte=1,
    description="State code",
    btype="uint8_t",
    units=""
)
topic_state.describe_byte(
    name="error",
    byte=2,
    description="Error code",
    btype="uint8_t",
    units=""
)
#### TOPIC: ADC
topic_adc = can.Topic(
    msg="ADC",
    id=0b11010110,
    frequency=10,
    description="Current measurements"
)
topic_adc.describe_byte(
    name="AVG_L",
    byte=1,
    description="Average, byte low",
    btype="uint16_t",
    units="A/100"
)
topic_adc.describe_byte(
    name="AVG_H",
    byte=2,
    description="Average, byte high",
    btype="uint16_t",
    units="A/100"
)
topic_adc.describe_byte(
    name="MIN_L",
    byte=3,
    description="Min byte low",
    btype="uint16_t",
    units="A/100"
)
topic_adc.describe_byte(
    name="MIN_H",
    byte=4,
    description="Min byte high",
    btype="uint16_t",
    units="A/100"
)
topic_adc.describe_byte(
    name="MAX_L",
    byte=5,
    description="Max byte low",
    btype="uint16_t",
    units="A/100"
)
topic_adc.describe_byte(
    name="MAX_H",
    byte=6,
    description="Max byte low",
    btype="uint16_t",
    units="A/100"
)

module_msc19_4.add_topic(topic_state)
module_msc19_4.add_topic(topic_adc)
can.add_module(module_msc19_4)


################################################################################
### MODULE: MSC19_5
module_msc19_5 = can.Module(
    name="msc19_5",
    signature=254,
    description="Main Battery Output Current Sensor"
)
#### TOPIC: STATE
topic_state = can.Topic(
    msg="state",
    id=0b1110100,
    frequency=1,
    description="Module state report"
)
topic_state.describe_byte(
    name="state",
    byte=1,
    description="State code",
    btype="uint8_t",
    units=""
)
topic_state.describe_byte(
    name="error",
    byte=2,
    description="Error code",
    btype="uint8_t",
    units=""
)
#### TOPIC: ADC
topic_adc = can.Topic(
    msg="ADC",
    id=0b11010111,
    frequency=10,
    description="Current measurements"
)
topic_adc.describe_byte(
    name="AVG_L",
    byte=1,
    description="Average, byte low",
    btype="uint16_t",
    units="A/100"
)
topic_adc.describe_byte(
    name="AVG_H",
    byte=2,
    description="Average, byte high",
    btype="uint16_t",
    units="A/100"
)
topic_adc.describe_byte(
    name="MIN_L",
    byte=3,
    description="Min byte low",
    btype="uint16_t",
    units="A/100"
)
topic_adc.describe_byte(
    name="MIN_H",
    byte=4,
    description="Min byte high",
    btype="uint16_t",
    units="A/100"
)
topic_adc.describe_byte(
    name="MAX_L",
    byte=5,
    description="Max byte low",
    btype="uint16_t",
    units="A/100"
)
topic_adc.describe_byte(
    name="MAX_H",
    byte=6,
    description="Max byte low",
    btype="uint16_t",
    units="A/100"
)

module_msc19_5.add_topic(topic_state)
module_msc19_5.add_topic(topic_adc)
can.add_module(module_msc19_5)


################################################################################
### MODULE: MCS19
module_mcs19 = can.Module(
    name="mcs19",
    signature=200,
    description="Modulo de Carregamento do Sistema"
)
#### TOPIC: STATE
topic_state = can.Topic(
    msg="state",
    id=117,
    frequency=1,
    description="Module state report",
)
topic_state.describe_byte(
    name="state",
    byte=1,
    description="State code",
    btype="uint8_t",
    units=""
)
topic_state.describe_byte(
    name="error",
    byte=2,
    description="Error code",
    btype="uint8_t",
    units=""
)

# TOPIC: Start stages
topic_start_stages = can.Topic(
    msg="start_stages",
    id=0b100101,
    frequency=50,
    description="Boat charging // Boat on"
)
topic_start_stages.describe_byte(
    name="main_relay",
    byte=1,
    description="Boat on/off",
    btype="bitfield",
    units=""
)
topic_start_stages.describe_bit(
    name="main_relay",
    byte=1,
    bit=0
)

topic_start_stages.describe_byte(
    name="charge_relay",
    byte=2,
    description="Boat Charging",
    btype="bitfield",
    units=""
)
topic_start_stages.describe_bit(
    name="charge_relay",
    byte=2,
    bit=0
)

#### TOPIC: BATTERY
topic_bat = can.Topic(
    msg="BAT",
    id=0b11011000,
    frequency=10,
    description="battery voltage values"
)
topic_bat.describe_byte(
    name="AVG_L",
    byte=1,
    description="Average, byte low",
    btype="uint16_t",
    units=""
)
topic_bat.describe_byte(
    name="AVG_H",
    byte=2,
    description="Average, byte high",
    btype="uint16_t",
    units=""
)
topic_bat.describe_byte(
    name="MIN_L",
    byte=3,
    description="Min byte low",
    btype="uint16_t",
    units=""
)
topic_bat.describe_byte(
    name="MIN_H",
    byte=4,
    description="Min byte high",
    btype="uint16_t",
    units=""
)
topic_bat.describe_byte(
    name="MAX_L",
    byte=5,
    description="Max byte low",
    btype="uint16_t",
    units=""
)
topic_bat.describe_byte(
    name="MAX_H",
    byte=6,
    description="Max byte low",
    btype="uint16_t",
    units=""
)

#### TOPIC: CAPACITOR
topic_cap = can.Topic(
    msg="CAP",
    id=0b11011001,
    frequency=10,
    description="capacitor bank voltage values"
)
topic_cap.describe_byte(
    name="AVG_L",
    byte=1,
    description="Average, byte low",
    btype="uint16_t",
    units=""
)
topic_cap.describe_byte(
    name="AVG_H",
    byte=2,
    description="Average, byte high",
    btype="uint16_t",
    units=""
)
topic_cap.describe_byte(
    name="MIN_L",
    byte=3,
    description="Min byte low",
    btype="uint16_t",
    units=""
)
topic_cap.describe_byte(
    name="MIN_H",
    byte=4,
    description="Min byte high",
    btype="uint16_t",
    units=""
)
topic_cap.describe_byte(
    name="MAX_L",
    byte=5,
    description="Max byte low",
    btype="uint16_t",
    units=""
)
topic_cap.describe_byte(
    name="MAX_H",
    byte=6,
    description="Max byte low",
    btype="uint16_t",
    units=""
)

module_mcs19.add_topic(topic_state)
module_mcs19.add_topic(topic_start_stages)
module_mcs19.add_topic(topic_bat)
module_mcs19.add_topic(topic_cap)
can.add_module(module_mcs19)


################################################################################
### MODULE: MT19
module_mt19 = can.Module(
    name="mt19",
    signature=255,
    description="Modulo Tacometro"
)

#### TOPIC: STATE
topic_state = can.Topic(
    msg="state",
    id=0b11011010,
    description="Module state report",
    frequency = 0
)
topic_state.describe_byte(
    name="state",
    byte=1,
    description="State code",
    btype="uint8_t",
    units=""
)
topic_state.describe_byte(
    name="error",
    byte=2,
    description="Error code",
    btype="uint8_t",
    units=""
)

#### TOPIC: RPM
topic_rpm = can.Topic(
    msg="RPM",
    id=0b11011011,
    description="RPM motor values",
    frequency = 0
)
topic_rpm.describe_byte(
    name="AVG_L",
    byte=1,
    description="RPM Average, byte low",
    btype="uint16_t",
    units=""
)
topic_rpm.describe_byte(
    name="AVG_H",
    byte=2,
    description="RPM Average, byte high",
    btype="uint16_t",
    units=""
)

module_mt19.add_topic(topic_state)
module_mt19.add_topic(topic_rpm)
can.add_module(module_mt19)


################################################################################
### MODULE: MSWI19
module_mswi19 = can.Module(
    name="mswi19",
    signature=241,
    description="Modulo de Interface de Controle"
)
#### TOPIC: STATE
topic_state = can.Topic(
    msg="state",
    id=0b1001,
    description="Module state report",
    frequency = 5
)
topic_state.describe_byte(
    name="state",
    byte=1,
    description="State code",
    btype="uint8_t",
    units=""
)
topic_state.describe_byte(
    name="error",
    byte=2,
    description="Error code",
    btype="uint8_t",
    units=""
)
#### TOPIC: MOTOR
topic_motor = can.Topic(
    msg="motor",
    id=0b1010,
    description="Motor controller parameters",
    frequency = 50
)
topic_motor.describe_byte(
    name="motor",
    byte=1,
    description="Motor state",
    btype="bitfield",
    units=""
)
topic_motor.describe_bit(
    name="motor on",
    byte=1,
    bit=0
)
topic_motor.describe_bit(
    name="dms on",
    byte=1,
    bit=1
)
topic_motor.describe_byte(
    name="D",
    byte=2,
    description="Motor Duty Cycle",
    btype="uint8_t",
    units="%"
)
topic_motor.describe_byte(
    name="I",
    byte=3,
    description="Motor Soft Start",
    btype="uint8_t",
    units="%"
)
#### TOPIC: PUMPS
topic_pumps = can.Topic(
    msg="pumps",
    id=0b11011100,
    description="Pumps controller parameters",
    frequency = 0
)
topic_pumps.describe_byte(
    name="pumps",
    byte=1,
    description="Pumps state",
    btype="bitfield",
    units=""
)
topic_pumps.describe_bit(
    name="pump1",
    byte=1,
    bit=0
)
topic_pumps.describe_bit(
    name="pump2",
    byte=1,
    bit=1
)
topic_pumps.describe_bit(
    name="pump3",
    byte=1,
    bit=2
)
#### TOPIC: MPPTS
topic_mppts = can.Topic(
    msg="mppts",
    id=0b11011101,
    description="Mppts controller parameters",
    frequency = 0
)
topic_mppts.describe_byte(
    name="mppts on",
    byte=1,
    description="MPPTs state",
    btype="bitfield",
    units=""
)
topic_mppts.describe_bit(
    name="mppts on",
    byte=1,
    bit=0
)
topic_mppts.describe_byte(
    name="POT",
    byte=2,
    description="MPPTs maximum power limitation",
    btype="uint8_t",
    units="%"
)
#### TOPIC: MCS
topic_mcs = can.Topic(
    msg="mcs",
    id=0b101000,
    description="MCS controller parameters",
    frequency = 1
)
topic_mcs.describe_byte(
    name="boat on",
    byte=1,
    description="Boat state",
    btype="bitfield",
    units=""
)
topic_mcs.describe_bit(
    name="boat on",
    byte=1,
    bit=0
)

module_mswi19.add_topic(topic_state)
module_mswi19.add_topic(topic_motor)
module_mswi19.add_topic(topic_pumps)
module_mswi19.add_topic(topic_mppts)
module_mswi19.add_topic(topic_mcs)
can.add_module(module_mswi19)
