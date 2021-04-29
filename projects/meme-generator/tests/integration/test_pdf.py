from src.QuoteEngine.ingestor import PdfIngestor
from src.QuoteEngine.model import QuoteModel


def test_can_ingest():
    assert PdfIngestor.can_ingest("/tmp/x.pdf") is True
    assert PdfIngestor.can_ingest("/tmp/y.wav") is False


def test_parse():
    quotes = PdfIngestor.parse("src/_data/DogQuotes/DogQuotesPDF.pdf")
    expected_quotes = [
        QuoteModel("Treat yo self", "Fluffles"),
        QuoteModel("Life is like a box of treats", "Forrest Pup"),
        QuoteModel("It's the size of the fight in the dog", "Bark Twain"),
    ]
    assert quotes == expected_quotes
