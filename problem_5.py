# Blockchain

# A Blockchain is a sequential chain of records, similar to a linked list. Each
# block contains some information and how it is connected related to the other
# blocks in the chain. Each block contains a cryptographic hash of the previous
# block, a timestamp, and transaction data. For our blockchain we will be using
# a SHA-256 hash, the Greenwich Mean Time when the block was created, and text
# strings as the data.

# Use your knowledge of linked lists and hashing to create a blockchain
# implementation.
import time
import hashlib

# We do this for the information we want to store in the block chain such as
# transaction time, data, and information like the previous chain.

class Block:

    def __init__(self, timestamp, data, previous):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous.hash
        self.previous = previous

        self.hash = self.calc_hash()

    def calc_hash(self):
        sha = hashlib.sha256()

        hash_str = ""
        hash_str += self.data
        hash_str += str(self.timestamp)
        hash_str += self.previous_hash
        hash_str = hash_str.encode('utf-8')

        sha.update(hash_str)

        return sha.hexdigest()

    def __repr__(self):
        return f"{str(int(self.timestamp * 100) / 100)}\t{self.hash}\t{self.previous_hash}\t{self.data}"

class DummyBlock(Block):
    def __init__(self):
        self.timestamp = time.time()
        self.data = "I am Groot"
        self.previous_hash = "DummyHashDummyHashDummyHashDummyHashDummyHashDummyHashDummyHashD"
        self.previous = None
        self.hash = self.calc_hash()

class BlockChain(object):

    def __init__(self):
        self.tail = DummyBlock()
        self.size = 1

    def append(self, data):
        old = self.tail
        new = Block(time.time(), data, old)
        self.tail = new
        self.size += 1

    def __repr__(self):
        str = ""
        block = self.tail
        while block:
            str += block.__repr__() + "\n"
            block = block.previous
        return str


# Test 1 - Empty Blockchain
chain = BlockChain()

print(chain)
print (chain.size)
# 1  Dummy block

print (chain.tail.data)
# I am Groot

# Test 2 - 4 Blocks in chain
chain.append("Rocket")
chain.append("Star Lord")
chain.append("Gemorrah")
chain.append("Drax")

print (chain)
# Drax

# Test 3 - 10k blocks
for _ in range(10_000):
    chain.append("something else!")

print(chain)


