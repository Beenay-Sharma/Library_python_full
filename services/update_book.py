import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from database import conn


def add_book(title,author,edition,total_copies):

 cursor = conn.cursor()
 cursor.execute("INSERT INTO books (title,author,edition,available_copies,total_copies) VALUES (%s,%s,%s,%s,%s)",(title,author,edition,total_copies,total_copies))
 
 conn.commit()
 

 
 return "Book added successfully"
def see_books():

 cursor = conn.cursor()
 cursor.execute("SELECT * FROM books")
 result = cursor.fetchall()
 return result


"""  """
def delete_book(book_id):


 cursor = conn.cursor()
 cursor.execute("DELETE FROM books WHERE book_id=%s",(book_id,))




 conn.commit()
 
 return "Book deleted successfully"


def update_book(book_id,title,author,edition):

 cursor = conn.cursor()
 cursor.execute("UPDATE books SET title=%s,author=%s,edition=%s WHERE book_id=%s",(title,author,edition,book_id))

 conn.commit()
 
 return "Book updated successfully"



def restock_book(book_id,additional_copies):

 cursor = conn.cursor()
 cursor.execute("UPDATE books SET available_copies = available_copies + %s,total_copies = total_copies + %s WHERE book_id=%s",(additional_copies,additional_copies,book_id))

 conn.commit()
 
 return "Book restocked successfully"

