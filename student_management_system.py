import pymysql as sql

# Make connection with database
conn = sql.connect(host='localhost', user='root',password='',database='Student_management')

cur = conn.cursor()

# Create Table 
cur.execute('''
    CREATE TABLE IF NOT EXISTS Student (
        id INTEGER PRIMARY KEY AUTO_INCREMENT,
        student_name VARCHAR(255) NOT NULL,
        student_class VARCHAR(255) NOT NULL,
        student_depart VARCHAR(255) NOT NULL,
        gender VARCHAR(255) NOT NULL,
        phone_number VARCHAR(255) NOT NULL
    )
''')

def Add_Student(s_name,s_class,s_dep,s_gender, s_pho):
    try:
        cur.execute("INSERT INTO Student (student_name,student_class,student_depart,gender,phone_number) VALUES(%s,%s,%s,%s,%s)",(s_name,s_class,s_dep,s_gender, s_pho))
        conn.commit()
        print("Student Data Add Successfully.")
    except Exception as e:
        print("Student Data not Added", e)
        
def View_Student():
    cur.execute("SELECT * FROM Student")
    for user in cur.fetchall():
        print(user)
        

def Update_Student():
    pass

def Delete_Student():
    pass

# Main Programme
def main():
    while True:
        print("\n Student Management System")
        print("1. Add Student:")
        print("2. View Student:")
        print("3. Update Student:")
        print("4. Delete Student:")
        print("5. Exit:")
        
        
        # User Choice
        choice = input("\n Enter Your Choice(1-5): ")
        
        # Building logic
        match choice:
            case '1':
                 
                 s_name = input("Enter Student Name: ")
                 s_class = input("Enter Student Class: ")
                 s_dept = input("Enter Student Department: ")
                 s_gender = input("Enter Student Gender: ")
                 s_phone = input("Enter Student Phone Number: ")
                 Add_Student(s_name,s_class,s_dept,s_gender,s_phone)
                
            case '2':
                 View_Student()
                
            case '3':
                Update_Student()
                
            case '4':
                Delete_Student()
                
            case '5':
                break
            
            case _:
                print("Invalid Choice. ")
                
        

if __name__ == '__main__':
    main()