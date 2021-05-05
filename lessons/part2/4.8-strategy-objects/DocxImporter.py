import docx
from .Importer import ImporterInterface

class DocxImporter(ImporterInterface):
    
    @classmethod
    def parse(cls, f):
        text = []
        with open(f, "r") as handle:
            doc = docx.Document(handle)
            for p in doc.paragraphs:
                text.append(p.text)
        return "\n".join(text)

