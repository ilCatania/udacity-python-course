"""Docx parsing module."""
import re
from typing import List

import docx

from .IngestorInterface import IngestorInterface
from .model import QuoteModel


class DocxIngestor(IngestorInterface):
    """Parse Microsoft Word file format using `python-docx`."""

    ext = ".docx"
    quote_regex = re.compile('"([^"]+)" - (.+)')

    @classmethod
    def _parse(cls, path) -> List[QuoteModel]:
        """Parse quotes from file."""
        doc = docx.Document(path)
        return [
            QuoteModel(m[1], m[2]) for p in doc.paragraphs for m in cls.quote_regex.finditer(p.text)
        ]
