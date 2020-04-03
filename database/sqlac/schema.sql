CREATE TABLE IF NOT EXISTS refTable(
	column_1 			SERIAL 	NOT NULL,	
	column_2 			TEXT 	NOT NULL,

	PRIMARY KEY(column_1),
	UNIQUE(column_2)
);

CREATE TABLE IF NOT EXISTS TestTable(
	column_1			SERIAL 		NOT NULL,
	column_ref 			INT 		NOT NULL,
	column_3			BYTEA 		NULL,
	column_4			TIMESTAMP 	NOT NULL CURRENT_DATE,	
	status				INT 		NOT NULL,

	PRIMARY KEY(id),
	UNIQUE(column_3),

	FOREIGN KEY (column_ref)
		REFERENCES refTable (column_1),
);