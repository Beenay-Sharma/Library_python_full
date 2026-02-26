
import mysql.connector


conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password123",
        database="library_management")

def create_tables():

 cursor = conn.cursor()
 cursor.execute("CREATE TABLE IF NOT EXISTS books (book_id INT AUTO_INCREMENT PRIMARY KEY, title VARCHAR(255), author VARCHAR(255), edition INT,available_copies INT, total_copies INT)")
 cursor.execute("CREATE TABLE IF NOT EXISTS students (student_id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), age INT,phonenumber VARCHAR(255), email VARCHAR(255), active_books INT)")
 cursor.execute("CREATE TABLE IF NOT EXISTS transactions (transact_id INT AUTO_INCREMENT PRIMARY KEY, student_id INT, book_id INT, borrow_date DATE NOT NULL, return_date DATE,due_date DATE NOT NULL, total_fine DECIMAL(10, 2), status VARCHAR(255), FOREIGN KEY (student_id) REFERENCES students(student_id), FOREIGN KEY (book_id) REFERENCES books(book_id))")
 conn.commit()
 print("Tables created successfully.")
    
create_tables()