from ellipticcurve.ecdsa import Ecdsa
from helper.hash import calculate_hash
from helper.signature_algorithm import SignatureAlgorithm
from pyspx import shake256_256f


class Transaction:
    def __init__(
        self,
        from_address,
        to_address,
        product_id: str,
        information: str,
        algorithm: SignatureAlgorithm,
    ):
        self.__from_address = from_address
        self.__to_address = to_address
        self.__product_id = product_id
        self.__information = information
        self.__message = (
            self.__convertKeysBytesToString(self.__from_address)
            + self.__convertKeysBytesToString(self.__to_address)
            + self.__product_id
            + self.__information
        )
        self.__algorithm = algorithm

    def get_from_address(self):
        return self.__from_address

    def get_to_address(self):
        return self.__to_address

    def get_product_id(self) -> str:
        return self.__product_id

    def get_information(self) -> str:
        return self.__information

    def get_message(self) -> str:
        return self.__message

    def sign_transaction(self, public_key, private_key):
        if public_key != self.__from_address:
            raise Exception("You cannot sign transactions for other wallets!")

        hash_tx = calculate_hash(self.__message)

        if self.__algorithm == SignatureAlgorithm.sphincs_plus:
            bytes_hash_tx = bytes(hash_tx, "utf-8")
            signature: bytes = shake256_256f.sign(bytes_hash_tx, private_key)
        else:
            signature = Ecdsa.sign(hash_tx, private_key)

        self.__signature = signature

    def is_valid(self):
        if not (self.__signature):
            raise Exception("No signature in the transaction!")

        hash_tx = calculate_hash(self.__message)

        if self.__algorithm == SignatureAlgorithm.sphincs_plus:
            bytes_hash_tx = bytes(hash_tx, "utf-8")
            verify = shake256_256f.verify(
                bytes_hash_tx,
                self.__signature,
                self.__from_address,
            )
        else:
            verify = Ecdsa.verify(
                hash_tx,
                self.__signature,
                self.__from_address,
            )

        return verify

    def __convertKeysBytesToString(self, bytes: bytes) -> str:
        temp = str(bytes)
        temp = temp[2:-1]
        return temp

    def break_transaction(self, information):
        self.__information = information
        self.__message = (
            self.__convertKeysBytesToString(self.__from_address)
            + self.__convertKeysBytesToString(self.__to_address)
            + self.__product_id
            + self.__information
        )
