class ModularSignatureMethod:
    def generate_key_pair(self) -> bytes | bytes:
        pass

    def sign(self, msg_hash: str, private_key: bytes) -> bytes:
        pass

    def verify(self, msg_hash: str, public_key: bytes, signature: bytes) -> bool:
        pass