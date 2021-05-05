import random
cat_string = "--Whiskers--, --Spot--, --Meowmeow--, --Tiger--, --Kitty--, --Henry--, --Mr.Paws--"
def random_cat(cat_names: str):
    return random.choice([c.strip("--") for c in cat_string.split(", ")])
print(f"{random_cat(cat_string)} is a good kitty.")

