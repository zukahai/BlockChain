import hashlib as hasher
import datetime as date
import random

from numpy import block
from Block import *
class BlockChain:
    blocks = []
    
    def __init__(self):
        self.blocks = [self.create_genesis_block()]
    
    def add(self, block):
        self.blocks.append(block)
        
    def create_genesis_block(seft):
        return Block(0, date.datetime.now(), "Genesis Block", previous_hash= "0")
    
    def next_block(self):
        last_block = self.blocks[len(self.blocks) - 1]
        this_index = last_block.index + 1
        this_timestamp = date.datetime.now()
        this_data = "block" + str(this_index)
        this_hash = last_block.hash
        return Block(this_index, this_timestamp, this_data, this_hash)
    
    def check_hacker(self):
        blockchain = self.blocks
        for i in range(1, len(blockchain)):
            block = Block(i, blockchain[i].timestamp, blockchain[i].data, blockchain[i - 1].hash)
            if blockchain[i].hash != block.hash:
                return "Block " + str(i) + " is hacked!"
        return "Data safe!"
      
    def __str__(self):
        ans = ""
        for block in self.blocks:
            ans = ans + "{}\n".format(block)
        return ans