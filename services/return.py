import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from database import conn


def return_book(book_id):

 cursor = conn.cursor()
 cursor.execute("UPDATE books SET available_copies = available_copies + 1 WHERE book_id=%s",(book_id,))

 conn.commit()
 
 return "Book returned successfully"
