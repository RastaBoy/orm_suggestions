from contextlib import contextmanager
import os

from sqlalchemy import create_engine, orm
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session



DeclarativeBase = declarative_base()

__CONNSTRING__ = f'sqlite:///{os.path.join(os.getcwd(), "test.db")}?check_same_thread=False'

class Database:

    _engine = create_engine(__CONNSTRING__, echo=False)
    _session_factory = orm.scoped_session(
        orm.sessionmaker(
            autocommit=False,
            autoflush=False,
            bind=_engine
        ),
    )

    @staticmethod
    def create_database():
        # DeclarativeBase.metadata.drop_all(Database._engine)
        DeclarativeBase.metadata.create_all(Database._engine)
    
    @staticmethod
    @contextmanager
    def session():
        session: Session = Database._session_factory()
        try:
            yield session
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()