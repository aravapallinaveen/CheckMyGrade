class Student:
    def __init__(self, first_name, last_name, email_address, grade, course_id, marks):
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address
        self.grade = grade
        self.course_id = course_id  
        self.marks = marks

    def display_records(self):
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Email: {self.email_address}")
        print(f"Course ID: {self.course_id}")
        print(f"Grade: {self.grade}")
        print(f"Marks: {self.marks}")

    def update_student_record(self, first_name=None, last_name=None, email_address=None, grade=None, course_id=None, marks=None):
        if first_name:
            self.first_name = first_name
        if last_name:
            self.last_name = last_name
        if email_address:
            self.email_address = email_address
        if grade:
            self.grade = grade
        if course_id:
            self.course_id = course_id
        if marks:
            self.marks = marks

    def update_my_marks(self, new_marks):
         self.marks = new_marks

    def check_my_grades(self):
        return self.grade

class Professor:
    def __init__(self, first_name, last_name, email_address, course_id):
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address
        self.course_id = course_id

    def professors_details(self):
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Email: {self.email_address}")
        print(f"Course ID: {self.course_id}")

    def modify_professor_details(self, first_name=None, last_name=None, email_address=None, course_id=None):
        if first_name:
            self.first_name = first_name
        if last_name:
            self.last_name = last_name
        if email_address:
            self.email_address = email_address
        if course_id:
            self.course_id = course_id

class Course:
    def __init__(self, course_id, credits, course_name):
        self.course_id = course_id
        self.credits = credits
        self.course_name = course_name

    def display_courses(self):
        print(f"Course ID: {self.course_id}")
        print(f"Credits: {self.credits}")
        print(f"Course Name: {self.course_name}")

class Grade:
    def __init__(self, grade_id, grade, marks_range):
        self.grade_id = grade_id
        self.grade = grade
        self.marks_range = marks_range

    def display_grade_report(self):
        print(f"Grade ID: {self.grade_id}")
        print(f"Grade: {self.grade}")
        print(f"Marks Range: {self.marks_range}")

    def add_grade(self, grade, marks_range):
        self.grade = grade
        self.marks_range = marks_range  

    def modify_grade(self, new_grade, new_marks_range):
        self.grade = new_grade
        self.marks_range = new_marks_range

    def delete_grade(self):
        del self.grade
        print("Grade deleted successfully")


class LoginUser:
    def __init__(self, email_id, password):
        self.email_id = email_id
        self.password = password

    def login(self, email_id, password):
        if self.email_id == email_id and self.password == password:
            print("Login successful")
            return True
        else:
            print("Login failed")
            return False

    def change_password(self, new_password):
        self.password = new_password
        print("Password changed successfully")

    def  Logout():
        print("Logged out successfully")
        return True 

    def Encrypt_password():
        # Implement encryption logic here
        pass    

    def Decrypt_password():
    # Implement decryption logic here
        pass    


    class Admin:
        def __init__(self, first_name, last_name, email_address):
            self.first_name = first_name
            self.last_name = last_name
            self.email_address = email_address

        def admin_details(self):
            print(f"Name: {self.first_name} {self.last_name}")
            print(f"Email: {self.email_address}")

        def modify_admin_details(self, first_name=None, last_name=None, email_address=None):
            if first_name:
                self.first_name = first_name
            if last_name:
                self.last_name = last_name
            if email_address:
                self.email_address = email_address