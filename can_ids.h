/**
 * @file can_ids.h
 *
 * @defgroup CANAPP    Ids for can application
 *
 * @brief Ids for canbus application
 *
 */

#ifndef CAN_IDS_H
#define CAN_IDS_H 

//------------------------------------------------------------------------------

// GENERIC FIELDS FROM ANY MODULE's STATE MESSAGE
#define CAN_LENGTH_MSG_STATE            3
#define CAN_SIGNATURE_BYTE              0       //<! ID from compilation
#define CAN_STATE_MSG_STATE_BYTE        1       //<! state flags
#define CAN_STATE_MSG_ERROR_BYTE        2       //<! error flags

//------------------------------------------------------------------------------

// SIGNATURES
#define CAN_SIGNATURE_MAM17             190
#define CAN_SIGNATURE_MCS17             200
#define CAN_SIGNATURE_MAD17             210
#define CAN_SIGNATURE_MCC17_1           221
#define CAN_SIGNATURE_MCC17_2           222
#define CAN_SIGNATURE_MCC17_3           223
#define CAN_SIGNATURE_MCC17_4           224
#define CAN_SIGNATURE_MAB17             230
#define CAN_SIGNATURE_MIC17             240
#define CAN_SIGNATURE_MSC19_1           251
#define CAN_SIGNATURE_MSC19_2           252
#define CAN_SIGNATURE_MSC19_3           253
#define CAN_SIGNATURE_MSC19_4           254

#define CAN_SIGNATURE_SELF              CAN_SIGNATURE_MSC19_1

//------------------------------------------------------------------------------

// MASKS:
#define CAN_MASK_MIC17                  0b11111111111   //<! Mask for MIC17
#define CAN_MASK_MAM17                  0b11111111111   //<! Mask for MAM17
#define CAN_MASK_MAB17                  0b11111111111   //<! Mask for MAB17
#define CAN_MASK_MCS17                  0b11111111111   //<! Mask for MCS17
#define CAN_MASK_MAD17                  0b11111111111   //<! Mask for MAD17
#define CAN_MASK_MCC17                  0b11111111111   //<! Mask for MCC17
#define CAN_MASK_MSC19                  0b11111111111   //<! Mask for MSC19

//------------------------------------------------------------------------------

// FILTERS FOR MESSAGES FROM MIC17 :
#define CAN_FILTER_MSG_MIC17_STATE      0b00000001000   //<! Informs about state and errors
#define CAN_FILTER_MSG_MIC17_MOTOR      0b00000001001   //<! Informs about motor controls.
#define CAN_FILTER_MSG_MIC17_PUMPS      0b00000001010   //<! Informs about pumps controls.
#define CAN_FILTER_MSG_MIC17_MPPTS    	0b00000001011   //<! Informs about mppts controls.
#define CAN_FILTER_MSG_MIC17_MCS        0b00000001100   //<! Informs about boat_on to mcs.

// MESSAGES FROM MIC17 TO MAM17:4
#define CAN_LENGTH_MSG_MIC17_MOTOR          4
#define CAN_MSG_MIC17_MOTOR_MOTOR_ON_BYTE   1
#define CAN_MSG_MIC17_MOTOR_MOTOR_ON_BIT    0
#define CAN_MSG_MIC17_MOTOR_DMS_BYTE    	1
#define CAN_MSG_MIC17_MOTOR_DMS_BIT      	1
#define CAN_MSG_MIC17_MOTOR_D_RAW_BYTE	    2
#define CAN_MSG_MIC17_MOTOR_I_RAW_BYTE		3

// MESSAGES FROM MIC17 TO MAB17:
#define CAN_LENGTH_MSG_MIC17_PUMPS          2
#define CAN_MSG_MIC17_PUMPS_PUMPS_BYTE      1
#define CAN_MSG_MIC17_PUMPS_PUMP1_BIT       0
#define CAN_MSG_MIC17_PUMPS_PUMP2_BIT       1
#define CAN_MSG_MIC17_PUMPS_PUMP3_BIT       2

// MESSAGES FROM MIC17 TO MCC17_x:
#define CAN_LENGTH_MSG_MIC17_MPPTS          3
#define CAN_MSG_MIC17_MPPTS_MPPTS_ON_BYTE   1
#define CAN_MSG_MIC17_MPPTS_MPPTS_ON_BIT    0
#define CAN_MSG_MIC17_MPPTS_POT_BYTE        2

// MESSAGES FROM MIC17 TO MCS17:
#define CAN_LENGHT_MSG_MIC17_MCS            2
#define CAN_MSG_MIC17_MCS_BOAT_ON_BYTE      1
#define CAN_MSG_MIC17_MCS_BOAT_ON_BIT       0

//------------------------------------------------------------------------------

// FILTERS FOR MESSAGES FROM MAM17:
#define CAN_FILTER_MSG_MAM17_STATE      0b00000010000   //<! Informs about state and errors
#define CAN_FILTER_MSG_MAM17_MOTOR      0b00000010001   //<! Informs about motor

// MAM17 MOTOR:
#define CAN_LENGTH_MSG_MAM17_MOTOR      3
#define CAN_MSG_MAM17_MOTOR_D_BYTE      1
#define CAN_MSG_MAM17_MOTOR_LIM_BYTE    2

//------------------------------------------------------------------------------

// FILTERS FOR MESSAGES FROM MAB17:
#define CAN_FILTER_MSG_MAB17_STATE      0b00001000000   //<! Informs about state and errors
#define CAN_FILTER_MSG_MAB17_PUMPS      0b00001000001   //<! Informs about pumps

// MESSAGES FROM MIC17 TO MAM17:
#define CAN_LENGTH_MSG_MAB17_PUMPS      2
#define CAN_MSG_MAB17_PUMPS_BYTE        1
#define CAN_MSG_MAB17_PUMP1_BIT         0
#define CAN_MSG_MAB17_PUMP2_BIT         1
#define CAN_MSG_MAB17_PUMP3_BIT         2

//------------------------------------------------------------------------------

// FILTERS FOR MESSAGES FROM MCS17:
#define CAN_FILTER_MSG_MCS19_STATE      0b00100000000   //<! Informs about state and errors and main relay
// #define CAN_FILTER_MSG_MCS17_BOAT_ON    0b00100000001   //<! Informs about bat, cap and main relay
#define CAN_FILTER_MSG_MCS19_BAT    0b00100000010   //<! Informs about bat
#define CAN_FILTER_MSG_MCS19_CAP    0b00100000011   //<! Informs about cap
#define CAN_FILTER_MSG_MCS19_RELAY  0b00100000100   //<! Informs about main relay and charging relay

// MCS17 :
// #define CAN_LENGTH_MSG_MCS17_BOAT_ON    4
// #define CAN_MSG_MCS17_VBAT_BYTE         1
// #define CAN_MSG_MCS17_VCAP_BYTE         2
// #define CAN_MSG_MCS17_MAIN_RELAY_BYTE   3
// #define CAN_MSG_MCS17_MAIN_RELAY_BIT    0

#define CAN_LENGTH_MSG_MCS19_RELAY		3
#define CAN_MSG_MCS19_MAIN_RELAY_BYTE	1
#define CAN_MSG_MCS19_MAIN_RELAY_BIT	0
#define CAN_MSG_MCS19_CHARGE_RELAY_BYTE	2
#define CAN_MSG_MCS19_CHARGE_RELAY_BIT	0

#define CAN_LENGTH_MSG_MCS19_BAT        7
#define CAN_MSG_MCS19_BAT_AVG_BYTE_L    1
#define CAN_MSG_MCS19_BAT_AVG_BYTE_H    2
#define CAN_MSG_MCS19_BAT_MIN_BYTE_L    3
#define CAN_MSG_MCS19_BAT_MIN_BYTE_H    4
#define CAN_MSG_MCS19_BAT_MAX_BYTE_L    5
#define CAN_MSG_MCS19_BAT_MAX_BYTE_H    6

#define CAN_LENGTH_MSG_MCS19_CAP        7
#define CAN_MSG_MCS19_CAP_AVG_BYTE_L    1
#define CAN_MSG_MCS19_CAP_AVG_BYTE_H    2
#define CAN_MSG_MCS19_CAP_MIN_BYTE_L    3
#define CAN_MSG_MCS19_CAP_MIN_BYTE_H    4
#define CAN_MSG_MCS19_CAP_MAX_BYTE_L    5
#define CAN_MSG_MCS19_CAP_MAX_BYTE_H    6


//------------------------------------------------------------------------------

// FILTERS FOR MESSAGES FROM MAD17:
#define CAN_FILTER_MSG_MAD17_STATE      0b10000000000   //<! Informs about state and errors
 
//------------------------------------------------------------------------------

// FILTERS FOR MESSAGES FROM MCC17:
#define CAN_FILTER_MSG_MCC17_STATE      0b00000100000   //<! Informs about state and errors
#define CAN_FILTER_MSG_MCC17_MPPT       0b00000100001   //<! Informs about mppts

// MCC17 MPPT:
#define CAN_LENGTH_MSG_MCC17_MPPT       5
#define CAN_MSG_MCC17_MPPT_D_BYTE       1
#define CAN_MSG_MCC17_MPPT_IPANEL_BYTE  2
#define CAN_MSG_MCC17_MPPT_VPANEL_BYTE  3
#define CAN_MSG_MCC17_MPPT_VBAT_BYTE    4
 
//------------------------------------------------------------------------------

// FILTERS FOR MESSAGES FROM MSC19:
#define CAN_FILTER_MSG_MSC19_STATE      0b00000100000   //<! Informs about state and errors
#define CAN_FILTER_MSG_MSC19_ADC        0b00000100001   //<! Informs about adc

// MSC19 ADC:
#define CAN_LENGTH_MSG_MSC19_ADC        7
#define CAN_MSG_MSC19_ADC_AVG_BYTE_L    1
#define CAN_MSG_MSC19_ADC_AVG_BYTE_H    2
#define CAN_MSG_MSC19_ADC_MIN_BYTE_L    3
#define CAN_MSG_MSC19_ADC_MIN_BYTE_H    4
#define CAN_MSG_MSC19_ADC_MAX_BYTE_L    5
#define CAN_MSG_MSC19_ADC_MAX_BYTE_H    6
 
//------------------------------------------------------------------------------
 

#endif /* ifndef CAN_IDS_H */
