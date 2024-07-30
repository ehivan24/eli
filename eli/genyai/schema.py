from pydantic import BaseModel


class OperatingSystem(BaseModel):
    os: str
