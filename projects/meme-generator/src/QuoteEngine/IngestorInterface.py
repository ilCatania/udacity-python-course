"""Ingestor interface module."""
import os
from abc import ABC, abstractmethod
from pathlib import Path
from typing import List

from .model import QuoteModel, InvalidFileFormat


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
