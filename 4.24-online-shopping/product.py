"""Implement your Product class in this file!"""

class Product:
    def __init__(self, name: str, description: str, seller, price: float, available: bool = True, reviews: set = set()):
        self.name = name
        self.description = description
        self.seller = seller
        self.price = price
        self.available = available
        self.reviews = set(reviews)
        
    def __str__(self):
        return f"Product(name: {self.name}, description: {self.description}, seller: {self.seller}, reviews: {len(self.reviews)}, price: {self.price}, available: {self.available})"
    
