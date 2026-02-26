class Student:
    def __init__(self,student_id,name,age,phonenumber,email,active_books):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.phonenumber = phonenumber
        self.email = email
        self.active_books=active_books

    def __str__(self):
        return f"student_id: {self.student_id}, name: {self.name}, age: {self.age}, phonenumber: {self.phonenumber}, email: {self.email}, active_books: {self.active_books}"
    