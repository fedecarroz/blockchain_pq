from hashlib import sha3_256

def calculate_hash(message: str) -> str:
    hash_func = sha3_256()
    hash_func.update(bytes(message, "utf-8"))
    return hash_func.hexdigest()