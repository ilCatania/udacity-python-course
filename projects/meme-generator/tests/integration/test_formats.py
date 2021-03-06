import pytest
from QuoteEngine.ingestor import (
    CsvIngestor,
    DocxIngestor,
    PdfIngestor,
    TxtIngestor,
    IngestorInterface,
)
from QuoteEngine.model import QuoteModel, InvalidFileFormat

ingestors_to_test = [
    ("csv", CsvIngestor),
    ("docx", DocxIngestor),
    ("pdf", PdfIngestor),
    ("txt", TxtIngestor),
]


@pytest.mark.parametrize("ext,ingestor", ingestors_to_test)
def test_can_ingest(ext: str, ingestor: IngestorInterface):
    assert ingestor.can_ingest(f"/tmp/x.{ext}") is True
    assert ingestor.can_ingest("/tmp/y.wav") is False


@pytest.mark.parametrize("ext,ingestor", ingestors_to_test)
def test_parse(ext: str, ingestor: IngestorInterface):
    quotes = ingestor.parse(f"src/_data/SimpleLines/SimpleLines.{ext}")
    expected_quotes = [QuoteModel(f"Line {n}", f"Author {n}") for n in range(1, 6)]
    assert quotes == expected_quotes
    with pytest.raises(InvalidFileFormat):
        ingestor.parse("/tmp/made_up_file.wav")
