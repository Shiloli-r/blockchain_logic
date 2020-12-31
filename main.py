from block import Block


def main():
    genesis_block = Block("No previous Transaction", ["Satoshi sent 5 BTC to Hal Finney",
                                                      "Satoshi sent 1 BTC to Ivan",
                                                      "Ronnie sent 1 BTC to Rhino"])
    second_block = Block(genesis_block.block_hash, ["Redington sent 3 BTC to Liz"])
    third_block = Block(second_block.block_hash, ["A to C 5 BTC", "G to F 8 BTC"])

    print("Genesis Block Hash: ", genesis_block.block_hash)
    print("Second Block Hash: ", second_block.block_hash)
    print("Third Block Hash: ", third_block.block_hash)


if __name__ == '__main__':
    main()
