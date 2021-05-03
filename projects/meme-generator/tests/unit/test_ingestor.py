from QuoteEngine.ingestor import Ingestor
from QuoteEngine.ingestor import InvalidFileFormat
from QuoteEngine.model import QuoteModel
from typing import List

import pytest


class FakeIngestor:
    """Duck-typed fake ingestor for testing."""

    def __init__(self, ext: str):
        self.ext = ext

    def can_ingest(self, path) -> bool:
        return path.endswith(self.ext)

    def parse(self, path) -> List[QuoteModel]:
        return [QuoteModel(f"Fake {self.ext} quote", self.ext)]


@pytest.fixture(autouse=True)
def setup_ingestor():
    test_extensions = [".py", ".ini"]
    ingestors = [FakeIngestor(ext) for ext in test_extensions]
    for ing in ingestors:
        Ingestor.register(ing)
    yield
    for ing in ingestors:
        Ingestor.deregister(ing)


def test_can_ingest():
    assert Ingestor.can_ingest("/tmp/x.py") is True
    assert Ingestor.can_ingest("/tmp/y.wav") is False


def test_parse():
    quotes = Ingestor.parse("/tmp/made_up_file.py")
    expected_quotes = [QuoteModel("Fake .py quote", ".py")]
    assert quotes == expected_quotes
    quotes = Ingestor.parse("/tmp/made_up_file.ini")
    expected_quotes = [QuoteModel("Fake .ini quote", ".ini")]
    assert quotes == expected_quotes
    with pytest.raises(InvalidFileFormat):
        Ingestor.parse("/tmp/made_up_file.wav")
