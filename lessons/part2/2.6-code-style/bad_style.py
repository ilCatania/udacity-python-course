import random
import os

catString = ("--Whiskers--, --Spot--, --Meowmeow--, --Tiger--, "
             "--Kitty--, --Henry--, --Mr.Paws--")


def random_cat(string_list):
    cat_list = catString.split(', ')  # split the cats
    cat_list = [cat.strip('--') for cat in cat_list]
    return random.choice(cat_list)


print(f'{random_cat(catString)} is a good kitty')

