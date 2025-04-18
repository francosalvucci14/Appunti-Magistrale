from io import BytesIO
import json
import helpers  # type: ignore


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

    def serialize(self):
        # Serialize the transaction to bytes
        bs = BytesIO()
        bs.write(self.version.to_bytes(4, "little"))

        # Write the number of inputs
        bs.write(helpers.int2varint(len(self.inputs)))

        # Write each input
        for txin in self.inputs:
            bs.write(txin.prevtx[::-1])
            bs.write(txin.prevtxidx.to_bytes(4, "little"))
            bs.write(helpers.int2varint(len(txin.scriptsig)))
            bs.write(txin.scriptsig)
            bs.write(txin.sequence.to_bytes(4, "little"))

        # Write the number of outputs
        bs.write(helpers.int2varint(len(self.outputs)))

        # Write each output
        for txout in self.outputs:
            bs.write(txout.value.to_bytes(8, "little"))
            bs.write(helpers.int2varint(len(txout.scriptpk)))
            bs.write(txout.scriptpk)
        # Write the locktime
        bs.write(self.locktime.to_bytes(4, "little"))
        return bs.getvalue()


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
            "scriptsig": self.scriptsig.hex(),
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
        scriptsig = bs.read(scriptsig_len)

        # 5. Read the sequence number (4 bytes)
        sequence = int.from_bytes(bs.read(4), "little")

        return cls(prevtx, prevtxidx, scriptsig, sequence)

    def serialize(self):
        # Serialize the input to bytes
        bs = BytesIO()
        bs.write(self.prevtx[::-1])
        bs.write(self.prevtxidx.to_bytes(4, "little"))
        bs.write(helpers.int2varint(len(self.scriptsig)))
        bs.write(self.scriptsig)
        bs.write(self.sequence.to_bytes(4, "little"))
        return bs.getvalue()


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
        scriptpk = bs.read(scriptpk_len)

        return cls(value, scriptpk)

    # questo serve perchè TxOUT non è JSON serializzabile
    def __str__(self):
        out = {"value": self.value, "scriptpk": self.scriptpk.hex()}
        return json.dumps(out, indent=4)

    def serialize(self):
        # Serialize the output to bytes
        bs = BytesIO()
        bs.write(self.value.to_bytes(8, "little"))
        bs.write(helpers.int2varint(len(self.scriptpk)))
        bs.write(self.scriptpk)
        return bs.getvalue()


if __name__ == "__main__":
    # Example usage
    with open("tx1.txt", "r") as f:
        txhex = f.read()
    # print(f"Transaction Hex: {txhex}")
    bs = BytesIO(bytes.fromhex(txhex))
    tx = TX.parse(bs)
    print(tx)
    print(f"Serialized Transaction: {tx.serialize().hex()}")

# scrivere programma che prende una transazione e torna a ritroso fino alla coinbase transaction
