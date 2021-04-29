from dataclasses import dataclass


@dataclass(frozen=True)  # this should probably be a namedtuple
class QuoteModel:
    body: str
    author: str
