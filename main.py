import psycopg2
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

username = 'postgres'
password = 'postgres'
database = 'db_lab5_lukianenko'
host = 'localhost'
port = '5432'


view_1 = '''
create or replace view deperssion_and_hours_per_day as
select hours_per_day, depression 
from person 
join mental_illness on person.mental_illness_id = mental_illness.mental_illness_id
order by hours_per_day;
'''
view_2 = '''
create or replace view genres_of_ocd_less_than_5 as
select fav_genre, ocd
from person
join mental_illness on person.mental_illness_id = mental_illness.mental_illness_id
join music on person.music_id = music.music_id
where mental_illness.ocd < 5;
'''
view_3 = '''
create or replace view genres_and_bpm_that_improve_mental_state as
select fav_genre, bpm
from person 
join mental_illness on person.mental_illness_id = mental_illness.mental_illness_id
join music on person.music_id = music.music_id
where mental_illness.averagescore > 5 and music.effects = 'Improve'
'''

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)
print(type(conn))


with conn:
    print("Database opened successfully")
    cur = conn.cursor()

    cur.execute(view_1)
    cur.execute(view_2)
    cur.execute(view_3)

    fig = plt.figure(figsize=(16, 9))
    gs = GridSpec(1, 3)

    # Розріз 1: Кількість годин прослуховування на день та рівень депресії
    ax1 = fig.add_subplot(gs[0, 0])
    cur.execute("SELECT * FROM deperssion_and_hours_per_day")
    hours_per_day, depression = zip(*cur.fetchall())
    plt.bar(hours_per_day, depression, width=0.3)
    plt.bar(hours_per_day, depression,color = 'red', width=0.3, alpha = 0.3) 
    ax1.set_xlabel('Кількість годин на день')
    ax1.set_ylabel('Рівень депресії')
    ax1.set_title('Кількість годин прослуховування на день та рівень депресії')

    # Розріз 2: Улюблені жанри тих, у кого рівень тривоги менше 5
    ax2 = fig.add_subplot(gs[0, 1])
    cur.execute("SELECT * FROM genres_of_ocd_less_than_5")
    fav_genres, ocd_values = zip(*cur.fetchall())
    genre_counts = {}
    for genre in fav_genres:
        genre_counts[genre] = genre_counts.get(genre, 0) + 1
    labels = genre_counts.keys()
    sizes = genre_counts.values()
    ax2.pie(sizes, autopct='%1.1f%%', startangle=90)
    ax2.legend(labels)
    ax2.set_title('Улюблені жанри тих, у кого рівень тривоги менше 5')

    # Розріз 3: Жанри та bpm музики для людей з середнім рівнем психічних захворювань більше 5, яким музика покращує психічний стан
    ax3 = fig.add_subplot(gs[0, 2])
    cur.execute("SELECT * FROM genres_and_bpm_that_improve_mental_state")
    fav_genres, bpm_values = zip(*cur.fetchall())
    plt.scatter(fav_genres, bpm_values)  
    plt.xticks(fav_genres, ha='left', va='bottom') 
    ax3.set_xlabel('Улюблений жанр')
    ax3.set_ylabel('BPM')
    ax3.set_title('Жанри та bpm музики для людей з середнім рівнем психічних \n захворювань більше 5, яким музика покращує психічний стан')
    plt.savefig('new_graphs.png')
    plt.show()

conn.close()
