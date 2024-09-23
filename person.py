from address import Address

class Person:
    def __init__(self, first, last, dob, phone, address):
        self.first_name = first
        self.last_name = last
        self.date_of_birth = dob
        self.phone = phone
        self.addresses = []

        if isinstance(address, Address):
            self.addresses.append(address)
        elif isinstance(address, list):
            for entry in address:
                if not isinstance(entry, Address):
                    raise TypeError ("Invalid Address...")
                self.addresses = address
        else:
           raise  TypeError("Invalid Address...")
    
    def add_address(self, address):
        if not isinstance(address, Address):
            raise TypeError("Invalid Address......")
        self.addresses.append(address)
        
    def __str__(self):
        addresses_str = '\n'.join(str(address) for address in self.addresses)
        return (f"First Name: {self.first_name}\n"
                f"Last Name: {self.last_name}\n"
                f"Date of Birth: {self.date_of_birth}\n"
                f"Phone: {self.phone}\n"
                f"Addresses:\n{addresses_str}")
    
    

# Create some Address instances
address1 = Address("123 Main St", "Anytown", "12345","K1L 6N5")

address2 = Address("456 Oak St", "Othertown", "67890","P1L 6BJ")

  # Create an instance of Person with a single address
person1 = Person("John", "Doe", "1990-01-01", "123-456-7890", address1)
print(person1)
print("-----------------------")
# Create an instance of Person with multiple addresses
person2 = Person("Jane", "Smith", "1985-05-15", "098-765-4321", [address1, address2])
print(person2)



