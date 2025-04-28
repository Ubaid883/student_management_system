
<h1 align="center">Student Management System (Python + PyMySQL)</h1>

## 👨‍💻 Author
- Developed by **Ubaid**
- linkdlin: www.linkedin.com/in/ubaid-ullah-712152360
- Email: ubaidsaleem811@gmail.com

## 📋 Project Description
This is a simple **command-line Student Management System** built using **Python** and **MySQL** (with PyMySQL connector).
It allows users to perform basic **CRUD operations**:
- Add a new student
- View all students
- Update an existing student's information
- Delete a student record

All operations are performed on a MySQL database named `Student_management`.

## 🛠️ Technologies Used
- Python 3
- MySQL
- PyMySQL library

## Setup Instructions
### 1. Install PyMySQL
Make sure you have PyMySQL installed:

`pip install pymysql`

### 2. MySQL Database Setup

- Start your MySQL server.

- Create a database named Student_management:
    ```bash
    CREATE DATABASE Student_management;

## 🚀 How to Run
1.  Open your terminal (or command prompt).

2.  Make sure your MySQL server is running.

3.  Run the Python script:
    ```bash
    python student_management_system.py

4. Follow the menu options to:
- Add a new student

- View all students

- Update an existing student

- Delete a student

- Exit the program

## 📚 Features
- **Add Student:** Enter student name, class, department, gender, and phone number.

- **View Students:** Display all student records from the database.

- **Update Student:** Modify existing student information based on the student ID.

- **Delete Student:** Remove a student from the database using their ID.

- **Error Handling:** Catches exceptions if database operations fail.

- **Simple Menu System:** Easy to navigate via number choices.

## ❗Important Notes
- The MySQL connection uses default credentials:

    - Host: `localhost`

    - User: `root`

    - Password: (empty)

    - Database: `Student_management`
- You can change these credentials in the code if needed:
    ```bash
    conn = sql.connect(host='localhost', user='root', password='', database='Student_management')

- Make sure the database server is running before starting the program.

## 📌 Future Work
- Input validation (e.g., check if phone number is digits only).

- Better formatting when displaying student data.

- Searching/filtering students.

- GUI interface using Tkinter or PyQt.



