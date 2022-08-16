// CODE GENERATED USING MAKOTEMPLATES.ORG, DO NOT EDIT.
#define CAN_VERSION "${db["version"]}"

#include <stdint.h>

%for module in db["modules"]:
    %for topic in module["topics"]:

// ${topic["description"]}
typedef struct
{
    union {
        uint8_t raw[8];
        struct {
        %for byte in topic["bytes"]:
            %if byte is not None:
                %if byte["type"] == "bitfield":
            struct { // ${byte["description"]}
                    %for bit in byte["bits"]:
                        %if bit is not None:
                uint8_t ${bit.lower()} : 1;
                        %endif
                    %endfor
                    %if byte["bits"].count(None) > 0:
                uint8_t _unused : ${byte["bits"].count(None)};
                    %endif
            } ${byte["name"].lower()};
                %else:
                    %if byte["type"] == "uint16_t":
                        %if byte["name"].lower()[-1] == 'l':
<% continue %>
                        %endif
            union {  // ${byte["description"].replace(" byte high", " bytes low/high")}. Units: ${byte["units"]}
                ${byte["type"]} ${byte["name"].lower()[:-2]};
                struct {
                    uint8_t ${byte["name"].lower()[:-2]}_l;
                    uint8_t ${byte["name"].lower()[:-2]}_h;
                };
            };
                    %else:
            ${byte["type"]} ${byte["name"].lower()};  // ${byte["description"]}. Units: ${byte["units"]}
                    %endif
                %endif
            %endif
        %endfor
        };
    };
} can_${module["name"].lower()}_${topic["name"].lower()}_msg_t;
    %endfor
%endfor
