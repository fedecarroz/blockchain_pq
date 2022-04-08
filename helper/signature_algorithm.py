from enum import Enum


class SignatureAlgorithm(Enum):
    ecdsa = "ECDSA"
    sphincs_plus = "SPHINCS+"
