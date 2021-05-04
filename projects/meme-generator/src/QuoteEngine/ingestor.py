"""Quote import module."""
import os
import re
import subprocess
import tempfile
from abc import ABC, abstractmethod
from pathlib import Path
from typing import List

import docx
import pandas as pd

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
            raise InvalidFileFormat(path, cls)
        return cls._parse(path)

    @classmethod
    def scan(cls, path) -> List[QuoteModel]:
        """Scan the input path, including subfolders, and parse all supported files for quotes."""
        quotes = []
        for dir, _, files in os.walk(path):
            for f in files:
                if cls.can_ingest(f):
                    quotes.extend(cls.parse(Path(dir) / f))
        return quotes

    @classmethod
    @abstractmethod
    def _parse(cls, path) -> List[QuoteModel]:
        """Format-specific parsing logic goes here."""
        raise NotImplementedError


class TxtIngestor(IngestorInterface):
    """Parse plain text files."""

    ext = ".txt"

    @classmethod
    def _parse(cls, path) -> List[QuoteModel]:
        """Parse quotes from file."""
        with open(path, "r", encoding="utf-8-sig") as f:
            return [QuoteModel(*line.strip().split(" - ")) for line in f if " - " in line]


class CsvIngestor(IngestorInterface):
    """Parse comma separated value files using pandas."""

    ext = ".csv"

    @classmethod
    def _parse(cls, path) -> List[QuoteModel]:
        """Parse quotes from file."""
        return (
            pd.read_csv(path).apply(lambda row: QuoteModel(row.body, row.author), axis=1).tolist()
        )


class DocxIngestor(IngestorInterface):
    """Parse Microsoft Word file format using `python-docx`."""

    ext = ".docx"

    @classmethod
    def _parse(cls, path) -> List[QuoteModel]:
        """Parse quotes from file."""
        doc = docx.Document(path)
        return [
            QuoteModel(m[1], m[2]) for p in doc.paragraphs for m in quote_regex.finditer(p.text)
        ]


class PdfIngestor(IngestorInterface):
    """Parse PDF files using pdftotext via the command line."""

    ext = ".pdf"

    @classmethod
    def _parse(cls, path) -> List[QuoteModel]:
        """Parse quotes from file."""
        _, tf = tempfile.mkstemp(suffix=cls.ext)
        try:
            subprocess.run(("pdftotext", path, tf), check=True)
            with open(tf, "r") as tf_handle:
                return [
                    QuoteModel(m[1], m[2]) for line in tf_handle for m in quote_regex.finditer(line)
                ]
        finally:
            os.remove(tf)


class Ingestor(IngestorInterface):
    """Main ingestor class supporting multiple types.

    Supports registering new ingestors in order to support
    additional file types.
    """

    _ingestors = set()

    @classmethod
    def can_ingest(cls, path) -> bool:
        """Return whether the input file is supported."""
        return any(ing.can_ingest(path) for ing in cls._ingestors)

    @classmethod
    def _parse(cls, path) -> List[QuoteModel]:
        for ing in cls._ingestors:  # type: IngestorInterface
            if ing.can_ingest(path):
                return ing.parse(path)
        raise InvalidFileFormat

    @classmethod
    def register(cls, ingestor: IngestorInterface):
        """Register a new ingestor type."""
        cls._ingestors.add(ingestor)

    @classmethod
    def deregister(cls, ingestor: IngestorInterface):
        """Deregister an ingestor type."""
        cls._ingestors.remove(ingestor)

    @classmethod
    def register_defaults(cls):
        """Register default ingestor types."""
        for ing in (CsvIngestor, DocxIngestor, PdfIngestor, TxtIngestor):
            cls.register(ing)
