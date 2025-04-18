# esercizio3.py
from block import Block


def verifica_blockchain(fname="blockchain.dat"):
    with open(fname, "rb") as f:
        blocks = []
        while chunk := f.read(80):
            blocks.append(Block.parse(chunk))

    for i in range(1, len(blocks)):
        print(f"Controllo blocco {i}")
        if blocks[i].prev_block != blocks[i - 1].block_id():
            print(f"Errore al blocco {i}: prev_block errato")
            return False
        if int(blocks[i].block_id().hex(), 16) > blocks[i].target():
            print(f"Errore al blocco {i}: block_id > target")
            return False
    print("La catena è valida secondo i criteri dell'esercizio 1")
    return True


def proof_of_work(fname="blockchain.dat"):
    with open(fname, "rb") as f:
        blocks = []
        while chunk := f.read(80):
            blocks.append(Block.parse(chunk))
    if verifica_blockchain():
        pow_sum = 0
        for b in blocks:
            pow_sum += 2**256 // (b.target() + 1)
        print(f"Proof-of-Work della catena: {pow_sum}")
        return pow_sum
    else:
        print("BlockChain non valida, quindi no PoW")


if __name__ == "__main__":
    proof_of_work()
