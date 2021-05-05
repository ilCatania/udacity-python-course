"""Pdf parsing module."""
import os
import re
import subprocess
import tempfile
from typing import List

from .IngestorInterface import IngestorInterface
from .model import QuoteModel


class PdfIngestor(IngestorInterface):
    """Parse PDF files using pdftotext via the command line."""

    ext = ".pdf"
    quote_regex = re.compile('"([^"]+)" - (.+)')

    @classmethod
    def _parse(cls, path) -> List[QuoteModel]:
        """Parse quotes from file."""
        _, tf = tempfile.mkstemp(suffix=cls.ext)
        try:
            subprocess.run(("pdftotext", path, tf), check=True)
            with open(tf, "r") as tf_handle:
                return [
                    QuoteModel(m[1], m[2])
                    for line in tf_handle
                    for m in cls.quote_regex.finditer(line)
                ]
        finally:
            os.remove(tf)
