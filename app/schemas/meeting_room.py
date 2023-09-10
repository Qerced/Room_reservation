from typing import Optional

from pydantic import BaseModel, Field, validator


class MeetingRoomBase(BaseModel):
    name: Optional[str] = Field(..., min_length=1, max_length=100)
    description: Optional[str]


class MeetingRoomCreate(MeetingRoomBase):
    name: str = Field(..., min_length=1, max_length=100)


class MeetingRoomUpdate(MeetingRoomBase):

    @validator('name')
    def name_cant_be_null(cls, value: str) -> str:
        if value is None:
            raise ValueError('Имя комнаты не может быть Пустым!')
        return value


class MeetingRoomDb(MeetingRoomCreate):
    id: int

    class Config:
        orm_mode = True
