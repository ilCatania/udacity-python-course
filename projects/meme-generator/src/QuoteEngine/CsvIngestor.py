"""Csv parsing module."""
from typing import List

import pandas as pd

from .IngestorInterface import IngestorInterface
from .model import QuoteModel


class CsvIngestor(IngestorInterface):
    """Parse comma separated value files using pandas."""

    ext = ".csv"

    @classmethod
    def _parse(cls, path) -> List[QuoteModel]:
        """Parse quotes from file."""
        return (
            pd.read_csv(path).apply(lambda row: QuoteModel(row.body, row.author), axis=1).tolist()
        )
