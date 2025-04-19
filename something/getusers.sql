CREATE OR REPLACE FUNCTION get_users_paginated(p_limit INT, p_offset INT)
RETURNS TABLE(user_id INT, user_name TEXT, user_phone TEXT)
AS $$
BEGIN
    RETURN QUERY
    SELECT * FROM Users ORDER BY user_id LIMIT p_limit OFFSET p_offset;
END;
$$ LANGUAGE plpgsql;
