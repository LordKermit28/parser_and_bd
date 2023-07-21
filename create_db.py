import psycopg2

def create_db():
    conn = psycopg2.connect(
        host='localhost',
        database='vacancy',
        user='postgres',
        password='Ps200028')

    cursor = conn.cursor()

    create_table_query = '''CREATE TABLE vacancy
              (id_vacancy serial PRIMARY KEY,
               vacancy varchar(150),
               salary integer,
               company varchar(150),
               description text,
               link varchar(150));'''

    try:
        # Выполнение SQL-запроса
        cursor.execute(create_table_query)
        conn.commit()
        print("Таблица создана успешно!")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        # Закрытие курсора и соединения
        cursor.close()
        conn.close()



create_db()