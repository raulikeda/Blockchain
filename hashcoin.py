from hashlib import blake2b
import datetime
import time

def testNonce(previous, nonce, coinbase, transactions):
  message = str(previous) + str(nonce) + str(coinbase) + str(transactions)
  hash = blake2b(message.encode(), digest_size=4)
  return hash.hexdigest()

def mountCoinbase(miner, value):
  return (miner, value)

def mountTransaction(buyer, seller, value):
  return (buyer, seller, value)
