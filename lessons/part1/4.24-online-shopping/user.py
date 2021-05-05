"""Implement your User class in this file!"""
from product import Product
from review import Review

class User:
    def __init__(self, idf: int, name: str):
        self.idf = idf
        self.name = name
        self.reviews = set()
        
    def __str__(self):
        return f"User(idf: {self.idf}, name: {self.name}, reviews: {len(self.reviews)})"
    
    def sell_product(self, product_name: str, product_description: str, product_price: float) -> Product:
        return Product(product_name, product_description, self, product_price)
    
    def buy_product(self, product: Product):
        product.available = False
    
    def write_review(self, review_description: str, product: Product) -> Review:
        r = Review(review_description, self, product)
        self.reviews.add(r)
        product.reviews.add(r)
        return r
    
    
if __name__ == "__main__":
    brianna = User(1, 'Brianna')
    mary = User(2, 'Mary')

    keyboard = brianna.sell_product('Keyboard', 'A nice mechanical keyboard', 100)
    print(keyboard.available)  # => True
    mary.buy_product(keyboard)
    print(keyboard.available)  # => False
    review = mary.write_review('This is the best keyboard ever!', keyboard)
    print(review in mary.reviews)  # => True
    print(review in keyboard.reviews)  # => True
