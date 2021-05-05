
# Build a set of small words from an explicit tuple of words.
english_words_small = set((
    "open",
    "peon",
    "nope",
    "stone",
    "notes",
    "onset",
    "tones",
    "cone",
    "pots",
    "post",
    "stop",
    "opts",
    "tops",
))


def load_words_from_filename(filename):
    """Load a set of words from a newline-separated file."""
    with open(filename) as infile:
        return set(line.strip().lower() for line in infile)


english_words = load_words_from_filename("words.txt")

