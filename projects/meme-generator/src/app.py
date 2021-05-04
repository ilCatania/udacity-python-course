import mimetypes
import os
import random
import requests
import tempfile
from flask import Flask, render_template, abort, request
from MemeGenerator.engine import MemeEngine
from QuoteEngine.ingestor import Ingestor
from pathlib import Path


app = Flask(__name__)
static = Path("./static")
meme = MemeEngine("./src/static")  # this is pretty ugly but wouldn't work otherwise


def setup():
    """Load all resources"""

    Ingestor.register_defaults()
    quotes_path = "./src/_data/DogQuotes"
    quotes = []
    for dir, _, files in os.walk(quotes_path):
        for f in files:
            if Ingestor.can_ingest(f):
                quotes.extend(Ingestor.parse(Path(dir) / f))

    images_path = "./src/_data/photos/dog/"
    imgs = [
        Path(dir) / f
        for dir, _, files in os.walk(images_path)
        for f in files
        if f.lower().endswith(".jpg")
    ]
    return quotes, imgs


quotes, imgs = setup()


@app.route("/")
def meme_rand():
    """Generate a random meme"""
    img, quote = (random.choice(item) for item in (imgs, quotes))
    meme_path = meme.make_meme(img, quote.body, quote.author)
    meme_file_name = static / os.path.basename(meme_path)  # assumes memes are saved under ./static/
    return render_template("meme.html", path=meme_file_name)


@app.route("/create", methods=["GET"])
def meme_form():
    """User input for meme information"""
    return render_template("meme_form.html")


@app.route("/create", methods=["POST"])
def meme_post():
    """Create a user defined meme"""

    image_url = request.form.get("image_url")
    body = request.form.get("body")
    author = request.form.get("author")

    response = requests.get(image_url, allow_redirects=True)
    content_type = response.headers["content-type"]
    extension = mimetypes.guess_extension(content_type)
    if not extension:
        raise ValueError(
            f"Unsupported content type: {content_type} for {image_url} (is it an image?)"
        )
    with tempfile.NamedTemporaryFile(suffix=extension) as tf:
        tf.write(response.content)
        meme_path = meme.make_meme(tf.name, body, author)
    meme_file_name = static / os.path.basename(meme_path)  # assumes memes are saved under ./static/
    return render_template("meme.html", path=meme_file_name)


if __name__ == "__main__":
    app.run()
