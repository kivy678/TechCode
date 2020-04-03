-- 현재 연결되어 있는 컨넥션들 강제 종료
DO $$
DECLARE
    db_name     CHAR(10) := 'DATABASE_NAME';
    d_name      BOOLEAN;
    p_id        INT;
BEGIN
    SELECT INTO d_name 
    EXISTS(
        SELECT datname
        FROM pg_database
        WHERE datname = db_name
    );
    
    IF d_name THEN
        FOR p_id IN SELECT pid FROM pg_stat_activity WHERE datname = db_name
        LOOP
            RAISE NOTICE 'pid: %', p_id;
            PERFORM pg_terminate_backend(p_id);
        END LOOP;
    END IF;

END;
$$ LANGUAGE plpgsql;


-- 데이터 베이스 생성
DROP DATABASE IF EXISTS DATABASE_NAME;
CREATE DATABASE DATABASE_NAME OWNER OWNER_NAME;
