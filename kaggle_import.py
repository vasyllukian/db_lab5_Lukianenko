import csv
import psycopg2

username = 'postgres'
password = 'postgres'
database = 'db_lab5_lukianenko'
host = 'localhost'
port = '5432'

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)
print(type(conn))

csv_file_path = r'D:\the work\the work\sem 5\data base\mxmh_survey_results.csv'

current_music_id = 9
current_mental_illness_id = 9

with conn:
    print("Database opened successfully")
    cur = conn.cursor()
    with open(csv_file_path, 'r') as csvfile:
        stop_at_row = 20
        counter = 0

        csvreader = csv.DictReader(csvfile)
        # пропускаємо перші 18 рядків оскільки вони вже додавались в третій лабораторній
        for _ in range(18):
            next(csvreader)
        
        for row in csvreader:
            counter += 1

            anxiety = int(row['Anxiety'])
            depression = int(row['Depression'])
            insomnia = int(row['Insomnia'])
            ocd = int(row['OCD'])
            average_score = (anxiety + depression + insomnia + ocd) / 4 

            cur.execute(
                "INSERT INTO Mental_Illness (Anxiety, Depression, Insomnia, OCD, AverageScore, mental_illness_id) VALUES (%s, %s, %s, %s, %s, %s)",
                (anxiety, depression, insomnia, ocd, average_score, current_mental_illness_id)
            )

            fav_genre = row['Fav genre']
            try:
                bpm = int(row['BPM'])
            except (ValueError, TypeError):
                bpm = None # якщо тими хто проходив опитування не зазначений BPM то поставимо їм BPM 120 тому що це середнє значення bpm у всій музиці
            effects = row['Music effects']

            cur.execute(
                "INSERT INTO Music (Fav_Genre, BPM, Effects, Music_id) VALUES (%s, %s, %s, %s)",
                (fav_genre, bpm, effects, current_music_id)
            )

            person_id = row['Timestamp']
            try:
                age = int(row['Age'])
            except (ValueError, TypeError):
                age = None 
            hours_per_day = float(row['Hours per day'])

            cur.execute(
                "INSERT INTO Person (person_id, age, hours_per_day, Music_id, mental_illness_id) VALUES (%s, %s, %s, %s, %s)",
                (person_id, age, hours_per_day,current_music_id, current_mental_illness_id)
            )

            current_music_id += 1
            current_mental_illness_id += 1

            if counter >= stop_at_row:
                break
conn.close()
