CREATE OR REPLACE PROCEDURE insert_many_users(names TEXT[], phones TEXT[])
LANGUAGE plpgsql
AS $$
DECLARE
    i INT;
    incorrect TEXT[] := ARRAY[]::TEXT[];
BEGIN
    FOR i IN 1..array_length(names, 1) LOOP
        IF phones[i] ~ '^\+?\d{10,15}$' THEN
            CALL insert_or_update_user(names[i], phones[i]);
        ELSE
            incorrect := array_append(incorrect, names[i] || ' - ' || phones[i]);
        END IF;
    END LOOP;

    RAISE NOTICE 'Incorrect data: %', incorrect;
END;
$$;


CREATE OR REPLACE FUNCTION/PROCEDURE имя(...) 
RETURNS ... AS $$
DECLARE
  -- тут твои переменные
BEGIN
  -- тут твои действия
END;
$$ LANGUAGE plpgsql;
