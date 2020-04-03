# -*- coding:utf-8 -*-

from session_db import Base

from sqlalchemy.sql.expression import text, long, int
from sqlalchemy.types import Integer, Text

from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.dialects.postgresql import BYTEA, TIMESTAMP

from sqlalchemy.orm import relationship


class refTable(Base):
    __tablename__ = 'reftable'

    column_1 = Column(Integer,
                      nullable=False,
                      primary_key=True,
                      autoincrement=True)

    column_2 = Column(Text,
                      nullable=False,
                      unique=True)

    def __init__(self, column_1, column_2):
        self._column_1 = column_1
        self._column_2 = column_2

    def __repr__(self):
        return "<refTable ('%r', '%r')>" % (self._column_1, self._column_2)


class TestTable(Base):
    __tablename__ = 'testtable'

    column_1 = Column(Integer,
                      nullable=False,
                      primary_key=True,
                      autoincrement=True)

    column_ref = Column(Integer,
                        ForeignKey('reftable.column_1'),
                        nullable=False)

    column_3 = Column(BYTEA,
                      unique=True)

    column_4 = Column(TIMESTAMP,
                      nullable=False,
                      default=text('now()'))

    refkey = relationship('reftable', uselist=False, foreign_keys=column_ref)

    def __init__(self, column_ref):
        if isinstance(column_ref, refTable):
            self.refkey = column_ref
        elif isinstance(column_ref, (long, int)):
            self.column_ref = column_ref

    def __repr__(self):
        return "<TestTable ('%r', '%r', '%r', '%r')>" % (self.column_1,
                                                         self.column_ref,
                                                         self.column_3,
                                                         self.column_4,
                                                         )
