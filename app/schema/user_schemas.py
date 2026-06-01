from pydantic import BaseModel,ConfigDict


class CreateUserDTO(BaseModel):
    email: str
    username: str
    password: str
    avatar_url: str | None

class CreateUserResponseDTO(BaseModel):
    id: str
    email: str
    username: str
    avatar_url: str | None
    is_active: bool
    
    model_config = ConfigDict(from_attributes=True)