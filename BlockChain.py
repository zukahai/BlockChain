import hashlib as hasher
import datetime as date

class Block:
  def __init__(self, index, timestamp, data, previous_hash):
    self.index = index
    self.timestamp = timestamp
    self.data = data
    self.previous_hash = previous_hash
    self.hash = self.hash_block()

  def hash_block(self):
    sha = hasher.sha256()
    sha = (str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash))
    sha = hasher.sha256(sha.encode('utf-8')).hexdigest()
    return sha

def create_genesis_block():
    return Block(0, date.datetime.now(), "Genesis Block", previous_hash= "0")

def next_block(last_block):
    this_index = last_block.index + 1
    this_timestamp = date.datetime.now()
    this_data = "I'm block " + str(this_index)
    this_hash = last_block.hash
    return Block(this_index, this_timestamp, this_data, this_hash)

blockchain = [create_genesis_block()]
previous_block = blockchain[0]

num_of_blocks_to_add = 20

for i in range(0, num_of_blocks_to_add):
  block_to_add = next_block(previous_block)
  blockchain.append(block_to_add)
  previous_block = block_to_add

#   print ("Block #{} added in blockchain".format(format(block_to_add.index, '3d')))
print ("Hash: {}\n".format(block_to_add.hash))

for i in range(1, num_of_blocks_to_add):
    print("{}\t{}".format(blockchain[i].hash, Block.hash_block(Block(i, blockchain[i].timestamp, blockchain[i].data, blockchain[i - 1].hash))))