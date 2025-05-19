from io import BytesIO
import json
import helpers 

class TX():
    def __init__(self,version, inputs, outputs,locktime):
        self.version = version      # primi 4 bytes, int
        self.inputs = inputs        # var len, array
        self.outputs = outputs      # var len, array
        self.locktime = locktime    # ultimi 4 bytes, int
    
    def __str__(self):
        out = {"version": self.version, "inputs": [txin.__str__() for txin in self.inputs], \
               "outputs": [txout.__str__() for txout in self.outputs], "locktime": self.locktime}
        return json.dumps(out,indent=4)
     
    @classmethod
    def parse(cls,bs): 
        # Parse the transaction from the raw bytes

        # 1. Read the version (4 bytes)
        version = int.from_bytes(bs.read(4), 'little') #bs is a byte stream

        # 2 . Read the inputs
        ninput = helpers.varint2int(bs)
        inputs = [TxIN.parse(bs) for _ in range(ninput)]
        
        # # 3. Read the outputs
        num_outputs = helpers.varint2int(bs)
        outputs = [TxOUT.parse(bs) for _ in range(num_outputs)]

        # 4. Read the locktime (4 bytes)
        locktime = int.from_bytes(bs.read(4), 'little')

        # 5. Create the transaction object
        transaction = cls(version, inputs, outputs, locktime)
        return transaction
    
    def isCoinbase(self,bs):
        if (len(self.inputs) == 1 and self.inputs[0].prevtx == bytes(32) and self.inputs[0].prevtxidx == 0xffffffff):
            return True
        return False
    
class TxIN:
    def __init__(self,prevtx,prevtxidx,scriptsig,sequence):
        self.prevtx = prevtx        # 32 bytes, hash of the previous transaction
        self.prevtxidx = prevtxidx  # 4 bytes, index of the output in the previous transaction, int
        self.scriptsig = scriptsig  # var len, script signature, bytes
        self.sequence = sequence    # 4 bytes, sequence number, int
    
    # questo serve perchè TxIn non è JSON serializzabile
    def __str__(self):
        out = {"prevtx": self.prevtx.hex(), "prevtxidx": self.prevtxidx, "scriptsig": self.scriptsig.hex(), "sequence": self.sequence}
        return json.dumps(out)

    @classmethod
    def parse(cls,bs):
        # Parse the input from the raw bytes

        # 1. Read the previous transaction hash (32 bytes)
        prevtx = bs.read(32)[::-1]  # Reverse the byte order

        # 2. Read the previous transaction index (4 bytes)
        prevtxidx = int.from_bytes(bs.read(4), 'little')

        # 3. Read the script signature length
        scriptsig_len = helpers.varint2int(bs)

        # 4. Read the script signature
        scriptsig = bs.read(scriptsig_len)

        # 5. Read the sequence number (4 bytes)
        sequence = int.from_bytes(bs.read(4), 'little')
        
        return cls(prevtx, prevtxidx, scriptsig, sequence)
    
class TxOUT:
    def __init__(self,value,scriptpk):
        self.value = value          # 8 bytes, int 
        self.scriptpk = scriptpk    # var len, script public key, bytes

    @classmethod
    def parse(cls,bs):
        # Parse the output from the raw bytes
        
        # 1. Read the value (8 bytes)
        value = int.from_bytes(bs.read(8),'little')

        # 2. Read the script public_key length
        scriptpk_len = helpers.varint2int(bs)

        # 3. Read the script public_key
        scriptpk = bs.read(scriptpk_len)

        return cls(value,scriptpk)

    # questo serve perchè TxOUT non è JSON serializzabile
    def __str__(self):
        out = {"value": helpers.satoshi_to_btc(self.value), "scriptpk": self.scriptpk.hex()}
        return json.dumps(out,indent=4)

class SegWitTx(TX): ##sottoclasse di TX
    
    def __init__(self, version, marker, flag, inputs, outputs, locktime):
        super().__init__( version, inputs, outputs, locktime)
        self.marker = marker      # 1 byte
        self.flag = flag    
          # 1 byte
    @classmethod
    def parse(cls, r):
        version = int.from_bytes(r.read(4), 'little')
        marker = r.read(1)
        flag = r.read(1)
        numin = helpers.varint2int(r)
        inputs = [TxIN.parse(r) for _ in range(numin)]
        numout = helpers.varint2int(r)
        outputs = [TxOUT.parse(r) for _ in range(numout)]
        locktime = int.from_bytes(r.read(4), 'little')
        # aggiungere parsing del Witness
        return cls( version, marker, flag, inputs, outputs, locktime)
    
    @classmethod
    def isSegWit(cls,bs):
        bs.seek(4) # Skip the version
        # Check if the first byte of the transaction is 0x00
        # If it is, then it's a SegWit transaction
        # Otherwise, it's a non-SegWit transaction
        marker = bs.read(1)
        flag = bs.read(1)
        bs.seek(0)
        if marker == b'\x00' and flag == b'\x01':
            return True
        
        return False

if __name__ == '__main__':
    # Example usage
    with open('tx_seg.txt', 'r') as f:
        txhex = f.read()
    
    bs = BytesIO(bytes.fromhex(txhex))
    if SegWitTx.isSegWit(bs):
        print("SegWit transaction")
        tx = SegWitTx.parse(bs)
        print(tx)
    else:
        print("Non-SegWit transaction")
        tx = TX.parse(bs)
        print(tx)
    print("Is coinbase: ", tx.isCoinbase(bs))