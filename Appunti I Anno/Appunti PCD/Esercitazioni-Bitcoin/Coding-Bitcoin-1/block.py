import helpers  # type: ignore
from io import BytesIO


class Block:

    def __init__(self, version, prev_block, merkle_root, timestamp, bits, nonce):
        self.version = version  # 4 bytes (int)
        self.prev_block = prev_block  # 32 bytes (bytes)
        self.merkle_root = merkle_root  # 32 bytes (bytes)
        self.timestamp = timestamp  # 4 bytes (int)
        self.bits = bits  # 4 bytes (bytes)
        self.nonce = nonce  # 4 bytes (int)

    @classmethod
    def parse(cls, bytes_sequence):
        """Prende in input una sequenza di 80 byte e restituisce un oggetto
        della classe Block"""
        r = BytesIO(bytes_sequence)
        version = int.from_bytes(r.read(4), "little")
        prev_block = r.read(32)[::-1]
        merkle_root = r.read(32)[::-1]
        timestamp = int.from_bytes(r.read(4), "little")
        bits = r.read(4)[::-1]
        nonce = int.from_bytes(r.read(4), "little")
        return cls(version, prev_block, merkle_root, timestamp, bits, nonce)

    def __str__(self):
        version = "version: " + str(self.version)
        prev_block = "prev_block: " + self.prev_block.hex()
        merkle_root = "merkle_root: " + self.merkle_root.hex()
        timestamp = "timestamp: " + str(self.timestamp)
        bits = "bits: " + self.bits.hex()
        nonce = "nonce: " + str(self.nonce)
        return "\n".join([version, prev_block, merkle_root, timestamp, bits, nonce])

    def serialize(self):
        """Restituisce la sequenza di byte serializzata che codifica il blocco"""
        return (
            self.version.to_bytes(4, "little")
            + self.prev_block[::-1]
            + self.merkle_root[::-1]
            + self.timestamp.to_bytes(4, "little")
            + self.bits[::-1]
            + self.nonce.to_bytes(4, "little")
        )

    def block_id(self):
        """L'id del blocco è il suo hash256 in little endian"""
        return helpers.hash256(self.serialize())[::-1]

    def target(self):
        """Il target si calcola dai 'bits' con la formula
        coeff * 256^(exp - 3)
        dove 'exp' è il primo byte dei 'bits' e 'coeff' e l'intero contenuto
        negli altri tre byte in little endian
        """
        exponent = self.bits[0]
        coefficient = int.from_bytes(self.bits[1:], "little")
        return coefficient * 256 ** (exponent - 3)

    def update_nonce(self, nonce):
        self.nonce = nonce

    def update_timestamp(self, timestamp):
        self.timestamp = timestamp

    def write(self, fname):
        """Scrive sul file binario 'fname' il blocco serializzato, appendendolo
        al contenuto attuale di fname"""
        with open(fname, "ab") as f:
            f.write(self.serialize())


if __name__ == "__main__":
    # L'header del 'genesis block' di Bitcoin
    GENESIS = "01000000000000000000000000000000000000000000000000000000000000\
               00000000003ba3edfd7a7b12b27ac72c3e67768f617fc81bc3888a51323a9f\
               b8aa4b1e5e4a29ab5f49ffff001d1dac2b7c"

    print("Blocco numero : 0 [GENESIS]")
    # Scrive a video il genesis block
    bytes_sequence = bytes.fromhex(GENESIS)
    b = Block.parse(bytes_sequence)
    print("block_id: ", b.block_id().hex())
    print(b)

    # Prepara i dati da inserire nei nuovi blocchi
    version = b.version
    bits = bytes.fromhex("1e00ffff")  # Target aumentato per testare più
    # rapidamente la creazione dei blocchi
    merkle_root = helpers.hash256(
        b"Principles of Cryptocurrency Design - \
                                    aa 24/25"
    )

    i = 1

    while True:
        # Aggiunge blocchi alla catena
        prev_block = b.block_id()
        timestamp = helpers.now()
        nonce = 0
        print(f"\nBlocco numero : {i}")
        b = Block(version, prev_block, merkle_root, timestamp, bits, nonce)
        while int(b.block_id().hex(), 16) > b.target():
            nonce += 1
            if nonce == 2**32:
                # Il nonce è di 4 byte, quando arriva al limite si ricomincia
                # con un nuovo timestamp
                nonce = 0
                b.update_timestamp(helpers.now())
            b.update_nonce(nonce)
        # Quando trova un blocco il cui hash è al di sotto del target lo scrive
        # a video e lo appende al file 'blockchain.dat'

        print("\nblock_id: " + b.block_id().hex())
        print(b)
        b.write("blockchain.dat")
        i += 1
