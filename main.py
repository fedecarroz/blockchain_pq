from models import *
from modular_signature import *

# Init modular signature
modular_signature = ModularSignature()

# Add modular signature methods
modular_signature.add_signature_method(
    SignatureAlgorithm.ecdsa,
    ModularECDSA(),
)
modular_signature.add_signature_method(
    SignatureAlgorithm.sphincs_plus,
    ModularSPHINCSPLUS(),
)

# Select a signature method
sign_method = modular_signature.get_signature_method(SignatureAlgorithm.sphincs_plus)

# Nodes creation
node_1 = Node(sign_method)
node_2 = Node(sign_method)

# Products id
product_1_id = "prdct1"
product_2_id = "prdct2"
product_3_id = "prdct3"

# Creation of the blockchain
pow_difficulty = 3
bc = Blockchain(pow_difficulty)

# First transaction
tx1 = Transaction(
    from_address=node_1.get_wallet_address(),
    to_address=node_2.get_wallet_address(),
    product_id=product_1_id,
    information="First information",
    sign_method=sign_method,
)
# Signature of transaction with chosen signature algorithm
tx1.sign_transaction(
    private_key=node_1.get_secret_key(),
    public_key=node_1.get_wallet_address(),
)
bc.add_transaction(tx=tx1)

# Second transaction
tx2 = Transaction(
    from_address=node_1.get_wallet_address(),
    to_address=node_2.get_wallet_address(),
    product_id=product_2_id,
    information="Second information",
    sign_method=sign_method,
)
# Signature of transaction with chosen signature algorithm
tx2.sign_transaction(
    private_key=node_1.get_secret_key(),
    public_key=node_1.get_wallet_address(),
)
bc.add_transaction(tx=tx2)

# Mining first block pending transactions
print("Starting the miner...")
bc.mine_pending_transactions()

# Third transaction
tx3 = Transaction(
    from_address=node_1.get_wallet_address(),
    to_address=node_2.get_wallet_address(),
    product_id=product_3_id,
    information="Third information",
    sign_method=sign_method,
)
# Signature of transaction with chosen signature algorithm
tx3.sign_transaction(
    private_key=node_1.get_secret_key(),
    public_key=node_1.get_wallet_address(),
)
bc.add_transaction(tx=tx3)

# Mining second block pending transactions
print("Starting the miner...")
bc.mine_pending_transactions()

############################################################
#                                                          #
# Code to break the chain (uncomment to try)               #
# bc.break_chain(1, product_1_id, "Wrong information")     #
# bc.break_mining(1, node.get_secret_key())                #
#                                                          #
############################################################

# Print all information about one product
print("\nInformation about PRODUCT 1:")
infos = bc.get_product_information(product_1_id)
for info in infos:
    print(info.get_information())

# Check blockchain validity
if bc.is_chain_valid():
    print("\nThe chain is valid.\n")
else:
    print("\nThe chain is not valid!\n")