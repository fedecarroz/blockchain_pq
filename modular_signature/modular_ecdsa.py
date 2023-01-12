from modular_signature.modular_signature_method import ModularSignatureMethod
from ellipticcurve.ecdsa import Ecdsa, Signature
from ellipticcurve.privateKey import PrivateKey
from ellipticcurve.publicKey import PublicKey


class ModularECDSA(ModularSignatureMethod):
    def generate_key_pair(self):
        sk = PrivateKey()
        pk = sk.publicKey()

        return pk.toDer(), sk.toDer()

    def sign(self, msg_hash: str, private_key: bytes) -> bytes:
        priv_key = PrivateKey.fromDer(private_key)
        signature: Signature = Ecdsa.sign(msg_hash, priv_key)
        return signature.toDer()

    def verify(self, msg_hash: str, public_key: bytes, signature: bytes) -> bool:
        pub_key = PublicKey.fromDer(public_key)
        sign = Signature.fromDer(signature)
        return Ecdsa.verify(msg_hash, sign, pub_key)
