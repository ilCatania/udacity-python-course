from src.QuoteEngine.ingestor import DocxIngestor
from src.QuoteEngine.model import QuoteModel


def test_can_ingest():
    assert DocxIngestor.can_ingest("/tmp/x.docx") is True
    assert DocxIngestor.can_ingest("/tmp/y.wav") is False


def test_parse():
    quotes = DocxIngestor.parse("src/_data/DogQuotes/DogQuotesDOCX.docx")
    expected_quotes = [
        QuoteModel("Bark like no one’s listening", "Rex"),
        QuoteModel("RAWRGWAWGGR", "Chewy"),
        QuoteModel("Life is like peanut butter: crunchy", "Peanut"),
<<<<<<< HEAD
        QuoteModel("Channel your inner husky", "Husky"),
    ]
=======
        QuoteModel("Channel your inner husky", "Tiny"),
    ]
    assert quotes == expected_quotes
>>>>>>> add docx parser + integration test
