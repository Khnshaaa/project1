CREATE OR REPLACE PROCEDURE insert_or_update_user(p_name TEXT, p_phone TEXT)
LANGUAGE plpgsql
AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM Users WHERE user_name = p_name) THEN
        UPDATE Users SET user_phone = p_phone WHERE user_name = p_name;
    ELSE
        INSERT INTO Users(user_name, user_phone) VALUES (p_name, p_phone);
    END IF;
END;
$$;
