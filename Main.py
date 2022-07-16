from Model.BlockChain import *
import json

if __name__ == "__main__":
    a = BlockChain()
    a.read_data()
    # for i in range(1, 100):
    #     a.add(a.next_block())
    a.save_data()
    for block in a.blocks:
        print(block)
    print(a.check_hacker())
    
    