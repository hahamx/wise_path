# coding:utf-8
import hashlib as hasher
from flask import Flask
from flask import request
import datetime
import json


class Bloc:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()

    def hash_block(self):
        sha = hasher.sha256()
        sha.update(str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash))
        return sha.hexdigest()

def create_gene_block():
    return Bloc(0,datetime.datetime.now(), 'genesis_block', '0')

def next_block(last_block):
    this_index = last_block.index + 1
    this_timestamp = datetime.datetime.now()
    this_data = "here is blok" + str(this_index)
    this_hash = last_block.hash
    return Bloc(this_index, this_timestamp, this_data, this_hash)


if __name__ == '__main__':
    b1 = Bloc(1, 123456, 'ydx', 'flzx3000c')
    print b1.hash_block()
    print create_gene_block().hash_block()
    blockchain = [create_gene_block()]
    previous_block = blockchain[0]

    num_of_blocks_to_add = 20

    for i in range(0, num_of_blocks_to_add):
        block_to_add = next_block(previous_block)
        blockchain.append(block_to_add)
        previous_block = block_to_add
        print "Block #{} has been added to the blockchian".format(block_to_add.index)
        print "Hash: {}n".format(block_to_add.hash)
        print "Hash: {}n".format(block_to_add.data)
        print "Hash: {}n".format(block_to_add.timestamp)

