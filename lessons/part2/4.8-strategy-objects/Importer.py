from abc import ABC, abstractmethod
import os

class ImporterInterface(ABC):
    
    allowed_extensions = set()

    @classmethod
    def can_ingest(cls, f) -> bool:
        filename, ext = os.path.splittext(f)
        return  ext in allowed_extensions
    
    @classmethod
    @abstractmethod
    def parse(cls, f):
        pass

