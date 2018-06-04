# -*-coding:utf-8 -*-
import sys

sys.path.append('.')
import json
import datetime as date
from flask import Flask
from flask import request
import hashlib as hasher
import random
import os

node = Flask(__name__)


# Store the transactions that
# this node has in a list
# Create the blockchain and add the genesis block
# global blockchain


class Bloc:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()

    def hash_block(self):
        sha = hasher.sha256()
        sha.update(str(self.index) +
                   str(self.timestamp) +
                   str(self.data) +
                   str(self.previous_hash))
        return sha.hexdigest()


def create_genesis_block():
    # Manually construct a block with
    # index zero and arbitrary previous hash
    return Bloc(0, date.datetime.now(), "Genesis Block", "0")


def next_block(last_block):
    this_index = last_block.index + 1
    this_timestamp = date.datetime.now()
    this_data = "Hey! I'm block " + str(this_index)
    this_hash = last_block.hash
    return Bloc(this_index, this_timestamp, this_data, this_hash)


blockchain = [create_genesis_block()]
previous_block = blockchain[0]

# How many blocks should we add to the chain
# after the genesis block
num_of_blocks_to_add = 20

# Add blocks to the chain
for i in range(0, num_of_blocks_to_add):
    block_to_add = next_block(previous_block)
    blockchain.append(block_to_add)
    previous_block = block_to_add
    # Tell everyone about it!
    print "Block #{} has been added to the blockchain!".format(block_to_add.index)
    print "Hash: {}n".format(block_to_add.hash)


def save_chain(chain_list=None):
    if not chain_list:
        return False
    file_path = "./mark/chain_pack.log"
    if not os.path.exists(file_path):
        os.mkdir(file_path)
    with open("./mark/chain_pack.log", 'ab+') as c_p:
        for cha in chain_list:
            cha_info = "from:{}, to:{}, amount:{}, RMB:{}".format(cha['from'], cha['to'], cha['amount'],
                                                                  int(cha['amount']) * 6.35)
            c_p.write(cha_info + '\n' + '\n')


this_nodes_transactions = []


@node.route('/txion', methods=['POST', 'GET'])
def transaction():
    if request.method == 'POST':
        # On each new POST request,
        # we extract the transaction data
        new_txion = request.get_json()
        # Then we add the transaction to our list
        this_nodes_transactions.append(new_txion)
        # Because the transaction was successfully
        # submitted, we log it to our console
        print "New transaction"
        print "FROM: {}".format(new_txion['from'])
        print "TO: {}".format(new_txion['to'])
        print "AMOUNT: {}\n".format(new_txion['amount'])
        save_chain(this_nodes_transactions)
        # Then we let the client know it worked out
        return "Transaction submission successful\n"
    else:
        new_txion = request.get_json()
        this_nodes_transactions.append(new_txion)
        print "New transaction"
        # print "FROM: {}".format(new_txion['from'])
        # print "TO: {}".format(new_txion['to'])
        # print "AMOUNT: {}\n".format(new_txion['amount'])
        return "Transaction submission successful\n"


# ...blockchain
# ...Block class definition
miner_address = "q3nf394hjg-random-miner-address-34nf3i4nflkn3oi"


def proof_of_work(last_proof):
    # Create a variable that we will use to find
    # our next proof of work
    incrementor = last_proof + 1
    # Keep incrementing the incrementor until
    # it's equal to a number divisible by 9
    # and the proof of work of the previous
    # block in the chain
    while not (incrementor % 9 == 0 and incrementor % last_proof == 0):
        incrementor += 1
    # Once that number is found,
    # we can return it as a proof
    # of our work
    return incrementor


@node.route('/', methods=['GET'])
def mine():
    # # Get the last proof of work
    last_block = blockchain[len(blockchain) - 1]
    print "last_block:{}".format(last_block)
    last_proof = last_block.index
    # # Find the proof of work for
    # # the current block being mined
    # # Note: The program will hang here until a new
    # #       proof of work is found
    print "last_proof:{}".format(last_proof)
    # print "last_proof data:",  last_proof.data, last_proof.timestamp, last_proof.index
    proof = proof_of_work(last_proof)
    print "proof:{}".format(proof)
    # # Once we find a valid proof of work,
    # # we know we can mine a block so
    # # we reward the miner by adding a transaction
    net_am = random.choice(range(1000))
    this_nodes_transactions.append(
        {"from": "network", "to": miner_address, "amount": net_am}
    )
    save_chain(this_nodes_transactions)
    #
    # # Now we can gather the data needed
    # # to create the new block
    new_block_data = {
        "proof-of-work": proof,
        "transactions": list(this_nodes_transactions)
    }
    new_block_index = last_block.index + 1
    new_block_timestamp = date.datetime.now()
    last_block_hash = last_block.hash
    # # Empty transaction list
    this_nodes_transactions[:] = []
    # # Now create the
    # # new block!
    mined_block = Bloc(
        new_block_index,
        new_block_timestamp,
        new_block_data,
        last_block_hash
    )
    blockchain.append(mined_block)
    # Let the client know we mined a block

    # return json.dumps({
    #     "index": new_block_index,
    #     "timestamp": str(new_block_timestamp),
    #     "data": new_block_data,
    #     "hash": last_block_hash
    # }) + "\n"

    return json.dumps({
        "index": new_block_index,
        "timestamp": str(new_block_timestamp),
        "data": new_block_data,
        "hash": last_block_hash
    })


@node.route('/blocks', methods=['GET'])
def get_blocks():
    chain_to_send = blockchain
    # Convert our blocks into dictionaries
    # so we can send them as json objects later
    for block in chain_to_send:
        block_index = str(block.index)
        block_timestamp = str(block.timestamp)
        block_data = str(block.data)
        block_hash = block.hash
        block = {
            "index": block_index,
            "timestamp": block_timestamp,
            "data": block_data,
            "hash": block_hash
        }
        # Send our chain to whomever requested it
        chain_to_send = json.dumps(block)
    return chain_to_send


if __name__ == '__main__':
    print proof_of_work(12)
    node.run(host='0.0.0.0', port=5002, debug=True)
