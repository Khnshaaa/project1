CREATE OR REPLACE FUNCTION insert_many_users(names TEXT[], phones TEXT[])
RETURNS TEXT[] AS $$
DECLARE
    i INT;
    bad_entries TEXT[] := '{}';
    clean_phone TEXT;
BEGIN
    FOR i IN 1..array_length(names, 1) LOOP
        -- Пропуск, если имя пустое или слишком длинное
        IF names[i] IS NULL OR char_length(names[i]) > 50 THEN
            bad_entries := array_append(bad_entries, '❌ Неверное имя: ' || coalesce(names[i], 'NULL'));
            CONTINUE;
        END IF;

        clean_phone := phones[i];

        -- Если номер состоит из 10 цифр и не начинается с +, добавляем +7
        IF clean_phone ~ '^\\d{10}$' THEN
            clean_phone := '+7' || clean_phone;
        END IF;

        -- Проверка телефона по шаблону
        IF clean_phone ~ '^\\+?\\d{6,15}$' THEN
            CALL insert_or_update_user(names[i], clean_phone);
        ELSE
            bad_entries := array_append(bad_entries, '❌ Неверный номер: ' || names[i] || ' - ' || phones[i]);
        END IF;
    END LOOP;

    RETURN bad_entries;
END;
$$ LANGUAGE plpgsql;
