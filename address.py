

class Address:
    def __init__(self, country, city, state, postal):
        self.country = country
        self.city = city
        self.state = state
        self.postal_code = postal
        
    def __str__(self):
        return f"{self.country}, {self.city} {self.state} {self.postal_code}"
    
    
    
address1 = Address("123 Main St", "Anytown", "12345","K1L 6N5")

address2 = Address("456 Oak St", "Othertown", "67890","P1L 6BJ")

print(address1)
print(address2)