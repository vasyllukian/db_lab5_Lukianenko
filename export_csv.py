import psycopg2

username = 'postgres'
password = 'postgres'
database = 'db_lab5_lukianenko'
host = 'localhost'
port = '5432'


def main():
    connection = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)

    with connection.cursor() as cursor:
        for table in ('Music', 'Mental_Illness', 'Person'):
            query = f'COPY (SELECT * FROM {table}) TO STDOUT WITH CSV HEADER'
            with open(f'{table}.csv', 'w') as file:
                cursor.copy_expert(query, file)


if __name__ == '__main__':
    main()