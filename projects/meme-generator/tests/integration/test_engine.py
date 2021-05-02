from src.MemeGenerator.engine import MemeEngine
from tempfile import TemporaryDirectory
import random
import filecmp


def test_make_meme():
    random.seed(42)
    expected = "./tests/_data/expected.jpg"
    with TemporaryDirectory() as d:
        me = MemeEngine(d)
        actual = me.make_meme("./tests/_data/black.bmp", "Test quote.", "Test author")
        assert filecmp.cmp(actual, expected)

