from helpers.hash import calculate_hash
from modular_signature import ModularSignatureMethod


class Transaction:
    def __init__(
            self,
            from_address,
            to_address,
            product_id: str,
            information: str,
            sign_method: ModularSignatureMethod,
    ):
        self.__from_address = from_address
        self.__to_address = to_address
        self.__product_id = product_id
        self.__information = information
        self.__message = (
                self.__convert_keys_bytes_to_string(self.__from_address)
                + self.__convert_keys_bytes_to_string(self.__to_address)
                + self.__product_id
                + self.__information
        )
        self.__sign_method = sign_method
        self.__signature = None

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

        self.__signature = self.__sign_method.sign(hash_tx, private_key)

    def is_valid(self):
        if not self.__signature:
            raise Exception("No signature in the transaction!")

        hash_tx = calculate_hash(self.__message)
        return self.__sign_method.verify(hash_tx, self.__from_address, self.__signature)

    def __convert_keys_bytes_to_string(self, bytes: bytes) -> str:
        temp = str(bytes)
        temp = temp[2:-1]
        return temp

    def break_transaction(self, information):
        self.__information = information
        self.__message = (
                self.__convert_keys_bytes_to_string(self.__from_address)
                + self.__convert_keys_bytes_to_string(self.__to_address)
                + self.__product_id
                + self.__information
        )
