from modular_signature.modular_signature_method import ModularSignatureMethod
from os import urandom
from pyspx import haraka_256f


class ModularSPHINCSPLUS(ModularSignatureMethod):
    def generate_key_pair(self) -> bytes | bytes:
        seed = urandom(haraka_256f.crypto_sign_SEEDBYTES)
        return haraka_256f.generate_keypair(seed)

    def sign(self, msg_hash: str, private_key: bytes) -> bytes:
        return haraka_256f.sign(bytes(msg_hash, "utf-8"), private_key)

    def verify(self, msg_hash: str, public_key: bytes, signature: bytes) -> bool:
        return haraka_256f.verify(bytes(msg_hash, "utf-8"), signature, public_key)
