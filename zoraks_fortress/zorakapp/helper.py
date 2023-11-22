import hashlib
from typing import Union

def get_hash_index(index: Union[str, int], length:int) -> str:
    hashed = hashlib.sha256(str(index).encode()).hexdigest()
    return hashed[:length]


