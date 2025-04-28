from io import BytesIO
import json
import helpers
from script import Script
import os


class TX:
    def __init__(self, version, inputs, outputs, locktime):
        self.version = version  # primi 4 bytes, int
        self.inputs = inputs  # var len, array
        self.outputs = outputs  # var len, array
        self.locktime = locktime  # ultimi 4 bytes, int

    def __str__(self):
        out = {
            "version": self.version,
            "inputs": [txin.__str__() for txin in self.inputs],
            "outputs": [txout.__str__() for txout in self.outputs],
            "locktime": self.locktime,
        }
        return json.dumps(out, indent=4)

    @classmethod
    def parse(cls, bs):
        # Parse the transaction from the raw bytes

        # 1. Read the version (4 bytes)
        version = int.from_bytes(bs.read(4), "little")  # bs is a byte stream

        # 2 . Read the inputs
        ninput = helpers.varint2int(bs)
        inputs = [TxIN.parse(bs) for _ in range(ninput)]

        # # 3. Read the outputs
        num_outputs = helpers.varint2int(bs)
        outputs = [TxOUT.parse(bs) for _ in range(num_outputs)]

        # 4. Read the locktime (4 bytes)
        locktime = int.from_bytes(bs.read(4), "little")

        # 5. Create the transaction object
        transaction = cls(version, inputs, outputs, locktime)
        return transaction


class TxIN:
    def __init__(self, prevtx, prevtxidx, scriptsig, sequence):
        self.prevtx = prevtx  # 32 bytes, hash of the previous transaction
        self.prevtxidx = (
            prevtxidx  # 4 bytes, index of the output in the previous transaction, int
        )
        self.scriptsig = scriptsig  # var len, script signature, bytes
        self.sequence = sequence  # 4 bytes, sequence number, int

    # questo serve perchè TxIn non è JSON serializzabile
    def __str__(self):
        out = {
            "prevtx": self.prevtx.hex(),
            "prevtxidx": self.prevtxidx,
            "scriptsig": str(self.scriptsig),
            "sequence": self.sequence,
        }
        return json.dumps(out)

    @classmethod
    def parse(cls, bs):
        # Parse the input from the raw bytes

        # 1. Read the previous transaction hash (32 bytes)
        prevtx = bs.read(32)[::-1]  # Reverse the byte order

        # 2. Read the previous transaction index (4 bytes)
        prevtxidx = int.from_bytes(bs.read(4), "little")

        # 3. Read the script signature length
        scriptsig_len = helpers.varint2int(bs)

        # 4. Read the script signature
        scriptsig = Script.parse(bs.read(scriptsig_len))

        # 5. Read the sequence number (4 bytes)
        sequence = int.from_bytes(bs.read(4), "little")

        return cls(prevtx, prevtxidx, scriptsig, sequence)


class TxOUT:
    def __init__(self, value, scriptpk):
        self.value = value  # 8 bytes, int
        self.scriptpk = scriptpk  # var len, script public key, bytes

    @classmethod
    def parse(cls, bs):
        # Parse the output from the raw bytes

        # 1. Read the value (8 bytes)
        value = int.from_bytes(bs.read(8), "little")

        # 2. Read the script public_key length
        scriptpk_len = helpers.varint2int(bs)

        # 3. Read the script public_key
        scriptpk = Script.parse(bs.read(scriptpk_len))

        return cls(value, scriptpk)

    # questo serve perchè TxOUT non è JSON serializzabile
    def __str__(self):
        out = {
            "value": helpers.satoshi_to_btc(self.value),
            "scriptpk": str(self.scriptpk),
        }
        return json.dumps(out, indent=4)


if __name__ == "__main__":
    # find all files in the current directory that start with "tx"
    # and end with ".txt"
    NUM_TXT = [
        f
        for f in os.listdir(".")
        if os.path.isfile(f) and f.startswith("tx") and f.endswith(".txt")
    ]
    NUM_TXT = sorted(NUM_TXT, key=lambda x: int(x.split(".")[0][2:]))
    count_p2pk = 0
    count_p2pkh = 0
    count_unk = 0
    for i in range(len(NUM_TXT)):
        file = NUM_TXT[i]
        print(f"Parsing {file}...\n")
        # Example usage
        with open(file, "r") as f:
            txhex = f.read()

        bs = BytesIO(bytes.fromhex(txhex))
        tx = TX.parse(bs)
        print(tx)
        for j in range(len(tx.outputs)):
            print(f"Output {j} -> Script type:", tx.outputs[j].scriptpk.get_type())
            if tx.outputs[j].scriptpk.get_type() == "P2PK":
                count_p2pk += 1
            elif tx.outputs[j].scriptpk.get_type() == "P2PKH":
                count_p2pkh += 1
            else:
                count_unk += 1
        f.close()
    print(f"\nTotal transactions: {len(NUM_TXT)}")
    print(f"Total p2pk: {count_p2pk}")
    print(f"Total p2pkh: {count_p2pkh}")
    print(f"Total unknown: {count_unk}")
    # with open('transaction_2.txt', 'r') as f2:
    #    txhex2 = f2.read()
    # bs2 = BytesIO(bytes.fromhex(txhex2))
    # tx2 = TX.parse(bs2)
    # print(tx2)
