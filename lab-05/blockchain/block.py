import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, transaction, proof, timestamp):
        self.index = index
        self.previous_hash = previous_hash
        self.transaction = transaction
        self.proof = proof
        self.timestamp = timestamp
        self.hash = self.calculate_hash()
        
    def calculate_hash(self):
        data = str(self.index) + str(self.previous_hash) + str(self.transaction) + str(self.proof) + str(self.timestamp)
        return hashlib.sha256(data.encode()).hexdigest()
    
        
        
        
