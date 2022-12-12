from typing import Optional
from pydantic import BaseModel

class UserSchema (BaseModel):
    username: str
    email: str
    password: str

    class Config:
        orm_mode = True

class UserTokenData(BaseModel):
    username: Optional[str] = None
    email: Optional[str] = None

class UserToken(BaseModel):
    access_token: str
    token_type: str