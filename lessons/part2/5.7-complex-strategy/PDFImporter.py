
from typing import List
import tempfile
import subprocess

from .ImportInterface import ImportInterface
from .Cat import Cat

class PDFImporter(ImportInterface):
    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[Cat]:
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')
        
        cats = []
        t = tempfile.mkstemp(suffix=".txt")
        try:
            subprocess.call(("pdftotext", path, t))
            with open(t, "r") as f:
                for l in f:
                    parts = l.split(",")
                    cats.append(Cat(l[0], int(l[1]), bool(l[2])))
        finally:
            os.remove(t)

        return cats
