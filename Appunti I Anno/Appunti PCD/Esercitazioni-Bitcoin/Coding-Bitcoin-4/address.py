from ecdsa import SigningKey, SECP256k1
import random
import helpers
import base58


class Address:
    def __init__(self, sk_string):
        self.sk = SigningKey.from_string(sk_string, curve=SECP256k1)

    def get_public_key(self, compressed=True):
        pk = self.sk.verifying_key.to_string()
        if not compressed:
            return b"\x04" + pk
        x, y = pk[:32], pk[32:]
        prefix = b"\x03" if y[-1] & 1 else b"\x02"  # 0x02 for even, 0x03 for odd
        return prefix + x

    def get_addr(self, compressed=True, is_testnet=False):
        pkh = helpers.hash160(self.get_public_key(compressed))
        prefix = b"\x6f" if is_testnet else b"\x00"
        checksum = helpers.hash256(prefix + pkh)[:4]  # [:4] to get the first 4 bytes
        return base58.b58encode(prefix + pkh + checksum)
    
    def wif(self, compressed = True, is_testnet = False):
        prefix = b'\xef' if is_testnet else b'\x80'
        suffix = b'\x01' if compressed else b''
        sk_string = prefix + self.sk.to_string() + suffix
        checksum = helpers.hash256(sk_string)[:4]
        return base58.b58encode(sk_string + checksum)


# Generate a random private key
r = random.randint(1, 2**256 - 1)
#r_prof = 10320262719635546425971816813685186004542889972915619493199054240878747601072
sk_string = r.to_bytes(32, "big")
addr = Address(sk_string)

print(f"r = {r}")
print(f"sk_string = {sk_string.hex()}")

pk = addr.get_public_key()
print(f"pk [compressed]= {pk.hex()}")

pk2 = addr.get_public_key(compressed=False)
print(f"pk [uncompressed]= {pk2.hex()}")

x, y = pk2[:32], pk2[32:]
print(f"\t1 - pk.x = {x.hex()}")
print(f"\t2 - pk.y = {y.hex()}\n")

print(f"BTC Address [Compressed] : {addr.get_addr()}")
print(f"BTC Address [TESTNET] : {addr.get_addr(is_testnet=True)}\n")

print(f"WIF [Compressed]: {addr.wif()}")
print(f"WIF [TESNET]: {addr.wif(compressed=False,is_testnet=True)}")
print(f"WIF [Compress + TESNET]: {addr.wif(is_testnet=True)}")
