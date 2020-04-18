import xlrd
import psycopg2

loc = ('/Volumes/Pro/pro_test/learn-chinese/backend/tool/common.xlsx')
list_word = []
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
sheet.cell_value(0, 0)
#
# for i in range(sheet.nrows - 2990):
#     chinese = sheet.cell_value(i, 0)
#     pinyin = sheet.cell_value(i, 7)
#     data = {
#         'chinese': chinese,
#         'pinyin': pinyin
#     }
#     list_word.append(data)
# print('list', list_word)


try:
    connection = psycopg2.connect(user="postgres",
                                  password="12345",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="learn_chinese")

    connection.autocommit = False
    cursor = connection.cursor()
    postgres_insert_query = """ INSERT INTO api_commonchinese (chinese, pinyin) VALUES (%s,%s)"""
    for i in range(sheet.nrows):
        chinese = sheet.cell_value(i, 0)
        pinyin = sheet.cell_value(i, 7)
        record_to_insert = (chinese, pinyin)
        cursor.execute(postgres_insert_query, record_to_insert)

    connection.commit()
    count = cursor.rowcount
    print(count, "Record inserted successfully into common table")


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
# finally:
    #closing database connection.

    if (connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")



