import docx
import os
import re
from abc import ABC, abstractmethod
from typing import List

from .model import QuoteModel


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


class DocxIngestor(IngestorInterface):
    """Parse Microsoft Word file format using"""

    ext = ".docx"
    r = re.compile('"([^"]+)" - (.+)')

    @classmethod
    def parse(cls, path) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise InvalidFileFormat
        quotes = []
        doc = docx.Document(path)
        for p in doc.paragraphs:
            quotes.extend(QuoteModel(m[1], m[2]) for m in cls.r.finditer(p.text))
        return quotes
