from fastapi import APIRouter , Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select


from models.user import User
from schema.user_schemas import CreateUserDTO,CreateUserResponseDTO
from api.dependencies import get_db


router = APIRouter(prefix="/api/v1/auth", tags=["auth"])

@router.post("/signup",response_model=CreateUserResponseDTO)
async def create_user(user: CreateUserDTO,db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User).where(User.email == user.email))
    existing_user  = result.scalars().first()

    if existing_user:
        raise HTTPException(status_code=400,detail="Email already registered")
    
    new_user = User(username=user.username,email  = user.email,hashed_password=user.password,avatar_url = user.avatar_url)
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)

    return new_user


