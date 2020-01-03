// CODE GENERATED USING MAKOTEMPLATES.ORG, DO NOT EDIT.
%for tbl in db:
// FILE_VERSION: {db["version"]}

    %for module in db["modules"]:
// ${module["name"]} - ${module["description"]}
#define CAN_SIGNATURE_${module["name"]} ${module["signature"]}
        %for topic in module["topics"]:
// ${topic["name"]} - ${topic["description"]}
#define ${topic["name"]} ${topic["id"]}
            %for i,byte in enumerate(topic["bytes"]):
                %if byte:
#define ${topic["name"]}_${byte["name"]}_BYTE ${i} //<!" ${byte["description"]}
#define ${topic["name"]}_${byte["name"]}_TYPE "${byte["type"]}"
#define ${topic["name"]}_${byte["name"]}_UNITS "${byte["units"]}"
                    %if "bits" in byte.keys():
                        %for k,bit in enumerate(byte["bits"]):
                            %if bit:
#define ${topic["name"]}_${byte["name"]}_${bit}_BIT ${k}
                            %endif
                        %endfor
                    %endif
                %endif
            %endfor
        %endfor
${"\n\n"}
    %endfor
%endfor:
