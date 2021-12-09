import sqlite3
import time

def getconn():
    conn = sqlite3.connect("c:/pydb/mydb.db")
    return conn



def select_emp():
    # conn = sqlite3.connect("c:/pydb/mydb.db")  # db 연결 객체 생성
    conn = getconn()
    cur = conn.cursor()  # db작업 객체
    sql = "SELECT * FROM employee ORDER BY emp_id"  # db검색
    cur.execute(sql)  # 검색 실행
    rs = cur.fetchall()  # 자료 가져오기
    # print(rs)


    conn.close()  # db 종료


def insert_emp():
    # conn = sqlite3.connect("c:/pydb/mydb.db")  # db 연결 객체생성
    conn = getconn()
    cur = conn.cursor()  # db 작업 객체
    # 입력방법 1 칼럼값을 직접 입력
    # sql = "INSERT INTO employee VALUES ('e1111', '손날두', 30, 500000)" #data추가
    # 방법2
    sql = "INSERT INTO employee VALUES (?, ?, ?, ?)"
    cur.execute(sql, ('e1112', '날강두', 40, 600000))
    conn.commit()  # 커밋 실행 필수
    conn.close()
def select_one(): #특정 자료 검색
    # conn = sqlite3.connect("c:/pydb/mydb.db")
    conn = getconn()
    cur = conn.cursor()
    sql = "SELECT emp_id, name FROM employee WHERE salary=100000"
    cur.execute(sql)
    rs = cur.fetchone()
    print(rs)
    conn.close()

def update_emp(): #자료 수정
    # conn = sqlite3.connect("c:/pydb/mydb.db")
    conn = getconn()
    cur = conn.cursor()
    sql = "UPDATE employee SET age=30 WHERE emp_id=?"
    cur.execute(sql, ('e1112', ))
    conn.commit()
    conn.close()

def delete_emp(): #자료 삭제
    conn = sqlite3.connect("c:/pydb/mydb.db")
    cur = conn.cursor()
    sql = "DELETE FROM employee WHERE name = ?"
    cur.execute(sql, ('승빈', ))
    conn.commit()
    conn.close()

if __name__=="__main--":
    # insert_emp()
    # select_emp()
    # select_one()
    # delete_emp()
    select_emp()