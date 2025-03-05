import csv
import time
from statistics import mean, median
from typing import List, Dict

# Student class
class Student:
    def __init__(self, FirstName: str, LastName: str, email_address: str, Courses_id: str = "", Grades: str = "", marks: float = 0.0):
        self.FirstName = FirstName
        self.LastName = LastName
        self.email_address = email_address
        self.Courses_id = Courses_id
        self.Grades = Grades
        self.marks = marks

    def display_records(self):
        print(f"Name: {self.FirstName} {self.LastName}, Email: {self.email_address}, Course: {self.Courses_id}, Grade: {self.Grades}, Marks: {self.marks}")

    def add_new_student(self, app):  # app is the CheckMyGradeApp instance
        app.students.append(self)
        app.save_data()

    def delete_new_student(self, app):
        app.students = [s for s in app.students if s.email_address != self.email_address]
        app.save_data()

    def check_my_grades(self):
        print(f"Grades for {self.FirstName} {self.LastName}: {self.Grades} (Marks: {self.marks})")

    def update_student_record(self, FirstName=None, LastName=None, email_address=None, Courses_id=None):
        if FirstName: self.FirstName = FirstName
        if LastName: self.LastName = LastName
        if email_address: self.email_address = email_address
        if Courses_id: self.Courses_id = Courses_id

    def update_my_marks(self, marks: float, Grades: str):
        self.marks = marks
        self.Grades = Grades

# Courses class
class Courses:
    def __init__(self, Course_id: str, Credits: int, Course_name: str):
        self.Course_id = Course_id
        self.Credits = Credits
        self.Course_name = Course_name

    def display_courses(self):
        print(f"Course ID: {self.Course_id}, Name: {self.Course_name}, Credits: {self.Credits}")

    def add_new_course(self, app):
        app.courses[self.Course_id] = self
        app.save_data()

    def delete_new_course(self, app):
        if self.Course_id in app.courses:
            del app.courses[self.Course_id]
            app.save_data()

# Professor class
class Professor:
    def __init__(self, Name: str, email_address: str, Rank: str, Course_id: str):
        self.Name = Name
        self.email_address = email_address
        self.Rank = Rank
        self.Course_id = Course_id

    def professors_details(self):
        print(f"Professor: {self.Name}, Email: {self.email_address}, Rank: {self.Rank}, Course ID: {self.Course_id}")

    def add_new_professor(self, app):
        app.professors[self.email_address] = self
        app.save_data()

    def delete_professor(self, app):
        if self.email_address in app.professors:
            del app.professors[self.email_address]
            app.save_data()

    def modify_professor_details(self, Name=None, email_address=None, Rank=None, Course_id=None):
        if Name: self.Name = Name
        if email_address: self.email_address = email_address
        if Rank: self.Rank = Rank
        if Course_id: self.Course_id = Course_id

# Grades class
class Grades:
    def __init__(self, Grade_id: str, Grade: str, Marks_range: str):
        self.Grade_id = Grade_id
        self.Grade = Grade
        self.Marks_range = Marks_range

    def calculate_grade(self, marks: float) -> str:
        if marks >= 90: return "A"
        elif marks >= 80: return "B"
        elif marks >= 70: return "C"
        elif marks >= 60: return "D"
        else: return "F"

    def show_course_details_by_professor(self, app):
        for prof in app.professors.values():
            if prof.Course_id in app.courses:
                print(f"Professor: {prof.Name}, Course: {app.courses[prof.Course_id].Course_name}")

    def display_grade_report(self, app, student_email: str = None, course_id: str = None):
        if student_email:
            for student in app.students:
                if student.email_address == student_email:
                    student.check_my_grades()
                    return
        elif course_id:
            print(f"Grade Report for Course ID: {course_id}")
            for student in app.students:
                if student.Courses_id == course_id:
                    student.check_my_grades()

    def add_grade(self, app, student_email: str, marks: float):
        grade = self.calculate_grade(marks)
        for student in app.students:
            if student.email_address == student_email:
                student.update_my_marks(marks, grade)
                app.save_data()
                return

    def delete_grade(self, app, student_email: str):
        for student in app.students:
            if student.email_address == student_email:
                student.Grades = ""
                student.marks = 0.0
                app.save_data()
                return

    def modify_grade(self, app, student_email: str, marks: float):
        self.add_grade(app, student_email, marks)

# LoginUser class
class LoginUser:
    def __init__(self, Email_id: str, password: str):
        self.Email_id = Email_id
        self.password = self.Encrypt_password(password)  # Store password as encrypted
        self.is_logged_in = False

    def Login(self, app, email: str, password: str):
        if self.Email_id == email and self.decrypt_password(self.password) == password:
            self.is_logged_in = True
            print("Login successful!")
            return True
        print("Invalid credentials!")
        return False

    def Logout(self):
        self.is_logged_in = False
        print("Logged out!")

    def Change_password(self, new_password: str):
        self.password = self.Encrypt_password(new_password)

    def Encrypt_password(self, password: str) -> str:
        cipher = TextSecurity(4)
        return cipher.encrypt(password)

    def decrypt_password(self, password: str) -> str:
        cipher = TextSecurity(4)
        return cipher.decrypt(password)

#textsecurity class
class TextSecurity:
    """This class with encrypt the test using Caesar cipher"""
    def __init__(self, shift):
        """COnstructor."""
        self.shifter=shift
        self.s=self.shifter%26
    def _convert(self, text,s):
        """return encrypted string."""
        result=""
        for i,ch in enumerate(text):
            if (ch.isupper()):
                result += chr((ord(ch) + s-65) % 26 + 65)
            else:
                result += chr((ord(ch) + s-97) % 26 + 97)
        return result
    def encrypt(self, text):
        """return encrypted string."""
        return self._convert(text,self.shifter)
    def decrypt(self, text):
        """return encrypted string."""
        return self._convert(text,26-self.s)

# Main application class
class CheckMyGradeApp:
    def __init__(self):
        self.students: List[Student] = []
        self.courses: Dict[str, Courses] = {}
        self.professors: Dict[str, Professor] = {}
        self.grades = Grades("G001", "", "0-100")
        self.login_user = LoginUser("admin@example.com", "admin123")
        self.load_data()

    def load_data(self):
        try:
            with open('students.csv', 'r') as f:
                reader = csv.reader(f)
                next(reader)
                for row in reader:
                    student = Student(row[0], row[1], row[2], row[3], row[4], float(row[5]))
                    self.students.append(student)
        except FileNotFoundError:
            pass

        try:
            with open('courses.csv', 'r') as f:
                reader = csv.reader(f)
                next(reader)
                for row in reader:
                    self.courses[row[0]] = Courses(row[0], int(row[1]), row[2])
        except FileNotFoundError:
            pass

        try:
            with open('professors.csv', 'r') as f:
                reader = csv.reader(f)
                next(reader)
                for row in reader:
                    self.professors[row[0]] = Professor(row[1], row[0], row[2], row[3])
        except FileNotFoundError:
            pass

    def save_data(self):
        with open('students.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['FirstName', 'LastName', 'email_address', 'Courses_id', 'Grades', 'marks'])
            for student in self.students:
                writer.writerow([student.FirstName, student.LastName, student.email_address, student.Courses_id, student.Grades, student.marks])

        with open('courses.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Course_id', 'Credits', 'Course_name'])
            for course in self.courses.values():
                writer.writerow([course.Course_id, course.Credits, course.Course_name])

        with open('professors.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['email_address', 'Name', 'Rank', 'Course_id'])
            for prof in self.professors.values():
                writer.writerow([prof.email_address, prof.Name, prof.Rank, prof.Course_id])

    # Sorting
    def display_sorted(self, by: str):
        if by == "name":
            sorted_students = sorted(self.students, key=lambda x: f"{x.FirstName} {x.LastName}")
        elif by == "grade":
            sorted_students = sorted(self.students, key=lambda x: x.marks, reverse=True)
        else:
            print("Invalid sort key!")
            return
        for student in sorted_students:
            student.display_records()

    # Searching with timing
    def search_student(self, email: str):
        start_time = time.time()
        for student in self.students:
            if student.email_address == email:
                end_time = time.time()
                print(f"Found: {student.FirstName} {student.LastName}")
                print(f"Search time: {(end_time - start_time) * 1000:.4f} ms")
                return
        end_time = time.time()
        print("Student not found!")
        print(f"Search time: {(end_time - start_time) * 1000:.4f} ms")

    # Statistics
    def course_statistics(self, course_id: str):
        scores = [s.marks for s in self.students if s.Courses_id == course_id and s.marks > 0]
        if not scores:
            print("No scores found for this course!")
            return
        print(f"Course ID: {course_id}")
        print(f"Average Score: {mean(scores):.2f}")
        print(f"Median Score: {median(scores):.2f}")

    # Reports
    def professor_report(self, prof_email: str):
        if prof_email in self.professors:
            prof = self.professors[prof_email]
            prof.professors_details()
            self.grades.show_course_details_by_professor(self)

    def run(self):
        # Login
        email = input("Enter email to login: ")
        password = input("Enter password: ")
        if not self.login_user.Login(self, email, password):
            return

        while True:
            print("\n1. Add Student\n2. Delete Student\n3. Modify Student\n4. Add Course\n5. Delete Course\n6. Add Professor\n7. Delete Professor\n8. Modify Professor\n9. Add Grade\n10. Delete Grade\n11. Sort Data\n12. Search Student\n13. Course Statistics\n14. Student Report\n15. Course Report\n16. Professor Report\n17. Change Password\n18. Logout")
            choice = input("Choose an option: ")

            if choice == "1":
                fname = input("Enter First Name: ")
                lname = input("Enter Last Name: ")
                email = input("Enter email: ")
                student = Student(fname, lname, email)
                student.add_new_student(self)
            elif choice == "2":
                email = input("Enter student email: ")
                for student in self.students:
                    if student.email_address == email:
                        student.delete_new_student(self)
                        break
            elif choice == "3":
                email = input("Enter student email: ")
                fname = input("Enter new First Name (or Enter to skip): ") or None
                lname = input("Enter new Last Name (or Enter to skip): ") or None
                for student in self.students:
                    if student.email_address == email:
                        student.update_student_record(fname, lname)
                        self.save_data()
                        break
            elif choice == "4":
                course_id = input("Enter Course ID: ")
                credits = int(input("Enter Credits: "))
                name = input("Enter Course Name: ")
                course = Courses(course_id, credits, name)
                course.add_new_course(self)
            elif choice == "5":
                course_id = input("Enter Course ID: ")
                if course_id in self.courses:
                    self.courses[course_id].delete_new_course(self)
            elif choice == "6":
                email = input("Enter Professor Email: ")
                name = input("Enter Professor Name: ")
                rank = input("Enter Rank: ")
                course_id = input("Enter Course ID: ")
                prof = Professor(name, email, rank, course_id)
                prof.add_new_professor(self)
            elif choice == "7":
                email = input("Enter Professor Email: ")
                if email in self.professors:
                    self.professors[email].delete_professor(self)
            elif choice == "8":
                email = input("Enter Professor Email: ")
                name = input("Enter new Name (or Enter to skip): ") or None
                rank = input("Enter new Rank (or Enter to skip): ") or None
                for prof in self.professors.values():
                    if prof.email_address == email:
                        prof.modify_professor_details(name, None, rank)
                        self.save_data()
                        break
            elif choice == "9":
                email = input("Enter student email: ")
                course_id = input("Enter Course ID: ")
                marks = float(input("Enter marks: "))
                for student in self.students:
                    if student.email_address == email:
                        student.Courses_id = course_id
                        self.grades.add_grade(self, email, marks)
                        break
            elif choice == "10":
                email = input("Enter student email: ")
                self.grades.delete_grade(self, email)
            elif choice == "11":
                by = input("Sort by (name/grade): ")
                self.display_sorted(by)
            elif choice == "12":
                email = input("Enter student email: ")
                self.search_student(email)
            elif choice == "13":
                course_id = input("Enter Course ID: ")
                self.course_statistics(course_id)
            elif choice == "14":
                email = input("Enter student email: ")
                self.grades.display_grade_report(self, student_email=email)
            elif choice == "15":
                course_id = input("Enter Course ID: ")
                self.grades.display_grade_report(self, course_id=course_id)
            elif choice == "16":
                email = input("Enter professor email: ")
                self.professor_report(email)
            elif choice == "17":
                new_password = input("Enter new password: ")
                self.login_user.Change_password(new_password)
            elif choice == "18":
                self.login_user.Logout()
                print("Goodbye!")
                break
            else:
                print("Invalid option!")

if __name__ == "__main__":
    app = CheckMyGradeApp()
    app.run()
