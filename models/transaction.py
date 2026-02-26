from datetime import datetime, timedelta
from random import randint


class Transaction:
    fine_rate_per_day = 5
    max_loan_days = 30
    
    def __init__(self,transact_id,student_id,book_id):
        self.transact_id = transact_id
        self.student_id = student_id
        self.book_id = book_id
        self.borrow_date= datetime.now().strftime("%Y-%m-%d")
        self.return_date = None
        self.due_date= (datetime.now() + timedelta(days=30)).strftime("%Y-%m-%d")
        self.total_fine=0

        
   

    def status(self):
        if self.return_date is None:
            return "Borrowed"
        else:
            return "Returned"
        
    def calculate_fine(self,return_date):
       
            borrow_date = datetime.strptime(self.borrow_date, "%Y-%m-%d")
            return_date = datetime.strptime(return_date, "%Y-%m-%d")
            days_borrowed = (return_date - borrow_date).days
            if days_borrowed > self.max_loan_days:
                overdue_days = days_borrowed - self.max_loan_days
                fine = overdue_days * self.fine_rate_per_day
                self.total_fine += fine
                return fine
            return 0


    def __str__(self):
        return f"transact_id: {self.transact_id}, student_id: {self.student_id}, book_id: {self.book_id}, borrow_date: {self.borrow_date}, return_date: {self.return_date}, due_date: {self.due_date}, total_fine: {self.total_fine}"