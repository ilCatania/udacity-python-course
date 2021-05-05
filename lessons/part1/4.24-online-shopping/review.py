"""Implement your Review class in this file!"""

class Review:
    def __init__(self, description: str, user, product):
        self.description = description
        self.user = user
        self.product = product
        
    def __str__(self):
        return f"Review(description: {self.description}, user: {self.user}, product:{self.product})"

