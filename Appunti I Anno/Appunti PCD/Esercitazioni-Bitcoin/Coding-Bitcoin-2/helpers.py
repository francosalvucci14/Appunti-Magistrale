import hashlib
from datetime import datetime

# from io import BytesIO


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


# Esercizio 1
def int2varint(i):
    if i < 0xFD:  # <256
        return i.to_bytes(1, "little")
    elif i <= 0xFFFF:  # = 253
        return b"\xfd" + i.to_bytes(2, "little")
    elif i <= 0xFFFFFFFF:  # = 254
        return b"\xfe" + i.to_bytes(4, "little")
    return b"\xff" + i.to_bytes(
        8, "little"
    )  # = 255, qua solo se non va in nessuno dei casi precedenti


def satoshi_to_btc(satoshi):
    return satoshi / 100_000_000


def doublesha256(b: bytes) -> bytes:
    return hashlib.sha256(hashlib.sha256(b).digest()).digest()
