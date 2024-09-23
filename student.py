import person

import address

class Student(person.Person):
    def __init__(self, first, last, dob, phone, address, international = False):
        super().__init__(first, last, dob, phone, address)
        self.international = international
        self.enrolled = []

    def add_enrollment(self, enrollment):
        from enroll import Enroll as e
        if not isinstance(enrollment, e.Enroll):
            raise TypeError("Invalid Enroll.....")
        self.enrolled.append(enrollment)

    def is_on_probation(self):
        return False
    
    def is_part_time(self):
        return len(self.enrolled) <=3
    

address1 = address.Address("123 Main St", "Anytown", "12345","K1L 6N5")

address2 = address.Address("456 Oak St", "Othertown", "67890","P1L 6BJ")

student_1= Student("Alice", "Johnson", "2002-04-10", "321-654-0987", address1)
student_2 = Student("Ananth", "Ainavolu", "1989-08-23", "+1 613-276-7116", address2)

print(student_1)
print(student_2)