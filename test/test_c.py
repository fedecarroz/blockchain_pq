# TEST 05, 06, 11, 12

import time
import numpy as np
from models import *
from modular_signature import *

modular_signature = ModularSignature()
modular_signature.add_signature_method(
    SignatureAlgorithm.ecdsa,
    ModularECDSA(),
)
modular_signature.add_signature_method(
    SignatureAlgorithm.sphincs_plus,
    ModularSPHINCSPLUS(),
)

sign_alg_1 = SignatureAlgorithm.ecdsa
sign_alg_2 = SignatureAlgorithm.sphincs_plus

# TEST 05, 11 => sign_alg_1
# TEST 06, 12 => sign_alg_2
sign_method = modular_signature.get_signature_method(sign_alg_2)

print("------------ Signature verification test ------------")

node_1 = Node(sign_method)
node_2 = Node(sign_method)

product_id = "test_id"

pow_difficulty = 3
bc = Blockchain(pow_difficulty)

n = 100
times = []
success_count = 0

for i in range(n):
    start_time = None
    end_time = None
    try:
        tx = Transaction(
            from_address=node_1.get_wallet_address(),
            to_address=node_2.get_wallet_address(),
            product_id=product_id,
            information="Product information",
            sign_method=sign_method,
        )
        tx.sign_transaction(
            private_key=node_1.get_secret_key(),
            public_key=node_1.get_wallet_address(),
        )
        start_time = time.time()
        bc.add_transaction(tx=tx)
        end_time = time.time()
        success_count += 1
        print(f"TEST {i + 1}/{n} PASSED")
    except:
        end_time = time.time()
        print(f"TEST {i + 1}/{n} NOT PASSED")
    finally:
        elapsed_time = (end_time - start_time) * 1e+6
        times.append(elapsed_time)

print(times)
times = np.array(times)

min_time = times.min()
max_time = times.max()
avg_time = times.mean()

print(f"min: {min_time} microsec, max: {max_time} microsec, avg: {avg_time} microsec")

if success_count > n * 0.8:
    print(f"\nTEST PASSED => {success_count}/{n}")
else:
    print(f"\nTEST FAILED => {success_count}/{n}")
