# TEST 01, 02, 07, 08

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

# TEST 01, 07 => sign_alg_1
# TEST 02, 08 => sign_alg_2
sign_method = modular_signature.get_signature_method(sign_alg_1)

print("------------ Key-pair generation test ------------")

n = 100
times = []
success_count = 0

for i in range(n):
    start_time = None
    end_time = None
    try:
        start_time = time.time()
        node = Node(sign_method)
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
