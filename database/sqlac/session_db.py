# -*- coding:utf-8 -*-

from sql_config import DATABASE_CONFIG

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

__version__ = 'v0.1'

URI = '{type}://{user}:{pass}@{host}/{db}'.format( **DATABASE_CONFIG )

engine = create_engine(URI, encoding='utf8',
							client_encoding='utf8',
							use_native_unicode=False,
							convert_unicode=False)

Session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

Base = declarative_base()
Base.query = Session.query_property()


def init_db():
	from pkg_db.model import Package, Download
	Base.metadata.create_all(engine)
	