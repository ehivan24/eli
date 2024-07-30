from pydantic import BaseModel, EmailStr


class OperatingSystem(BaseModel):
    os: str
