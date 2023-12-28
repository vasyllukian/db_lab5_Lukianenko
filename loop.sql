DO $$ 
BEGIN
    FOR i IN 1..6 LOOP
        INSERT INTO mental_illness (anxiety, depression, insomnia, ocd, averagescore, mental_illness_id)
        VALUES ('Anxiety' || i, 
                'Depression' || i,
                'Insomnia' || i, 
                'OCD' || i,
                (CAST('Anxiety' || i AS INTEGER) + CAST('Depression' || i AS INTEGER) + CAST('Insomnia' || i AS INTEGER) + CAST('OCD' || i AS INTEGER)) / 4.0 ,
                i);
    END LOOP;
END $$;