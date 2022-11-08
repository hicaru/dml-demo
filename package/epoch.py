import hashlib
import json
from random import randbytes
from block import Block


class Epoch:
    def __init__(self, id: int, blocks: list[Block], previous_hash: str) -> None:
        payload = str(id) + '.'.join(b.hash for b in blocks) + previous_hash
        self.epoch_number = id
        self.blocks = blocks
        self.previous_hash = previous_hash
        self.hash = hashlib.sha512(
            payload.encode('utf8')
        ).hexdigest()

    def serialize(self):
        return json.dumps(
            self,
            default=lambda o: o.__dict__,
            sort_keys=True,
            indent=4
        )

if __name__ == '__main__':
    # testing
    random_txns = lambda n : [randbytes(32).hex() for _ in range(n)]
    block_number = 42
    creater = 'creater'
    previous_hash = '0000000000000000000000000000000000000000000000000000000000000000'
    genesis_epoch_hash = '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
    epoch = 0

    block0 = Block(block_number, random_txns(16), creater, previous_hash, epoch)
    block_number += 1
    block1 = Block(block_number, [random_txns(8)], creater, block0.hash, epoch)
    block_number += 1
    block2 = Block(block_number, [random_txns(4)], creater, block1.hash, epoch)

    epoch = Epoch(epoch, [block0, block1, block2], genesis_epoch_hash)

    print(epoch.serialize())
