import hashlib
from configparser import ConfigParser
from Crypto.Hash import RIPEMD160


def hash256(msg):
    return hashlib.sha256(hashlib.sha256(msg).digest()).digest()

def hash160(msg):
    ripemd160 = RIPEMD160.new()
    ripemd160.update(hashlib.sha256(msg).digest())
    return ripemd160.digest()

if __name__ == '__main__':
    x = b'Franco'
    print(f"hash256(x) = {hash256(x).hex()}")
    print(f"hash160(x) = {hash160(x).hex()}")