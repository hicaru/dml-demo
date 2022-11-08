import hashlib
import json


class Block:
    def __init__(self, id: int, transactions: list, creater: str, previous_hash: str, epoch: str):
        self.blocknumber = id
        self.epoch = epoch
        self.previous_hash = previous_hash
        self.transactions = transactions
        self.creater = creater
        self.hash = hashlib.sha256(
            self.blocknumber + '.'.join(str(x) for x in self.transactions) + self.creater + self.previous_hash + self.epoch
        ).hexdigest()

    def serialize(self):
        return json.dumps({
            "blocknumber": self.blocknumber,
            "transactions": self.transactions,
            "creater": self.creater,
            "hash": self.hash,
            "previous_hash": self.previous_hash,
            "epoch": self.epoch
        })
