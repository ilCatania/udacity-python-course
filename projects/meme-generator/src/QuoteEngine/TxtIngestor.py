"""Txt parsing module."""
from typing import List

from .IngestorInterface import IngestorInterface
from .model import QuoteModel


class TxtIngestor(IngestorInterface):
    """Parse plain text files."""

    ext = ".txt"

    @classmethod
    def _parse(cls, path) -> List[QuoteModel]:
        """Parse quotes from file."""
        with open(path, "r", encoding="utf-8-sig") as f:
            return [QuoteModel(*line.strip().split(" - ")) for line in f if " - " in line]
