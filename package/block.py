import hashlib
import json


class Block:
    def __init__(self, id: int, transactions: list[str], creater: str, previous_hash: str, epoch: str):
        payload = str(id) + '.'.join(str(x) for x in transactions) + creater + previous_hash + str(epoch)
        self.blocknumber = id
        self.epoch = epoch
        self.previous_hash = previous_hash
        self.transactions = transactions
        self.creater = creater
        self.hash = hashlib.sha256(
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
    block_number = 42
    transactions = ['1', '2']
    creater = 'creater'
    previous_hash = '0000000000000000000000000000000000000000000000000000000000000000'
    epoch = 0

    block = Block(block_number, transactions, creater, previous_hash, epoch)

    print(block.serialize())
