import pymysql

def connect():
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        db='cisstudent'
    )

    cur = conn.cursor()

    cur.execute('SELECT * FROM students')
    out = cur.fetchall()

    for i in out:
        print(i)

    conn.close()

if __name__ == "__main__":
    connect()