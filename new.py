from pydantic import Field,BaseModel
from datetime import  datetime
from typing import Optional

class student(BaseModel):
    examName:str=None
    examStartDateTime:datetime=None
    examEndDateTime:datetime=None
    randomQue:Optional [str]=None
    randomAns:Optional [str]=None
    repeatable:Optional[str]=None
    displayResult:str=None
    duration:str=None
    status:str=None
    papercode:Optional[str]=None
    ipAddress:Optional[str]=None
    userId:Optional[str]=None
    no:Optional [str] = Field(None, alias="Schema")
    programId: Optional[str]=None
    programName:Optional [str]=None
    ExamID:str=None
    groups:list=None


    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        schema_extra = {
            "example": {
                    "_id":{"$oid":"60cc3ef0c1c46d92cb6352c7"},
                    "examName":"SR.JEEMAIN_SPLGT-7(19-06-21)N",
                    "examStartDateTime":{"$date":"2021-06-19T07:30:00.000Z"},
                    "examEndDateTime":{"$date":"2021-06-19T14:30:00.000Z"},
                    "randomQue":"1",
                    "randomAns":"0",
                    "repeatable":"0",
                    "displayResult":"1",
                    "duration":"180",
                    "status":"1",
                    "papercode":"210420131126807",
                    "ipAddress":"****",
                    "userId":"11",
                    "schema":"JEEMAINS_2021",
                    "programId":"2",
                    "programName":"JEE MAINS",
                    "ExamID":"24190",
                    "groups":[{"groupName":"AJCKKDMC-ADV","groupID":"250"},{"groupName":"MC-GC-HC-JEEMAINS","groupID":"252"},{"groupName":"MYDEMO","groupID":"262"},{"groupName":"AJCAMP-SR-ACE-19-21","groupID":"263"},{"groupName":"AJCTPG-SR-JEEMAINS-19-21","groupID":"275"},{"groupName":"AJCSKLM-SR-ADV-19-21","groupID":"276"},{"groupName":"AJCRJY-SR-ADV-19-21","groupID":"277"},{"groupName":"AJCELR-SR-JEEMAINS-19-21","groupID":"278"},{"groupName":"AJCELR-SR-ADV-19-21","groupID":"279"},{"groupName":"AJCAMP-SR-ARIJE-19-21","groupID":"283"},{"groupName":"AJCRJY-SR-JEEMAINS-19-21","groupID":"285"},{"groupName":" AJCSKLM-SR-JEEMAINS-19-21","groupID":"286"},{"groupName":"AJCPKL-SR-JEEMAINS-19-21","groupID":"289"},{"groupName":"IIT-SR-ACE-1-2021","groupID":"290"},{"groupName":"IIT-SR-ACE-2-2021","groupID":"291"},{"groupName":"IIT-SR-APT-1-2021","groupID":"292"},{"groupName":"IIT-SR-APT-2-2021","groupID":"293"},{"groupName":"AJCNSP-SR-ARIJE-19-21","groupID":"298"},{"groupName":"AJCBVM-SR-ARIJE-19-21","groupID":"300"},{"groupName":"AJCBVM-SR-ACE-19-21","groupID":"311"},{"groupName":"AJCMDP-ARIJE-19-21","groupID":"321"}]}
            }
        

