drop table tname;

CREATE TABLE IF NOT EXISTS tname (
    column1          BIGINT,
    column2          INT,
    column3          VARCHAR,
    column4          TEXT,
    column5          FLOAT,
    column6          ASCII,
    column7          LIST<VARCHAR>,
    column8          LIST<TEXT>,
    column9          TIMESTAMP,
    column10         TIMEUUID,
    column11         DATE,

    PRIMARY KEY (column1, column2)
) WITH comment='tname Test';

CREATE INDEX IF NOT EXISTS idx_tname_column2 ON tname (column2);
