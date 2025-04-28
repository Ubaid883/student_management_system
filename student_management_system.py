import pymysql as sql

conn = sql.connect(host='localhost', user='root',password='',database='Student_management')

cur = conn.cursor()

# Create Table 
cur.execute('''CREATE TABLE IF NOT EXISTS 
            Student(id INTEGER PRIMARY KEY NOT NULL, 
            student_name VARCHAR(255) NOT NULL,
            student_class VARCHAR(255) NOT NULL, 
            student_depart VARCHAR(255) NOT NULL,
            gender VARCHAR(255) NOT NULL, 
            phone_number VARCHAR(255) NOT NULL)''')
