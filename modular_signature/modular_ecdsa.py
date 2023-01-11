from modular_signature.modular_signature_method import ModularSignatureMethod
from ellipticcurve.ecdsa import Ecdsa, Signature
from ellipticcurve.privateKey import PrivateKey


class ModularECDSA(ModularSignatureMethod):
    def generate_key_pair(self):
        sk = PrivateKey()
        pk = sk.publicKey()

        return pk.toDer(), sk.toDer()

    def sign(self, msg_hash: str, private_key: bytes) -> bytes:
        signature: Signature = Ecdsa.sign(msg_hash, private_key)
        return signature.toDer()

    def verify(self, msg_hash: str, public_key: bytes, signature: bytes) -> bool:
        return Ecdsa.verify(msg_hash, signature, public_key)
