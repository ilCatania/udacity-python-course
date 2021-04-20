"""Reference solutions to each of the pieces of the T9 exercise.

Sure, these are some solutions. They're right here, if you reall need to see them.
"""
import collections
import functools
import operator

from helper import keymap


def parse_content(content):
    """Parse the content of a file into a dictionary mapping words to word"""
    words = {}
    for line in content.split('\n'):
        word, frequency = line.split()
        words[word] = int(frequency)
    return words



def make_tree(words):
    trie = {}
    for word, frequency in words.items():
        node = trie
        for ch in word:
            if ch not in node:
                node[ch] = {}
            node = node[ch]
        node[f'${word}'] = frequency
    return trie

# def node():
#     return collections.defaultdict(node)


# def make_tree(words):
#     trie = node()
#     for word, frequency in words.items():
#         functools.reduce(collections.defaultdict.__getitem__, word, trie)['$'] = (word, frequency)
#     return trie


def predict(tree, numbers):
    leaves = [tree]
    for number in numbers:
        letters = keymap[number]
        leaves = [leaf.get(letter, None) for letter in letters for leaf in leaves]
        while True:
            try:
                leaves.remove(None)
            except ValueError:
                break
    words = {}
    for node in leaves:
        while node:
            letter, child = node.popitem()
            if not isinstance(child, dict):  # We have a word!
                word, frequency = letter[1:], child
                words[word] = frequency
                continue
            leaves.append(child)
    return sorted(words.items(), key=operator.itemgetter(1), reverse=True)

