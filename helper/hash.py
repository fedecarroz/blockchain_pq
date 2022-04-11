from hashlib import sha3_512


def calculate_hash(message: str) -> str:
    hash_func = sha3_512()
    hash_func.update(bytes(message, "utf-8"))
    return hash_func.hexdigest()
