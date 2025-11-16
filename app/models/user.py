from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.orm import relationship
from app.database import Base
from app.enums import RoleEnum   # ✅ import RoleEnum

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    email = Column(String, unique=True)

    password = Column(String, nullable=False)
    role = Column(Enum(RoleEnum), default=RoleEnum.user)

    
    comments = relationship("Comment", back_populates="user", cascade="all, delete")
