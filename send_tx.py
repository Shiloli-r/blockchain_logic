from web3 import Web3

ganache_url = "http://localhost:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

# Test the connection
# print(web3.isConnected())
# print(web3.eth.blockNumber)

account_1 = "0xa30CFb470E49D7ce0E62F7c4a10e37768d82f89A"
account_2 = "0xA2AB2cdc202521ec77B9Fc914BF1a9512a579883"
private_key = "0dfa0e42033dbdec2d77eb29d7ac7aa4077e994b8f166d7ad467999354fd2032"  # private key of account_1

# get the nonce
nonce = web3.eth.getTransactionCount(account_1)

# build a transaction
tx = {
    'nonce': nonce,
    'to': account_2,
    'value': web3.toWei(1, "ether"),
    'gas': 200000,
    'gasPrice': web3.toWei(50, 'gwei'),
}

# sign the transaction
signed_tx = web3.eth.account.signTransaction(tx, private_key)
# send the transaction and get transaction hash
tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
print(web3.toHex(tx_hash))
