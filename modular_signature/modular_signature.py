from modular_signature.signature_algorithm import SignatureAlgorithm
from modular_signature.modular_signature_method import ModularSignatureMethod


class ModularSignature:
    def __init__(self):
        self.__signature_methods = {}

    def add_signature_method(self, alg: SignatureAlgorithm, method: ModularSignatureMethod) -> None:
        self.__signature_methods[alg] = method

    def get_signature_method(self, alg: SignatureAlgorithm) -> ModularSignatureMethod:
        return self.__signature_methods[alg]
