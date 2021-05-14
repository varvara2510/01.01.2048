#создаем базу данных для хранения лучших попыток (имя игрока и его результат)
import sqlite3   #модуль по работе с базой sqlite

bd = sqlite3.connect("2048.sqlite")  #подключаем нашу базу данных к модулю

cur = bd.cursor()    #cur - курсор, нужен чтобы написать инструкцию для добавления данных в таблицу непосредственно на языке sql(structured query language), с помощью метода execute
cur.execute("""
create table if not exists RECORDS (
    name text,
    score integer
)""")

def insert_result(name, score):
    cur.execute("""
        insert into RECORDS values (?, ?)
    """, (name, score))  #с помощью SQL кода можем сделать так, что знаки вопроса принимают значения name и score соответственно
    bd.commit()   #каждое изменение нужно сохранять в коде, как и в приложении с базой данных

def get_best():   #с помощью этой функции я могу видеть 3 максимальных результата и имена их обладателей в sql редакторе
    cur.execute("""
    SELECT name gamer, max(score) score from RECORDS
    GROUP by name
    ORDER by score DESC
    limit 3
    """)
    return cur.fetchall()

insert_result('QQQ', 777)


