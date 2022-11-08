from block import Block
import hashlib


class Epoch:
    def __init__(self, id: int, blocks: list[Block]) -> None:
        self.epoch_number = id
        self.blocks = blocks
        self.hash = hashlib.sha256(
            id + '.'.join(b.hash for b in self.blocks)
        ).hexdigest()
