import pymysql
import pandas as pd

conn = pymysql.connect(host='192.168.187.3', port=4567, user='root', db='madang', password='eoaks14', charset='utf8')

cursor = conn.cursor()

cursor.execute('USE madang;') #madang database 사용

work = input("CHOOSE WORK: SEARCH, INSERT, DELETE : ")
if work == "SEARCH":
    sql = "SELECT * from Book;"
    cursor.execute(sql)    
    with conn:
        with conn.cursor() as cur:
            cur.execute(sql)
            result = cur.fetchall()
            for data in result:
                print(data)
    conn.commit()

elif work == "INSERT":
    bookid, bookname, publisher, price = input("bookid, bookname, publisher, price : ").split()
    sql = f"INSERT INTO Book VALUES ('{bookid}','{bookname}','{publisher}','{price}';) "
    cursor.execute(sql)
    conn.commit() 
else:
    cond1 = input("condition1 : ")
    cond2 = input("condition2 : ")
    sql = f"DELETE FROM Book WHERE {cond1} = '{cond2}';"
    cursor.execute(sql)
    conn.commit() 

conn.close()
