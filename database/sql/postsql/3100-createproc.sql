
-- 배열 반복문 예제
CREATE OR REPLACE FUNCTION public.Proc()
                                IN arg_Val1     TEXT,
                                IN arg_Val2     INT,
                                IN arg_Val3     ename.ename
)RETURNS INT AS $$

DECLARE
    proc_id         BOOLEAN;
    proc_array      CHAR(11)[] := array['String Test', 'String Test2'];
    proc_returnId   SMALLINT := 0;
    
BEGIN
    SELECT INTO proc_id
    EXISTS(
        SELECT id
        FROM public.tname
    );

    IF NOT proc_id THEN
        FOR i in 1..array_length(proc_array, 1) LOOP
            INSERT INTO public.inertTname(stringColumn)
            VALUES(proc_array[i]) RETURNING id INTO proc_returnId;

        END LOOP;
        
        RETURN proc_returnId;


    ELSE
        UPDATE public.updateTname
        SET intColumn = intColumn + 1
        WHERE conditionColumn = arg_Val2
        RETURNING 0 INTO proc_returnId;

    END IF;
        
    RETURN proc_returnId;


END;
$$ LANGUAGE plpgsql;
