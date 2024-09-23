import address
from professor import Professor


class Course:
    def __init__(self, name, code, max_, min_, professor):
        self.name = name
        self.code = code
        self.max = max_
        self.min = min_
        self. professors = []
        self. enrollments= []

        if isinstance(professor,Professor):
            self.professors.append(professor)
        elif isinstance(professor, list):
            for entry in professor:
                if not isinstance(entry, professor):
                    raise TypeError("Invalid Professor....")
            self.professors = professor
        else:
            raise TypeError("Invalid Professor.....")

    def add_professor(self, professor):
        if not isinstance(professor, Professor):
            raise TypeError("Invalid professor....")
        self.professors.append(professor)

    def add_enrollment(self, enroll):
        from enroll import Enroll as el
        if not isinstance(enroll, el.Enroll):
            raise TypeError("Invalid Enroll....")
        if len(self.enrollments) == self.max:
            raise Exception("Cannot enroll, course is completely full....")
        self.enrollments.append(enroll)

    def is_cancelled(self):
        return len(self.enrollments) < self.min
    



professor_address_2 = address.Address("India", "Hyderabad","Telangana", "500039")
professor_2 = Professor("Ananth", "Ainavolu", "1970-08-23", "+91 9032850347", professor_address_2, 100000)
course_1 = Course("Math 101", "MATH101", 30, 5, professor_2)


professor_address_1 = address.Address("USA", "Boston", "MA", "02101")
professor_1 = Professor("Jane", "Smith", "1970-01-01", "123-456-7890", professor_address_1, 80000)
course_2 = Course("History", "102",20, 2, professor_1 )


print(course_1)
print(course_2)




