import docx
import os
import re
import subprocess
import tempfile
from abc import ABC, abstractmethod
from typing import List

from .model import QuoteModel

quote_regex = re.compile('"([^"]+)" - (.+)')


class InvalidFileFormat(BaseException):
    """Raise when a file with the wrong extension is passed to an ingestor."""
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
    @abstractmethod
    def parse(cls, path) -> List[QuoteModel]:
        """Parse the input file."""
        raise NotImplemented


class TxtIngestor(IngestorInterface):
    """Parse plain text files."""

    ext = ".txt"

    @classmethod
    def parse(cls, path) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise InvalidFileFormat
        with open(path, "r", encoding="utf-8-sig") as f:
            return [QuoteModel(*line.strip().split(" - ")) for line in f if " - " in line]


class DocxIngestor(IngestorInterface):
    """Parse Microsoft Word file format using `python-docx`."""

    ext = ".docx"

    @classmethod
    def parse(cls, path) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise InvalidFileFormat
        doc = docx.Document(path)
        return [QuoteModel(m[1], m[2])
                for p in doc.paragraphs
                for m in quote_regex.finditer(p.text)]

class PdfIngestor(IngestorInterface):
    """Parse PDF files using pdftotext via the command line."""

    ext = ".pdf"

    @classmethod
    def parse(cls, path) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise InvalidFileFormat

        _, tf = tempfile.mkstemp(suffix=cls.ext)
        try:
            subprocess.run(("pdftotext", path, tf), check=True)
            with open(tf, "r") as tf_handle:
                return [QuoteModel(m[1], m[2])
                        for line in tf_handle
                        for m in quote_regex.finditer(line)]
        finally:
            os.remove(tf)
