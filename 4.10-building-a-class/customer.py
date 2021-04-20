class Customer:
    
    def __init__(self, first_name: str, last_name: str, tier: tuple = ("free", 0)):
        self.first_name = first_name
        self.last_name = last_name
        self.tier = tier

    @staticmethod
    def premium(first_name: str, last_name: str):
        return Customer(first_name, last_name, ("premium", 10))
    
    @property
    def name(self):
        return f"{self.first_name} {self.last_name}"

    def can_access(self, item: dict) -> bool:
        return self.tier[0] == "premium" or item["tier"] == "free" # hack
    
    def bill_for(self, months: int) -> int:
        return months * self.tier[1]


if __name__ == '__main__':
    # This won't run until you implement the `Customer` class!
    
    marco = Customer('Marco', 'Polo')  # Defaults to the free tier
    print(marco.name)  # Marco Polo
    print(marco.can_access({'tier': 'free', 'title': '1812 Overture'}))  # True
    print(marco.can_access({'tier': 'premium', 'title': 'William Tell Overture'}))  # False

    victoria = Customer.premium("Alexandrina", "Victoria")  # Build a customer around the ('premium', 10$/mo) streaming plan.
    print(victoria.can_access({'tier': 'free', 'title': '1812 Overture'}))  # True
    print(victoria.can_access({'tier': 'premium', 'title': 'William Tell Overture'}))  # True
    print(victoria.bill_for(5))  # => 50 (5 months at 10$/mo)
    print(victoria.name)  # Alexandrina Victoria
