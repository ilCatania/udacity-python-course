from dataclasses import dataclass


@dataclass(frozen=True)  # this should probably be a namedtuple
class QuoteModel:
    body: str
    author: str

    def __str__(self):
        return f'"{self.body}" - {self.author}'
