CREATE TABLE IF NOT EXISTS db.tname (
  column1     BIGINT UNSIGNED     NOT NULL AUTO_INCREMENT,
  column2     TINYINT UNSIGNED    DEFAULT NULL,
  column3     CHAR(32)            NOT NULL,
  column4     VARCHAR(5)          NOT NULL,
  column5     TINYTEXT            NOT NULL,
  column6     DATETIME            NOT NULL DEFAULT CURRENT_TIMESTAMP(), -- CURRENT_DATE --date(subdate(now(), INTERVAL 0 DAY))
  column7     ENUM('Y','N')       NOT NULL DEFAULT 'N',  

  PRIMARY KEY (column1),
  UNIQUE KEY (column2),

  CONSTRAINT fk_tname_column2 FOREIGN KEY(column2) 
    REFERENCES db.refTname(refColumn)         -- 참조하는 테이블의 테이블 명과 컬럼 명
  ON DELETE SET NULL ON UPDATE CASCADE
  
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE INDEX indx_column2 ON db.tname ( column2 );
