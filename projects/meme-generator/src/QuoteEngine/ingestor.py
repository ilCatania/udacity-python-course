import docx
import os
import pandas as pd
import re
import subprocess
import tempfile
from abc import ABC, abstractmethod
from typing import List

from .model import QuoteModel

quote_regex = re.compile('"([^"]+)" - (.+)')


class InvalidFileFormat(BaseException):
    """Raised when a file with the wrong extension is passed to an ingestor."""
    pass


class IngestorInterface(ABC):
    """Base interface to parse quotes from files."""

    """Supported extension (must include leading dot)."""
    ext = None

    @classmethod
    def can_ingest(cls, path) -> bool:
        """Check whether this ingestor supports the input file."""
        _, ext = os.path.splitext(path)
        return cls.ext == ext

    @classmethod
    def parse(cls, path) -> List[QuoteModel]:
        """Parse the input file, checking whether it's supported first."""
        if not cls.can_ingest(path):
            raise InvalidFileFormat
        return cls._parse(path)


    @classmethod
    @abstractmethod
    def _parse(cls, path) -> List[QuoteModel]:
        """Format-specific parsing logic goes here."""
        raise NotImplemented


class TxtIngestor(IngestorInterface):
    """Parse plain text files."""

    ext = ".txt"

    @classmethod
    def _parse(cls, path) -> List[QuoteModel]:
        """Parsing logic."""
        with open(path, "r", encoding="utf-8-sig") as f:
            return [QuoteModel(*line.strip().split(" - ")) for line in f if " - " in line]


class CsvIngestor(IngestorInterface):
    """Parse comma separated value files using pandas."""

    ext = ".csv"

    @classmethod
    def _parse(cls, path) -> List[QuoteModel]:
        """Parsing logic."""
        return pd.read_csv(path)\
            .apply(lambda row: QuoteModel(row.body, row.author), axis=1)\
            .tolist()


class DocxIngestor(IngestorInterface):
    """Parse Microsoft Word file format using `python-docx`."""

    ext = ".docx"

    @classmethod
    def _parse(cls, path) -> List[QuoteModel]:
        """Parsing logic."""
        doc = docx.Document(path)
        return [QuoteModel(m[1], m[2])
                for p in doc.paragraphs
                for m in quote_regex.finditer(p.text)]

class PdfIngestor(IngestorInterface):
    """Parse PDF files using pdftotext via the command line."""

    ext = ".pdf"

    @classmethod
    def _parse(cls, path) -> List[QuoteModel]:
        """Parsing logic."""
        _, tf = tempfile.mkstemp(suffix=cls.ext)
        try:
            subprocess.run(("pdftotext", path, tf), check=True)
            with open(tf, "r") as tf_handle:
                return [QuoteModel(m[1], m[2])
                        for line in tf_handle
                        for m in quote_regex.finditer(line)]
        finally:
            os.remove(tf)

class Ingestor(IngestorInterface):

    _ingestors = set()

    @classmethod
    def can_ingest(cls, path) -> bool:
        return any(ing.can_ingest(path) for ing in cls._ingestors)

    @classmethod
    def _parse(cls, path) -> List[QuoteModel]:
        for ing in cls._ingestors:  #type: IngestorInterface
            if ing.can_ingest(path):
                return ing.parse(path)
        raise InvalidFileFormat

    @classmethod
    def register(cls, ingestor: IngestorInterface):
        cls._ingestors.add(ingestor)

    @classmethod
    def deregister(cls, ingestor: IngestorInterface):
        cls._ingestors.remove(ingestor)

    @classmethod
    def register_defaults(cls):
        for ing in (CsvIngestor, DocxIngestor, PdfIngestor, TxtIngestor):
            cls.register(ing)