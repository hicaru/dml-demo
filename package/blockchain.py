from epoch import Epoch
from block import Block
from config import zero_512_hash


class BlockChain:
    def __init__(self):
        self.chain = [Epoch(0, [], zero_512_hash)]

    def get_current_epoch(self):
        return self.chain[-1]

    def get_epoch(self, epoch_number):
        return self.chain[epoch_number]


if __name__ == '__main__':
    # testing
    chain = BlockChain()
