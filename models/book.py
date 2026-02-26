
from datetime import datetime



class Book:
    def __init__(self,book_id,title,author,edition,available_copies,total_copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.edition = edition
        self.available_copies = available_copies
        self.total_copies = total_copies   
        

    
    def borrow_book(self):
        
       
        if self.available_copies>0:
            self.available_copies-=1 
              
            return True
            
        else:
            return False    
       

    def return_book(self):
        if self.available_copies < self.total_copies:
            
            self.available_copies+=1
            
            return True
        else:
            return False

    def book_checker(self):
       
        if self.available_copies>0:
               return True
        else:
                return False
        

    def __str__(self):
        return f"book_id: {self.book_id}, title: {self.title}, author: {self.author}, edition: {self.edition}, available_copies: {self.available_copies}"