// CODE GENERATED USING MAKOTEMPLATES.ORG, DO NOT EDIT.
#define CAN_VERSION "${db["version"]}"

#include <stdint.h>

%for module in db["modules"]:
// ${module["name"]} - ${module["description"]}
#define CAN_SIGNATURE_${module["name"]} ${module["signature"]}
        %for topic in module["topics"]:
// ${module["name"]} - ${topic["name"]} - ${topic["description"]}
#define CAN_MSG_${module["name"]}_${topic["name"]}_ID ${topic["id"]}
#define CAN_MSG_${module["name"]}_${topic["name"]}_LENGTH ${len(list(filter(None, topic["bytes"])))}
#define CAN_MSG_${module["name"]}_${topic["name"]}_FREQUENCY ${int(topic["frequency"])}
            %for i,byte in enumerate(topic["bytes"]):
                %if byte:
#define CAN_MSG_${module["name"]}_${topic["name"]}_${byte["name"]}_BYTE ${i} //<!" ${byte["description"]}
#define CAN_MSG_${module["name"]}_${topic["name"]}_${byte["name"]}_TYPE ${ byte["type"] if byte["type"] != "bitfield" else "uint8_t"}
#define CAN_MSG_${module["name"]}_${topic["name"]}_${byte["name"]}_UNITS "${byte["units"]}"
                    %if "bits" in byte.keys():
                        %for k,bit in enumerate(byte["bits"]):
                            %if bit:
#define CAN_MSG_${module["name"]}_${topic["name"]}_${byte["name"]}_${bit}_BIT ${k}
                            %endif
                        %endfor
                    %endif
                %endif
            %endfor
        %endfor


%endfor
