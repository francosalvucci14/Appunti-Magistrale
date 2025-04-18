import hashlib
from datetime import datetime

def hash256(msg):
    return hashlib.sha256(hashlib.sha256(msg).digest()).digest()

def now():
    return int(datetime.now().timestamp())

