from pydantic import BaseModel, Field
from typing import Optional


class User_Mesage_Chat(BaseModel):
    id: int
    first_name: str
    last_name: Optional[str]=None
    username: str
    type: str

class User_Message_From(BaseModel):
    id: int
    is_bot: bool
    first_name: str
    last_name: Optional[str]=None
    username: str
    language_code: str

class User_Message(BaseModel):
    message_id: int
    from_f: User_Message_From=Field(alias="from")
    chat:User_Mesage_Chat
    date: int
    text: str

class User(BaseModel):
    update_id: int
    message: User_Message
