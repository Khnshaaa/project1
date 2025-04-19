CREATE OR REPLACE PROCEDURE delete_by_name_or_phone(p_val TEXT)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM Users WHERE user_name = p_val OR user_phone = p_val;
END;
$$;
