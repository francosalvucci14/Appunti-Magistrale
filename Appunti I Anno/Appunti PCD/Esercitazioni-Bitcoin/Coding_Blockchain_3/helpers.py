import hashlib
from configparser import ConfigParser
import os

def opcodes(fname):
    
    config = ConfigParser()
    config.read(fname)
    #print(config.sections())
    return {int(config['OPCODES'][x],16):x for x in config['OPCODES']}

OPCODES = opcodes("opcodes.cfg")

def hash256(msg):
    return hashlib.sha256(hashlib.sha256(msg).digest()).digest()

def varint2int(bs):
    first = int.from_bytes(bs.read(1), "little")
    if first < 0xFD:  # <256
        return first
    elif first == 0xFD:  # = 253
        return int.from_bytes(bs.read(2), "little")
    elif first == 0xFE:  # = 254
        return int.from_bytes(bs.read(4), "little")
    return int.from_bytes(
        bs.read(8), "little"
    )  # = 255, qua solo se non va in nessuno dei casi precedenti

def satoshi_to_btc(satoshi):
    return satoshi / 100_000_000

if __name__ == '__main__':
    #print(os.path.isfile("opcodes.cfg"))  # Deve stampare True
    print(opcodes("opcodes.cfg"))