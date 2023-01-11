from modular_signature import ModularSignatureMethod


class Node:
    def __init__(
            self,
            sign_method: ModularSignatureMethod,
    ):
        self.__wallet_address, self.__secret_key = sign_method.generate_key_pair()

    def get_secret_key(self):
        return self.__secret_key

    def get_wallet_address(self):
        return self.__wallet_address
