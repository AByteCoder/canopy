from typing import List
from resin.knoweldge_base.chunker.base import Chunker
from resin.knoweldge_base.models import KBDocChunk
from resin.models.data_models import Document


class StubChunker(Chunker):

    def __init__(self, num_chunks_per_doc: int = 1):
        super().__init__()
        self.num_chunks_per_doc = num_chunks_per_doc

    def chunk_single_document(self, document: Document) -> List[KBDocChunk]:
        if document.text == "":
            return []

        # simply duplicate docs as chunks
        return [KBDocChunk(id=f"{document.id}_{i}",
                           document_id=document.id,
                           text=document.text + (f" dup_{i}" if i > 0 else ""),
                           source=document.source,
                           metadata=document.metadata)
                for i in range(self.num_chunks_per_doc)]

    async def achunk_single_document(self, document: Document) -> List[KBDocChunk]:
        raise NotImplementedError()
