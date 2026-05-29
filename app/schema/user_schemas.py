from pydantic import BaseModel


class CreateUserDTO(BaseModel):
    email: str
    username: str
    password: str
    avatar_url: str | None

class CreateUserResponseDTO(BaseModel):
    id: str
    emai: str
    username: str
    avatar_url: str | None
    is_active: bool