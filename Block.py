import hashlib as hasher

class Block:
  def __init__(self, index, timestamp, data, previous_hash):
    self.index = index
    self.timestamp = timestamp
    self.data = data
    self.previous_hash = previous_hash
    self.hash = self.hash_block()

  def hash_block(self):
    d = 4
    sha = (str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash))
    while sha[0: d] != "a" * d:
      sha = hasher.sha256(sha.encode('utf-8')).hexdigest()
    return sha