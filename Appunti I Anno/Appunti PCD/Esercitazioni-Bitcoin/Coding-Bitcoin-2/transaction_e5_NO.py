from io import BytesIO
import json
import requests
import helpers  # type: ignore

class TX:
    def __init__(self, version, inputs, outputs, locktime):
        self.version = version
        self.inputs = inputs
        self.outputs = outputs
        self.locktime = locktime

    def __str__(self):
        out = {
            "version": self.version,
            "inputs": [str(txin) for txin in self.inputs],
            "outputs": [str(txout) for txout in self.outputs],
            "locktime": self.locktime
        }
        return json.dumps(out, indent=4)

    def serialize(self):
        bs = BytesIO()
        bs.write(self.version.to_bytes(4, 'little'))
        bs.write(helpers.int2varint(len(self.inputs)))
        for txin in self.inputs:
            bs.write(txin.serialize())
        bs.write(helpers.int2varint(len(self.outputs)))
        for txout in self.outputs:
            bs.write(txout.serialize())
        bs.write(self.locktime.to_bytes(4, 'little'))
        return bs.getvalue()

    def txid(self):
        return helpers.doublesha256(self.serialize())[::-1].hex()

    @classmethod
    def parse(cls, bs):
        version = int.from_bytes(bs.read(4), 'little')
        ninput = helpers.varint2int(bs)
        inputs = [TxIN.parse(bs) for _ in range(ninput)]
        num_outputs = helpers.varint2int(bs)
        outputs = [TxOUT.parse(bs) for _ in range(num_outputs)]
        locktime = int.from_bytes(bs.read(4), 'little')
        return cls(version, inputs, outputs, locktime)

    @classmethod
    def from_txid(cls, txid):
        url = f"https://mempool.space/api/tx/{txid}/hex"
        response = requests.get(url)
        if response.status_code != 200:
            raise Exception(f"Errore nel recupero della transazione {txid}")
        raw = bytes.fromhex(response.text)
        return cls.parse(BytesIO(raw))

    def build_ancestor_tree(self):
        def helper(current_tx):
            children = []
            for txin in current_tx.inputs:
                prevtxid = txin.prevtx[::-1].hex()
                url = f"https://mempool.space/api/tx/{prevtxid}"
                response = requests.get(url)
                if response.status_code != 200:
                    continue
                tx_data = response.json()
                if "vin" in tx_data and "coinbase" in tx_data["vin"][0]:
                    continue
                prevtx = TX.from_txid(prevtxid)
                child_node = helper(prevtx)
                children.append(child_node)
                print(children)
            return TxTreeNode(current_tx, children)

        return helper(self)

class TxTreeNode:
    def __init__(self, tx, children=None):
        self.tx = tx
        self.children = children if children else []

    def __str__(self, level=0):
        ret = "    " * level + f"TXID: {self.tx.txid()}\n"
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret

class TxIN:
    def __init__(self, prevtx, prevtxidx, scriptsig, sequence):
        self.prevtx = prevtx
        self.prevtxidx = prevtxidx
        self.scriptsig = scriptsig
        self.sequence = sequence

    def __str__(self):
        out = {
            "prevtx": self.prevtx.hex(),
            "prevtxidx": self.prevtxidx,
            "scriptsig": self.scriptsig.hex(),
            "sequence": self.sequence
        }
        return json.dumps(out)

    def serialize(self):
        bs = BytesIO()
        bs.write(self.prevtx[::-1])
        bs.write(self.prevtxidx.to_bytes(4, 'little'))
        bs.write(helpers.int2varint(len(self.scriptsig)))
        bs.write(self.scriptsig)
        bs.write(self.sequence.to_bytes(4, 'little'))
        return bs.getvalue()

    @classmethod
    def parse(cls, bs):
        prevtx = bs.read(32)[::-1]
        prevtxidx = int.from_bytes(bs.read(4), 'little')
        scriptsig_len = helpers.varint2int(bs)
        scriptsig = bs.read(scriptsig_len)
        sequence = int.from_bytes(bs.read(4), 'little')
        return cls(prevtx, prevtxidx, scriptsig, sequence)

class TxOUT:
    def __init__(self, value, scriptpk):
        self.value = value
        self.scriptpk = scriptpk

    def __str__(self):
        out = {
            "value": self.value,
            "scriptpk": self.scriptpk.hex()
        }
        return json.dumps(out, indent=4)

    def serialize(self):
        bs = BytesIO()
        bs.write(self.value.to_bytes(8, 'little'))
        bs.write(helpers.int2varint(len(self.scriptpk)))
        bs.write(self.scriptpk)
        return bs.getvalue()

    @classmethod
    def parse(cls, bs):
        value = int.from_bytes(bs.read(8), 'little')
        scriptpk_len = helpers.varint2int(bs)
        scriptpk = bs.read(scriptpk_len)
        return cls(value, scriptpk)

if __name__ == '__main__':
    with open('tx3.txt', 'r') as f:
        txhex = f.read()
    bs = BytesIO(bytes.fromhex(txhex))
    tx = TX.parse(bs)
    print(tx)

    tree = tx.build_ancestor_tree()
