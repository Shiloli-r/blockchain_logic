from web3 import Web3
from pprint import pprint

infura_url = "https://mainnet.infura.io/v3/25767e76b9de4c05ad7dbaeb47ebd65e"
web3 = Web3(Web3.HTTPProvider(infura_url))

print(web3.isConnected())

latest = web3.eth.blockNumber
# pprint(web3.eth.getBlock(latest).__dict__)

# get the last 10 blocks
for i in range(0, 10):
    print("\nBlock {}:".format(i))
    pprint(web3.eth.getBlock(latest-i).__dict__)


# get specific transaction on block
hash = "0x98e31e6f60957465a153cadd1c036427204325891cd57de77502eb469bf5aa55"
print("\n\n")
pprint(web3.eth.getTransactionByBlock(hash, 5).__dict__)  # get 5th transaction
