import helper
import gold

def parse_content(content):
    rows = (r.split() for r in content.split("\n"))
    return {word: int(freq) for word, freq in rows}

def make_tree(words):
    num_map = {c: n for n, chars in helper.keymap.items() for c in chars}
    tree_root = dict()
    for word, freq in words.items():
        leaf = tree_root
        for c in word:
            n = num_map[c]
            new_leaf = leaf.get(n, {})
            leaf[n] = new_leaf
            leaf = new_leaf
        leaf[ word ] = freq    
    
    return tree_root

def predict(tree, numbers):
    subtree = tree
    for n in numbers:
        subtree = subtree.get(n, {})
    
    nodes = [subtree]
    predictions = []
    for node in nodes:
        for k, v in node.items():
            if k.isdigit():
                nodes.append(v)
            else:
                predictions.append((k, v))
    return sorted(predictions, key=lambda x: -x[1])


if __name__ == '__main__':
    content = helper.read_content(filename='ngrams-10k.txt')

    # When you've finished implementing a part, remove the `gold.` prefix to check your own code.

    # PART 1: Parsing a string into a dictionary.
    words = parse_content(content)

    # PART 2: Building a trie from a collection of words.
    tree = make_tree(words)

    while True:
        # PART 3: Predict words that could follow
        numbers = helper.ask_for_numbers()
        predictions = predict(tree, numbers)

        if not predictions:
            print('No words were found that match those numbers. :(')
        else:
            for prediction, frequency in predictions[:10]:
                print(prediction, frequency)

        response = input('Want to go again? [y/N] ')
        again = response and response[0] in ('y', 'Y')
        if not again:
            break

