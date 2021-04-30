from src.QuoteEngine.ingestor import InvalidFileFormat
from src.QuoteEngine.ingestor import TxtIngestor
from src.QuoteEngine.model import QuoteModel

import pytest


def test_can_ingest():
    assert TxtIngestor.can_ingest("/tmp/x.txt") is True
    assert TxtIngestor.can_ingest("/tmp/y.wav") is False


def test_parse():
    quotes = TxtIngestor.parse("src/_data/DogQuotes/DogQuotesTXT.txt")
    expected_quotes = [
        QuoteModel("To bork or not to bork", "Bork"),
        QuoteModel("He who smelt it...", "Stinky"),
    ]
    assert quotes == expected_quotes
    with pytest.raises(InvalidFileFormat):
        TxtIngestor.parse("/tmp/made_up_file.wav")
