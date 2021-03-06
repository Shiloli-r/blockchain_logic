""" The program interacts with a smart contract (written in solidity, on remix)
    A transaction is carried out through the smart contract
    Smart Contract used: asset.sol
    Written 1/3/2021
"""
import json
from web3 import Web3

ganache_url = "http://localhost:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

web3.eth.defaultAccount = web3.eth.accounts[0]  # Get first account on ganache

abi = json.loads('[{"inputs":[],"name":"asset_","outputs":[],"stateMutability":"nonpayable","type":"function"},'
                 '{"inputs":[],"name":"display","outputs":[{"internalType":"string","name":"","type":"string"},'
                 '{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},'
                 '{"inputs":[{"internalType":"uint256","name":"_price","type":"uint256"},{"internalType":"string",'
                 '"name":"_name","type":"string"}],"name":"setter","outputs":[],"stateMutability":"nonpayable",'
                 '"type":"function"}]')
address = web3.toChecksumAddress("0xa454A2C633c2824aBf2Bcec8BAb7533FD6455606")
contract = web3.eth.contract(address=address, abi=abi)
print("\nASSET: \n", contract.functions.display().call())

# Transaction
tx_hash = contract.functions.setter(1000, 'Car').transact()
print("Transaction Hash: ", web3.toHex(tx_hash))
web3.eth.waitForTransactionReceipt(tx_hash)

print("\nASSET: \n", contract.functions.display().call())
