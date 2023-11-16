import hashlib


def get_hash_index(index, length):
    hashed = hashlib.sha256(str(index).encode()).hexdigest()
    return hashed[:length]
