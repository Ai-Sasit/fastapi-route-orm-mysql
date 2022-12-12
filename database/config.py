import sqlalchemy as _sql
import sqlalchemy.orm as _orm

DATABASE_URL = "mysql://root:password@localhost/db"

engine = _sql.create_engine(DATABASE_URL)

SessionLocal = _orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)

conn = engine.connect()