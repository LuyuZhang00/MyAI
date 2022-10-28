from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base

# 定义User类
class User(Base):
    __tablename__ = "users" # 定义表名
    # 定义属性
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True)
    hashed_password = Column(String(255))
    is_active = Column(Boolean, default=True)
    items = relationship("Item", back_populates="owner") # 关联Item表

# 定义Item类
class Item(Base):
    __tablename__ = "items"  # 定义表名
    # 定义属性
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), index=True)
    description = Column(String(255), index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="items") # 关联User表