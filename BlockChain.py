import hashlib as hasher
import datetime as date
import random
from Block import *

def create_genesis_block():
    return Block(0, date.datetime.now(), "Genesis Block", previous_hash= "0")

def next_block(last_block):
    this_index = last_block.index + 1
    this_timestamp = date.datetime.now()
    this_data = "block" + str(this_index)
    this_hash = last_block.hash
    return Block(this_index, this_timestamp, this_data, this_hash)
  
def check_hacker(blockchain):
  for i in range(1, len(blockchain)):
    block = Block(i, blockchain[i].timestamp, blockchain[i].data, blockchain[i - 1].hash)
    if blockchain[i].hash != block.hash:
      return "Block " + str(i) + " is hacked!"
  return "Data safe!"

blockchain = [create_genesis_block()]
previous_block = blockchain[0]

num_of_blocks_to_add = 20

for i in range(0, num_of_blocks_to_add):
  block_to_add = next_block(previous_block)
  blockchain.append(block_to_add)
  previous_block = block_to_add

print("Blockchain init")

for block in blockchain:
  print("{}\t{}".format(block.previous_hash, block.hash))

  # print ("Block #{} added in blockchain".format(format(block_to_add.index, '3d')))

print ("Hash: {}\n".format(block_to_add.hash))

# for i in range(1, num_of_blocks_to_add):
#     print("{}\t{}".format(blockchain[i].hash, Block.hash_block(Block(i, blockchain[i].timestamp, blockchain[i].data, blockchain[i - 1].hash))))

# print(check_hacker(blockchain))
# blockchain[random.choice(range(0, num_of_blocks_to_add))].data = "222"
# print(check_hacker(blockchain))