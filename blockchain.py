import hashlib
import json
from time import time


class Blockchain (object):
    def __init__(self):
        self.chain = []

    def getLastBlock(self):
        return self.chain[-1]

    def addBlock(self, block):
        if(len(self.chain) > 0):
            block.prev = self.getLastBlock().hash
        else:
            block.prev = "none"
        self.chain.append(block)

    def chainJSONencode(self):
        blockArrJSON = []
        for block in self.chain: 
            blockJSON = {}
            blockJSON['hash'] = block.hash
            blockJSON['index'] = block.index
            blockJSON['prev'] = block.prev
            blockJSON['time'] = block.time

            transactionsJSON = []
            tJSON = {}
            for transaction in block.transactions: 
                tJSON['time'] = transaction.time
                tJSON['sender'] = transaction.sender
                tJSON['receiver'] = transaction.receiver
                tJSON['amount'] = transaction.amount
                tJSON['hash'] = transaction.hash
                transactionsJSON.append(tJSON)

            blockJSON['transactions'] = transactionsJSON
            blockArrJSON.append(blockJSON)

        return blockArrJSON

class Block (object):
    def __init__(self, transactions, time, index):
        self.index = index
        self.transactions = transactions
        self.time = time
        self.prev = ''
        self.hash = self.calculateHash()

    def calculateHash(self):
        hashTransactions = ""
        for transaction in self.transactions:
            hashTransactions += transaction.hash

        hashString = str(self.time) + hashTransactions + self.prev + str(self.index)
        hashEncoded = json.dumps(hashString, sort_keys = True).encode()
        return hashlib.sha256(hashEncoded).hexdigest()


class Transaction (object):
    def __init__(self, sender, receiver, amount):
            self.sender = sender
            self.receiever = receiver
            self.amount = amount
            self.time = time()
            self.hash = self.calculateHash()

    def calculateHash(self):
        hashTransactions = ""
        for transaction in self.transactions:
            hashTransactions += transaction.hash

        hashString = self.sender + self.receiver + str(self.amount) + str(self.time)
        hashEncoded = json.dumps(hashString, sort_keys = True).encode()
        return hashlib.sha256(hashEncoded).hexdigest()
