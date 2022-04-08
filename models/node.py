from helper.key_generator import KeyGenerator
from helper.signature_algorithm import SignatureAlgorithm


class Node:
    def __init__(
        self,
        algorithm: SignatureAlgorithm,
    ):
        key_gen = KeyGenerator(algorithm)
        self.__secret_key = key_gen.get_private_key()
        self.__wallet_address = key_gen.get_public_key()

    def get_secret_key(self):
        return self.__secret_key

    def get_wallet_address(self):
        return self.__wallet_address
