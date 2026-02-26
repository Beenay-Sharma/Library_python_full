import sys
import os
from models import Transaction
from models import Book
from datetime import datetime, timedelta 
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from database import conn

def see_all_transactions():

 cursor = conn.cursor()
 cursor.execute("SELECT * FROM transactions")
 result = cursor.fetchall()
 return result


def see_students_transactions(student_id):

 cursor = conn.cursor()
 cursor.execute("SELECT * FROM transactions WHERE student_id=%s",(student_id,))
 result = cursor.fetchall()
 return result


def borrow_book(student_id,book_id):

 cursor = conn.cursor()
 cursor.execute("INSERT INTO transactions (student_id,book_id,borrow_date,due_date,status) VALUES (%s,%s,%s,%s,%s)",(student_id,book_id,datetime.now().strftime('%Y-%m-%d %H:%M:%S'),(datetime.now() + timedelta(days=14)).strftime('%Y-%m-%d %H:%M:%S'),'borrowed'))
 cursor.execute("UPDATE books SET available_copies = available_copies - 1 WHERE book_id=%s",(book_id,))
 conn.commit()
 return "Book borrowed successfully"

def return_book(transaction_id):
    cursor = conn.cursor()
    
    
    cursor.execute("SELECT book_id, due_date FROM transactions WHERE transact_id=%s", (transaction_id,))
    row = cursor.fetchone()
    book_id = row[0]
    due_date = row[1]
    
    
    return_date = datetime.now().date()
    fine = 0
    if return_date > due_date:
        overdue_days = (return_date - due_date).days
        fine = overdue_days * 5  
    
    
    cursor.execute("UPDATE transactions SET return_date=%s,status=%s,total_fine=%s WHERE transact_id=%s",(datetime.now().strftime('%Y-%m-%d %H:%M:%S'),'returned',fine,transaction_id))
    
   
    cursor.execute("UPDATE books SET available_copies = available_copies + 1 WHERE book_id=%s",(book_id,))
    conn.commit()
    return "Book returned successfully"