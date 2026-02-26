import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from database import conn


def add_student(name,age,email,phonenumber):

 cursor = conn.cursor()
 cursor.execute("INSERT INTO students (name,age,email,phonenumber,active_books) VALUES (%s,%s,%s,%s,%s)",(name,age,email,phonenumber,0))

 conn.commit()
 
 return "Student added successfully"



def delete_student(student_id):

 cursor = conn.cursor()
 cursor.execute("DELETE FROM students WHERE student_id=%s",(student_id,))

 conn.commit()
 
 return "Student deleted successfully"


def update_student(student_id,name,age,email,phonenumber):

 cursor = conn.cursor()
 cursor.execute("UPDATE students SET name=%s,age=%s,email=%s,phonenumber=%s WHERE student_id=%s",(name,age,email,phonenumber,student_id))

 conn.commit()
 
 return "Student updated successfully"