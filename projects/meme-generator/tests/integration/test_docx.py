from src.QuoteEngine.ingestor import DocxIngestor
from src.QuoteEngine.ingestor import InvalidFileFormat
from src.QuoteEngine.model import QuoteModel

import pytest


def test_can_ingest():
    assert DocxIngestor.can_ingest("/tmp/x.docx") is True
    assert DocxIngestor.can_ingest("/tmp/y.wav") is False


def test_parse():
    quotes = DocxIngestor.parse("src/_data/DogQuotes/DogQuotesDOCX.docx")
    expected_quotes = [
        QuoteModel("Bark like no one’s listening", "Rex"),
        QuoteModel("RAWRGWAWGGR", "Chewy"),
        QuoteModel("Life is like peanut butter: crunchy", "Peanut"),
        QuoteModel("Channel your inner husky", "Tiny"),
    ]
    assert quotes == expected_quotes
    with pytest.raises(InvalidFileFormat):
        DocxIngestor.parse("/tmp/made_up_file.wav")
