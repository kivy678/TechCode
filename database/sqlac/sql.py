# -*- coding: utf-8 -*-
from session_db import Session
from model import refTable, TestTable

try:
    if session.query(refTable, TestTable).join(TestTable)		\
            .filter(TestTable.column_3 == "Test String")		\
            .first() == None:
    else:
        ref = refTable(app, config.LANG)
        test = TestTable(ref, version)

        session.add_all([ref, test])
        session.commit()

except Exception as e:
    print(e)
    session.rollback()
