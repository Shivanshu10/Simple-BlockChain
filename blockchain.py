from hashlib import sha256
import json
from time import time

class Block:
	def __init__(self, index, transactions, timestamp, previous_hash):
		self.index = index
		self.transactions = transactions
		self.timestamp = timestamp
		self.previous_hash = previous_hash

	def compute_hash(self):
		block_string = json.dumps(self.__dict__, sort_keys = True)
		return sha256(block_string.encode()).hexdigest()

class BlockChain:

	difficulty = 2

	def __init__(self):
		self.chain = []
		self.create_genesis_block()

	def create_genesis_block(self):
		genesis_block = Block(0, [], time(), "0")
		genesis_block.hash = genesis_block.compute_hash()
		self.chain.append(genesis_block)

	def proof_of_work(self, block):
		block.nonce = 0

		computed_hash = block.compute_hash()
		while not computed_hash.startswith('0' * BlockChain.difficulty):
			block.nonce += 1
			computed_hash = block.compute_hash()

		return computed_hash

	def add_block(self, block, proof):
		previous_hash = self.last_block.hash

		if previous_hash != block.previous_hash:
			return False
		
		if not BlockChain.is_valid_proof(block, proof):
			return False

		block.hash = proof
		self.chain.append(block)
		return True

	def is_valid_proof(self, block, block_hash):
		if (block_hash.startswith('0' * BlockChain.difficulty) and block_hash == block.compute_hash()):
			return True

	@property
	def last_block(self):
		return self.chain[-1]

