from PIL import Image, ImageDraw, ImageFont
from QuoteEngine.model import QuoteModel

import os
import random
import tempfile


class MemeEngine:

    text_margin = 2  # avoid the text sticking too close to the borders

    def __init__(self, root):
        self.root = root
        os.makedirs(root, exist_ok=True)

    def _write_quote(self, img: Image, quote: QuoteModel, font_name: str, font_size: int):
        quote_str = str(quote)
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype(font_name, font_size)

        # try to avoid text going outside the image
        margin = min(type(self).text_margin, img.width, img.height)
        text_width, text_height = draw.textsize(quote_str, font=font)
        text_x = random.randint(margin, max(margin, img.width - text_width - margin))
        text_y = random.randint(margin, max(margin, img.height - text_height - margin))

        draw.text((text_x, text_y), str(quote), font=font)

    def make_meme(self, img_path, text, author, width=500, font_name="FreeSans.ttf", font_size=20) -> str:
        with Image.open(img_path) as img:  # type: Image
            if img.width > width:
                new_height = int(img.height * width / img.width)
                resized = img.resize((width, new_height))
            else:
                resized = img
            self._write_quote(resized, QuoteModel(text, author), font_name, font_size)
            _, tf = tempfile.mkstemp(dir=self.root, prefix="meme-", suffix=".jpg")
            resized.save(tf)
        return tf