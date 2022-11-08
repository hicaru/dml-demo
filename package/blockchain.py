from epoch import Epoch
from block import Block
from config import zero_512_hash


class BlockChain:
    def __init__(self):
        self.chain = [Epoch(0, [], zero_512_hash)]

