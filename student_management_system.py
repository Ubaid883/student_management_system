import pymysql as sql

# Make connection with database
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

def Add_Student():
    pass

def View_Student():
    pass

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
        print("5. Delete Student:")
        
        
        # User Choice
        choice = input("Enter Your Choice(1-5)")
        
        # Building logic
        match choice:
            case '1':
                 Add_Student()
                
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