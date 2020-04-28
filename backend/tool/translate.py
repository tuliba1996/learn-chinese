import psycopg2

from google.cloud import translate_v2 as translate
translator = translate.Client()

try:
    connection = psycopg2.connect(user="postgres",
                                  password="12345",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="learn_chinese")

    connection.autocommit = False
    cursor = connection.cursor()
    # postgres_insert_query = """ INSERT INTO api_commonchinese (chinese, pinyin) VALUES (%s,%s)"""
    query_word = """SELECT * FROM api_commonchinese ORDER BY ID;"""
    query_update_word = """UPDATE api_commonchinese SET vietnamese = %s where id= %s;"""
    cursor.execute(query_word)
    words = cursor.fetchall()
    for i in words:
        print(i[1])
        tl = translator.translate(i[1], target_language='vi')
        # sleep(1)
        # print(tl)
        cursor.execute(query_update_word, (tl['translatedText'], i[0]))
        print(str(i[0]) + '\t' + i[1] + '\t>>>\t' + tl['translatedText'])
    # cursor.execute(query_update_word, ('vietnam', 2))
    connection.commit()
    # count = cursor.rowcount
    # print('list_word', words)
    print('insert success')

    # Print PostgreSQL Connection properties
    # sql_check_table = '''select * from information_schema.tables where table_name=api_book;'''
    # test_select = '''SELECT * FROM api_book;'''

    # cursor.execute(test_select)
    # records = cursor.fetchall()
    # connection.commit()
    # print('records', records)
except (Exception, psycopg2.Error) as error:
    print("Error in transction Reverting all other operations of a transction ", error)
    connection.rollback()
finally:
    #closing database connection.

    if (connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
