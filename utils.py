from person import Person





class Enroll:
    def __init__(self, student, course):
        if not isinstance(student, Student):
            raise Exception("Invalid Student...")
        
        if not isinstance(course, Course):
            raise Exception("Invalid Course...")
        self.student = student
        self.course = course
        self.date = datetime.now()


    def set_grade(self, grade):
        self.grade = grade


class Student(Person):
    def __init__(self, first, last, dob, phone, address, international = False):
        super().__init__(self, first, last, dob, phone, address)
        self.international = international
        self.enrolled = []

    def add_enrollment(self, enroll):
        if not isinstance(enroll, Enroll):
            raise Exception("Invalid Enroll.....")
        self.enrolled.append(enroll)

    def is_on_probation(self):
        return False
    
    def is_part_time(self):
        return len(self.enrolled) <=3
    