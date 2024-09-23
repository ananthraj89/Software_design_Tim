from person import Person
import address



class Professor(Person):
    def __init__(self, first, last, dob, phone, address, salary):
        super().__init__(first, last, dob, phone, address)
        self.salary = salary
        self.courses = []
        self.got_raise = False

    def check_for_raise(self):
        if len(self.courses) >= 4 and not self.got_raise:
            self.salary += 20000
            self.got_raise = True

    def add_course(self, course_1):
        from course import Course as c
        if not isinstance(course_1, c.Course):
            raise TypeError("Invalid Course....")
        self.courses.append(course_1)


professor_address_1 = address.Address("USA", "Boston", "MA", "02101")
professor_address_2 = address.Address("India", "Hyderabad","Telangana", "500039")

print(professor_address_1)
print(professor_address_2)

# Create a Professor instance
professor_1 = Professor("Jane", "Smith", "1970-01-01", "123-456-7890", professor_address_1, 80000)
professor_2 = Professor("Ananth", "Ainavolu", "1970-08-23", "+91 9032850347", professor_address_2, 100000)


print(professor_1)
print(professor_2)