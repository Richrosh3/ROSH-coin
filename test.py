from blockchain import *
from time import *
import pprint

pp = pprint.PrettyPrinter(indent=4)

blockchain = Blockchain()
transactions = []

genesis = Block(transactions, asctime(localtime(time())), 0)
blockchain.addBlock(genesis)

sleep(1) # waits 1 second1 after creating genesis

b1 = Block(transactions, asctime(localtime(time())), 1)
blockchain.addBlock(b1)

sleep(5) # waits 5 seconds after creating b1

b2 = Block(transactions, asctime(localtime(time())), 2)
blockchain.addBlock(b2)

pp.pprint(blockchain.chainJSONencode())
print("Length: ", len(blockchain.chain))
