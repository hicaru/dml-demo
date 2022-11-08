from block import Block

class Epoch:
    def __init__(self, id: int, blocks: list[Block]) -> None:
        self.epoch_number = id
        self.blocks = blocks
