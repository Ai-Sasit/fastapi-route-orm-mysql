from sqlalchemy import MetaData, Table, Column, Integer, String, ForeignKey
from database.config import engine

meta = MetaData()

User = Table("user", meta,
    Column("id", Integer, primary_key=True),
    Column("Username", String(50), unique=True, nullable=False),
    Column("Password", String(150), nullable=False),
    Column("Email", String(50), unique=True, nullable=False),
    ) 

meta.create_all(engine)          