from helpers.key_generator import KeyGenerator
from modular_signature.signature_algorithm import SignatureAlgorithm


class Node:
    def __init__(
        self,
        algorithm: SignatureAlgorithm,
    ):
        self.__key_gen = self.__init_key_gen(algorithm)
        self.__secret_key = self.__key_gen.get_private_key()
        self.__wallet_address = self.__key_gen.get_public_key()

    def __init_key_gen(self, algorithm: SignatureAlgorithm):
        return KeyGenerator(algorithm)

    def get_secret_key(self):
        return self.__secret_key

    def get_wallet_address(self):
        return self.__wallet_address
