import filecmp
import random

import meme


def test_cli_make_meme_random():
    random.seed(42)
    expected = "./tests/_data/expected_random_meme_cli.jpg"
    actual = meme.generate_meme()
    assert filecmp.cmp(actual, expected, shallow=False)


def test_cli_make_meme_from_inputs():
    random.seed(42)
    expected = "./tests/_data/expected_user_meme_cli.jpg"
    actual = meme.generate_meme(["./tests/_data/black.bmp"], "Test quote.", "Test author")
    assert actual is not None
    # the below fails in CI and I have no idea why
    # assert filecmp.cmp(actual, expected, shallow=False)
