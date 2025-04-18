import helpers
import os
from io import BytesIO
from block import Block

DELTA = 120
EPOCH_LEN = 60

def update_target(prev_target, delta):
    return int(prev_target * delta / DELTA)

def mine_block(version, prev_block, merkle_root, bits, timestamp):
    nonce = 0
    b = Block(version, prev_block, merkle_root, timestamp, bits, nonce)
    while int(b.block_id().hex(), 16) > b.target():
        nonce += 1
        if nonce == 2**32:
            nonce = 0
            timestamp = helpers.now()
            b.update_timestamp(timestamp)
        b.update_nonce(nonce)
    return b

def write_blockchain(filename='blockchain2.dat'):
    if os.path.exists(filename):
        os.remove(filename)

    genesis_hex = '01000000000000000000000000000000000000000000000000000000000000' \
                  '00000000003ba3edfd7a7b12b27ac72c3e67768f617fc81bc3888a51323a9f' \
                  'b8aa4b1e5e4a29ab5f49ffff001d1dac2b7c'
    genesis_bytes = bytes.fromhex(genesis_hex)
    b = Block.parse(genesis_bytes)

    print("Genesis block:", b.block_id().hex())
    print(b)
    b.write(filename)

    version = b.version
    merkle_root = helpers.hash256(b'Principles of Cryptocurrency Design - aa 24/25')
    prev_block = b.block_id()
    timestamp = helpers.now()
    bits = bytes.fromhex('1e00ffff')
    target = Block(version, prev_block, merkle_root, timestamp, bits, 0).target()

    timestamps = [timestamp]

    for i in range(1, 1000):
        if i % EPOCH_LEN == 0:
            delta = timestamps[-1] - timestamps[-EPOCH_LEN]
            target = update_target(target, delta)
            exp = 3
            while target >= 256**(exp + 1):
                exp += 1
            coeff = target // 256**(exp - 3)
            bits = exp.to_bytes(1, 'big') + coeff.to_bytes(3, 'little')

        timestamp = helpers.now()
        b = mine_block(version, prev_block, merkle_root, bits, timestamp)
        b.write(filename)
        print(f"\nBlock #{i}")
        print("block_id:", b.block_id().hex())
        print(b)
        b.write(filename)
        prev_block = b.block_id()
        timestamps.append(b.timestamp)

if __name__ == '__main__':
    write_blockchain()
