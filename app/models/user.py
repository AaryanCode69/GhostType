from  core.database import Base
from sqlalchemy import Column,DateTime,String,UUID,Boolean
from sqlalchemy.sql import func
import uuid

class BaseClass:
    id = Column(String,primary_key= True,index= True,default=lambda: str(uuid.uuid4()))
    created_at = Column(DateTime(timezone=True),server_default=func.now())
    updated_at = Column(DateTime(timezone=True),server_default=func.now(),onupdate=func.now())


class User(Base,BaseClass):
    __tablename__ = "users"
    
    email = Column(String,index=True,nullable=False,unique=True)
    hashed_password = Column(String,nullable=False)
    username = Column(String,index= True,nullable= False,unique=True)
    avatar_url = Column(String,nullable= True)
    is_active = Column(Boolean,default= True)
    is_superuser = Column(Boolean,default=False)