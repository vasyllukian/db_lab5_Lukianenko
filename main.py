import psycopg2
import matplotlib.pyplot as plt

username = 'postgres'
password = 'postgres'
database = 'db_lab5_lukianenko'
host = 'localhost'
port = '5432'


view_1 = '''
create or replace view deperssion_and_hours_per_day as
select hours_per_day, depression
from person
join mental_illness on person.averagescore = mental_illness.averagescore
order by hours_per_day;
'''
view_2 = '''
create or replace view genres_of_ocd_less_than_5 as
select fav_genre, ocd
from person
join mental_illness on person.averagescore = mental_illness.averagescore
join music on person.music_id = music.music_id
where mental_illness.ocd < 5;
'''
view_3 = '''
create or replace view genres_and_bpm_that_improve_mental_state as
select fav_genre, bpm
from person
join mental_illness on person.averagescore = mental_illness.averagescore
join music on person.music_id = music.music_id
where person.averagescore > 5 and music.effects = 'Improve';
'''


conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)
print(type(conn))


with conn:
    print("Database opened successfully")
    cur = conn.cursor()

    cur.execute(view_1)
    cur.execute(view_2)
    cur.execute(view_3)

    # Розріз 1. Вивести кількість годин прослуховування на день та рівень депресії
    cur.execute("SELECT * FROM deperssion_and_hours_per_day")
    hours_per_day, depression = zip(*cur.fetchall())

    plt.bar(hours_per_day, depression, width=0.3)
    plt.bar(hours_per_day, depression,color = 'red', width=0.3, alpha = 0.3)    
    plt.xlabel('Кількість годин на день')
    plt.ylabel('Рівень депресії')
    plt.title('Кількість годин прослуховування на день та рівень депресії')
    plt.show()

    # Розріз 2. Вивести улюблені жанри тих, у кого рівень тривоги менше 5
    cur.execute("SELECT * FROM genres_of_ocd_less_than_5")
    fav_genres, ocd_values = zip(*cur.fetchall())

    genre_counts = {}
    for genre in fav_genres:
        genre_counts[genre] = genre_counts.get(genre, 0) + 1

    labels = genre_counts.keys()
    sizes = genre_counts.values()

    plt.pie(sizes, autopct='%1.1f%%', startangle=90)
    plt.legend(labels, loc='best')
    plt.title('Улюблені жанри тих, у кого рівень тривоги менше 5')
    plt.show()


    # Розріз 3. Вивести жанри та bpm музики для людей з середнім рівнем психічних захворювань більше 5, яким музика покращує психічний стан
    cur.execute("SELECT * FROM genres_and_bpm_that_improve_mental_state")
    fav_genres, bpm_values = zip(*cur.fetchall())

    plt.scatter(fav_genres, bpm_values)  
    plt.xlabel('Улюблений жанр')
    plt.ylabel('BPM')
    plt.title('Жанри та bpm музики для людей з середнім рівнем психічних захворювань більше 5, яким музика покращує психічний стан')
    plt.show()

conn.close()