import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from database import conn


def see_data():

 cursor = conn.cursor()
 cursor.execute("SELECT * FROM students")
 result = cursor.fetchall()
 return result

print(see_data())