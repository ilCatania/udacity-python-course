from src.QuoteEngine.ingestor import CsvIngestor
from src.QuoteEngine.model import QuoteModel


def test_can_ingest():
    assert CsvIngestor.can_ingest("/tmp/x.csv") is True
    assert CsvIngestor.can_ingest("/tmp/y.wav") is False


def test_parse():
    quotes = CsvIngestor.parse("src/_data/DogQuotes/DogQuotesCSV.csv")
    expected_quotes = [
        QuoteModel("Chase the mailman", "Skittle"),
        QuoteModel("When in doubt, go shoe-shopping", "Mr. Paws"),
    ]
    assert quotes == expected_quotes
