​from wordsets import english_words, english_words_small
from collections import defaultdict

def find_anagrams(letters, words):
    """Find a collection of anagrams of given letters from a given word bank.

    :param letters: The letters from which to form anagrams.
    :param words: A set of lowercase, alphabetic English words in a word bank.
    :return: A set of anagrams of the given letters found in the word bank.
    """
    #### ADD YOUR CODE BELOW ####
    bank = defaultdict(set)
    for word in words:
        canonical = "".join(sorted(word))
        bank[canonical].add(word)
    
    return bank.get("".join(sorted(letters)), set())

    #### ADD YOUR CODE ABOVE ####


if __name__ == '__main__':
    while True:
        letters = input("What letters would you like to find the anagram of? ").lower().strip()
        for anagram in find_anagrams(letters, english_words):
            print(anagram)

