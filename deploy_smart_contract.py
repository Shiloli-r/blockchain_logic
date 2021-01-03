""" The program Deploys a smart contract (written in solidity, on remix)
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

bytecode = "608060405234801561001057600080fd5b506113886000819055506040518060400160405280600881526020017f636f6d70757465720000000000000000000000000000000000000000000000008152506001908051906020019061006592919061006b565b50610116565b828054600181600116156101000203166002900490600052602060002090601f0160209004810192826100a157600085556100e8565b82601f106100ba57805160ff19168380011785556100e8565b828001600101855582156100e8579182015b828111156100e75782518255916020019190600101906100cc565b5b5090506100f591906100f9565b5090565b5b808211156101125760008160009055506001016100fa565b5090565b61033a806101256000396000f3fe608060405234801561001057600080fd5b50600436106100365760003560e01c80630c1b7c1e1461003b578063bcb131c9146100c5575b600080fd5b61004361018a565b6040518080602001838152602001828103825284818151815260200191508051906020019080838360005b8381101561008957808201518184015260208101905061006e565b50505050905090810190601f1680156100b65780820380516001836020036101000a031916815260200191505b50935050505060405180910390f35b610188600480360360408110156100db57600080fd5b81019080803590602001909291908035906020019064010000000081111561010257600080fd5b82018360208201111561011457600080fd5b8035906020019184600183028401116401000000008311171561013657600080fd5b91908080601f016020809104026020016040519081016040528093929190818152602001838380828437600081840152601f19601f820116905080830192505050505050509192919290505050610237565b005b606060006001600054818054600181600116156101000203166002900480601f0160208091040260200160405190810160405280929190818152602001828054600181600116156101000203166002900480156102285780601f106101fd57610100808354040283529160200191610228565b820191906000526020600020905b81548152906001019060200180831161020b57829003601f168201915b50505050509150915091509091565b816000819055508060019080519060200190610254929190610259565b505050565b828054600181600116156101000203166002900490600052602060002090601f01602090048101928261028f57600085556102d6565b82601f106102a857805160ff19168380011785556102d6565b828001600101855582156102d6579182015b828111156102d55782518255916020019190600101906102ba565b5b5090506102e391906102e7565b5090565b5b808211156103005760008160009055506001016102e8565b509056fea26469706673582212202e0c30ef5eefd8521274ac1b73d3811039fa6dd249e90317436ab231b3cbd4dd64736f6c63430007040033"
Asset = web3.eth.contract(abi=abi, bytecode=bytecode)
tx_hash = Asset.constructor().transact()
tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)

contract = web3.eth.contract(
    address=tx_receipt.contractAddress,
    abi=abi
)

# Transact
print("ASSET: \n", contract.functions.display().call())
tx_hash = contract.functions.setter(1000, 'Car').transact()
print("Transaction Hash: ", web3.toHex(tx_hash))
web3.eth.waitForTransactionReceipt(tx_hash)

print("\nASSET: \n", contract.functions.display().call())
