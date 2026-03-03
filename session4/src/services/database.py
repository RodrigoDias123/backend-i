from pathlib import Path
import json
from data.models import Meeting, MeetingMedata
from uuid import uuid4
from dataclasses import asdict



BASE_PATH = Path("meetings")
INDEX_PATH = Path("meetings/index.json")

def create(meeting: Meeting):
    filename = f"{BASE_PATH}/{uuid4()}.md"
    with open(filename, "w")as file:
        file.writelines(str(meeting))

    
    if not INDEX_PATH.exists():
        INDEX_PATH.touch()
        INDEX_PATH.write_text("[]")

    
    index_content = None
    
    with open(INDEX_PATH.absolute(), "r") as file:
        index_content : list = json.loads(file.read())

    index_content.append(
       asdict(MeetingMedata(
          meeting=meeting,
          path=filename

        ))
    )
    

    with open(INDEX_PATH.absolute(), "w") as file:
        json.dump(index_content, file)
    


    #     index= []
    #     index.append(MeetingMedata(
    #         Meeting=meeting(
    #             title=meeting["meeting"]["title"],
    #             owner=meeting["meeting"]["owner"],
    #             date=meeting["meeting"]["date"],
    #         ),
    #         path=meeting["path"]
    #     ))

    # index_content.append(index)