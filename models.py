from database import Base   
from sqlalchemy import Column,Integer,String,Boolean,Date,DateTime,ForeignKey
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text


class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True,nullable=False)
    title = Column(String,nullable=False)
    content = Column(String,nullable=False)
    published = Column(Boolean,server_default = 'TRUE',nullable = False)
    created_at = Column(TIMESTAMP(timezone = True),nullable=False,
                        server_default=text('now()'))
    salary = Column(Integer,nullable=False)
    emprequest = Column(String,nullable=False)

    owner_id= Column(Integer,ForeignKey("users.id",ondelete="CASCADE"),nullable=False)
    username = Column(String,nullable=False)
    category_id = Column(Integer, nullable=False)


class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True,nullable=False)
    name = Column(String,nullable=False)
    last_name = Column(String,nullable=False)
    number = Column(String,nullable=False)
    email = Column(String,nullable=False,unique=True)
    password = Column(String,nullable=False)
    created_at = Column(TIMESTAMP(timezone = True),nullable=False,
                        server_default=text('now()'))
    
