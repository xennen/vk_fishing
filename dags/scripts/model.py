from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class Members(BaseModel):
    user_id_vk: int
    fullname: str
    last_seen: Optional[datetime] = None
    contacts: str
    friends_count: int
    town: str
    age: Optional[int]
