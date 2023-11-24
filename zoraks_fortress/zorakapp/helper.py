import hashlib
from flask import redirect, Response
from typing import Union

def get_hash_index(index: Union[str, int], length:int = 5) -> str:
    hashed = hashlib.sha256(str(index).encode()).hexdigest()
    return hashed[:length]

def go_home() -> Response:
    return redirect(url_for('index')) #! BUG: Doesn't load map class