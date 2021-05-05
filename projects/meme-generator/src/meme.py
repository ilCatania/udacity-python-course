"""Command line meme generator module."""
import argparse
import random
import tempfile
from pathlib import Path

from MemeGenerator.engine import MemeEngine
from QuoteEngine.ingestor import Ingestor
from QuoteEngine.model import QuoteModel

current_dir = Path(__file__).parent


def generate_meme(path=None, body=None, author=None):
    """Generate a meme given an path and a quote."""
    img = None
    quote = None

    if path is None:
        imgs = MemeEngine.find_images(current_dir / "_data/photos/dog/")
        img = random.choice(imgs)
    else:
        img = path[0]

    if body is None:
        Ingestor.register_defaults()
        quotes = Ingestor.scan(current_dir / "_data/DogQuotes")
        quote = random.choice(quotes)
    else:
        if author is None:
            raise Exception("Author Required if Body is Used")
        quote = QuoteModel(body, author)

    meme = MemeEngine(tempfile.mkdtemp(prefix="memes-"))
    path = meme.make_meme(img, quote.body, quote.author)
    return path


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Create a meme.")
    parser.add_argument("--path", type=Path, help="Path to an image to use.")
    parser.add_argument("--body", help="Some quote text.")
    parser.add_argument("--author", help="The quote's author.")
    args = parser.parse_args()
    print(generate_meme(args.path, args.body, args.author))
