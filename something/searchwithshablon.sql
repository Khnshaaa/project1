CREATE OR REPLACE FUNCTION search_by_pattern(pattern TEXT)
RETURNS TABLE(user_id INT, user_name TEXT, user_phone TEXT)
AS $$
BEGIN
    RETURN QUERY
    SELECT * FROM Users
    WHERE user_name ILIKE '%' || pattern || '%' OR user_phone LIKE '%' || pattern || '%';
END;
$$ LANGUAGE plpgsql;
