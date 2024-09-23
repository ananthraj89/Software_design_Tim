
from datetime import datetime
import course
import professor
import address
import student

class Enroll:
    def __init__(self, students, course_):
        import student as s1
        if not isinstance(students, s1.Student):
            raise Exception("Invalid Student...")
        
        import course as c
        if not isinstance(course_, c.Course):
            raise Exception("Invalid Course...")
        self.students = students
        self.course_ = course_
        self.date = datetime.now()

    
    def set_grade(self, grade):
        self.grade = grade
   
    
    def __str__(self):
         return f"Grade: {getattr(self, 'grade', 'Not assigned')}"




el = Enroll(students=student.student_1, course_=course.course_2)
student_1= student.Student("Alice", "Johnson", "2002-04-10", "321-654-0987", address.address1)
course_2 = course.Course("History", "102",20, 2, professor.professor_1 )

#print enrollment details 
print(f"Student: {el.students.first_name} {el.students.last_name}")
print(f"Course: {el.course_.name}")
print(f"Enrollment Date: {el.date.now()}")