"""Data model."""
from dataclasses import dataclass


@dataclass(frozen=True)  # this should probably be a namedtuple
class QuoteModel:
    """A quote object."""

    body: str
    author: str

    def __str__(self):
        """Return the string representation."""
        return f'"{self.body}" - {self.author}'
