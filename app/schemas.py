from typing import Optional
from pydantic import BaseModel,EmailStr, PositiveInt,conint,Field, validator
from datetime import datetime
from typing_extensions import Annotated


class Post(BaseModel):
    title: str
    content: str
    published:bool =True
    

class PostBase(BaseModel):
    
    title: str
    content: str
    published:bool =True


class PostCreate(PostBase):
    pass

class UserOut(BaseModel):
    id:int
    email:EmailStr
    created_at:datetime

    class Config:
        from_attributes = True


class Post(PostBase):
    id:int
    created_at:datetime
    
    owner_id:int
    owner:UserOut

    class Config:
        from_attributes = True
    
class PostOut(BaseModel):
    Post:Post
    votes:int

    class Config:
        from_attributes = True

class UserCreate(BaseModel):
    email:EmailStr
    password:str


class UserLogin(BaseModel):
    email:EmailStr
    password:str


class Token(BaseModel):
    access_token:str
    token_type:str

class TokenData(BaseModel):
    id: Optional[str|int] = None


class Vote(BaseModel):
    post_id:int
    dir:Annotated[int,Field(strict=True,gt=0)]
    #dir: int
    

    




