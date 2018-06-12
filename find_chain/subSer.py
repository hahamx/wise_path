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


# 以列表的形式, 存储传输的信息
# 创建并添加链币到区块中
# 链币全局可见


class Bloc:
    """定义区块的结构"""
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        # 为了确保整个区块链的完整性，每个区块都会有一个自识别的哈希值
        # 每个区块的哈希是该块的索引、时间戳、数据和前一个区块的哈希值等数据的加密哈希值。
        self.hash = self.hash_block()

    def hash_block(self):
        sha = hasher.sha256()
        sha.update(str(self.index) +
                   str(self.timestamp) +
                   str(self.data) +
                   str(self.previous_hash))
        return sha.hexdigest()


def create_genesis_block():
    # 这个区块的索引为 0 
    # 其包含一些任意的数据值，其“前一哈希值”参数也是任意值。
    return Bloc(0, date.datetime.now(), "Genesis Block", "0")


def next_block(last_block):
    """该函数将获取链中的前一个区块作为参数，为要生成的区块创建数据，并用相应的数据返回新的区块。
    新的区块的哈希值来自于之前的区块，这样每个新的区块都提升了该区块链的完整性。
    如果我们不这样做，外部参与者就很容易“改变过去”，把我们的链替换为他们的新链了。
    这个哈希链起到了加密的证明作用，并有助于确保一旦一个区块被添加到链中，就不能被替换或移除。
    """
    this_index = last_block.index + 1
    this_timestamp = date.datetime.now()
    this_data = "Hey! I'm block " + str(this_index)
    this_hash = last_block.hash
    return Bloc(this_index, this_timestamp, this_data, this_hash)


blockchain = [create_genesis_block()]
previous_block = blockchain[0]

# 打算一次创建多少链币
num_of_blocks_to_add = 10

# 添加链币到链块
for i in range(0, num_of_blocks_to_add):
    block_to_add = next_block(previous_block)
    blockchain.append(block_to_add)
    previous_block = block_to_add
    # 告诉所有人所有信息
    print "Block #{} has been added to the blockchain!".format(block_to_add.index)
    print "Hash: {}n".format(block_to_add.hash)


def save_chain(chain_list=None):
    """简单的钱包, 用于存储链币"""
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
        # 从每次新的post请求中提取数据
        new_txion = request.get_json()
        # 然后添加到我们的链块
        this_nodes_transactions.append(new_txion)
        # 传输成功,存到我们的log
        print "New transaction"
        print "FROM: {}".format(new_txion['from'])
        print "TO: {}".format(new_txion['to'])
        print "AMOUNT: {}\n".format(new_txion['amount'])
        save_chain(this_nodes_transactions)
        # 让对方知道我们传输成功
        return "Transaction submission successful\n"
    else:
        new_txion = request.get_json()
        this_nodes_transactions.append(new_txion)
        print "New transaction"
        # print "FROM: {}".format(new_txion['from'])
        # print "TO: {}".format(new_txion['to'])
        # print "AMOUNT: {}\n".format(new_txion['amount'])
        return "Transaction submission successful\n"


# 定义
miner_address = "q3nf3943234-random-min_addr-34nf3i555454xasd"


def proof_of_work(last_proof):
    """在服务器层，以在多台机器上跟踪链的改变，并通过工作量证明算法（POW）来限制给定时间周期内可以添加的区块数量。
    创建了一个简单的 PoW 算法。要创建一个新区块，矿工的计算机需要递增一个数字，
    当该数字能被 11 （随机）整除时，这就是最后这个区块的证明数字，就会挖出一个新的区块，
    而该矿工就会得到一个新的链币.
    """
    incrementor = last_proof + 1

    while not (incrementor % 11 == 0 and incrementor % last_proof == 0):
        incrementor += 1

    return incrementor


@node.route('/', methods=['GET'])
def mine():
    """控制特定的时间段内挖到的区块数量，并且我们给了网络中的人新的币，让他们彼此发送。
    但是如我们说的，我们只是在一台计算机上做的。如果区块链是去中心化的，我们怎样才能确保每个节点都有相同的链呢？
    要做到这一点，我们会使每个节点都广播其（保存的）链的版本，并允许它们接受其它节点的链。
    然后，每个节点会校验其它节点的链，以便网络中每个节点都能够达成最终的链的共识。这称之为共识算法（consensus algorithm）。
    """
    last_block = blockchain[len(blockchain) - 1]
    print "last_block:{}".format(last_block)
    last_proof = last_block.index

    print "last_proof:{}".format(last_proof)
    # print "last_proof data:",  last_proof.data, last_proof.timestamp, last_proof.index
    proof = proof_of_work(last_proof)
    print "proof:{}".format(proof)
    
    net_am = random.choice(range(1000))
    this_nodes_transactions.append(
        {"from": "network", "to": miner_address, "amount": net_am}
    )
    save_chain(this_nodes_transactions)

    new_block_data = {
        "proof-of-work": proof,
        "transactions": list(this_nodes_transactions)
    }
    new_block_index = last_block.index + 1
    new_block_timestamp = date.datetime.now()
    last_block_hash = last_block.hash
    # 清空
    this_nodes_transactions[:] = []
    # 创建新区块
    mined_block = Bloc(
        new_block_index,
        new_block_timestamp,
        new_block_data,
        last_block_hash
    )
    blockchain.append(mined_block)
    # 返回让对方知道创建了新的区块

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
    """
    如果一个节点的链与其它的节点的不同（例如有冲突），那么最长的链保留，更短的链会被删除。
    如果我们网络上的链没有了冲突，那么就可以继续了。
    """
    chain_to_send = blockchain
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
        
        chain_to_send = json.dumps(block)
    return chain_to_send


if __name__ == '__main__':
    print proof_of_work(12)
    node.run(host='0.0.0.0', port=5002, debug=True)
