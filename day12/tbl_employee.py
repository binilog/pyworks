import sqlite3
import time

def select_emp():
    conn = sqlite3.connect("c:/pydb/mydb.db") #db 연결 객체 생성
    cur = conn.cursor() #db작업 객체
    sql = "SELECT * FROM employee" #db검색
    cur.execute(sql) #검색 실행
    rs = cur.fetchall() #자료 가져오기
    # print(rs)
    for i in rs:
        print(i * 1000)
        time.sleep(0.1)
        print("CLOSE\n" * 100)
    conn.close() #db 종료

def insert_emp():
    conn = sqlite3.connect("c:/pydb/mydb.db") #db 연결 객체생성
    cur = conn.cursor() #db 작업 객체
    sql = "INSERT INTO employee VALUES ('e1111', '손날두', 30, 500000)" #data추가
    cur.execute(sql)
    conn.commit() #커밋 실행 필수
    conn.close()
# insert_emp()
select_emp()