import datetime as date
import json

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
    
    def read_data(self):
        try:
            f = open ('data/blocks.json', "r")
            data = json.loads(f.read())
            self.blocks = [Block(js['index'], js['timestamp'], js['data'], js['previous_hash']) for js in data]
        except:
            self.blocks = [self.create_genesis_block()]
            
    def save_data(self):
        json_string = json.dumps([ob.__dict__ for ob in self.blocks], default=str, ensure_ascii=False, indent=4)
        with open('data/blocks.json', 'w', encoding='utf-8') as f:
            f.write("{}".format(json_string))
    
    def next_block(self):
        last_block = self.blocks[len(self.blocks) - 1]
        this_index = last_block.index + 1
        this_timestamp = date.datetime.now()
        this_data = "block" + str(this_index)
        this_hash = last_block.hash
        return Block(this_index, this_timestamp, this_data, this_hash)
    
    def check_hacker(self):
        for i in range(1, len(self.blocks)):
            block = Block(i, self.blocks[i].timestamp, self.blocks[i].data, self.blocks[i - 1].hash)
            if self.blocks[i].hash != block.hash:
                print(self.blocks[i].hash, block.hash)
                # self.blocks[i].hash = block.hash
                return "Block " + str(i) + " is hacked!"
        return "Data safe!"
      
    def __str__(self):
        ans = ""
        for block in self.blocks:
            ans = ans + "{}\n".format(block)
        return ans