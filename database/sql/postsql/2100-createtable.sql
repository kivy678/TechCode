CREATE TYPE ename.ename AS ENUM(
    'ENUM1',
    'ENUM2',
    'ENUM3'
);

CREATE TABLE IF NOT EXISTS tname.tname(
    column1     SMALLSERIAL         NOT NULL,
    column2     SMALLINT            DEFAULT NULL
    column3     CHAR(15)            NOT NULL,
    column4     TEXT                NOT NULL,
    column5     BYTEA               NOT NULL,    
    column6     ename.ename         NOT NULL DEFAULT 'ENUM1',
    column7     DATE                NOT NULL DEFAULT CURRENT_DATE,
    column8     TIMESTAMP           NULL,

    PRIMARY KEY(id),
    UNIQUE(ip)

    CONSTRAINT fk_tname_column2 FOREIGN KEY (column2)
        REFERENCES refTname.refTname (refColumn)        -- 참조하는 테이블의 테이블 명과 컬럼 명
    ON DELETE CASCADE
);

CREATE INDEX idx_tname_column2
    ON tname.tname (column2);
