from os import urandom

from ellipticcurve.privateKey import PrivateKey
from pyspx import haraka_256f

from modular_signature.signature_algorithm import SignatureAlgorithm


class KeyGenerator:
    def __init__(
        self,
        algorithm: SignatureAlgorithm,
    ):
        if algorithm == SignatureAlgorithm.sphincs_plus:
            seed = urandom(haraka_256f.crypto_sign_SEEDBYTES)
            public_key, private_key = haraka_256f.generate_keypair(seed)
        else:
            private_key = PrivateKey()
            public_key = private_key.publicKey()

        self.__public_key = public_key
        self.__private_key = private_key

    def get_public_key(self):
        return self.__public_key

    def get_private_key(self):
        return self.__private_key
