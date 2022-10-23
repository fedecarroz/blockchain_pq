from helper import *
from models import *

# Define signature algorithm (sphincs_plus / ecdsa)
# this is for comparison purpose:
#    SPHINCS+  -> quantum safe
#    ECDSA     -> not quantum safe
sig_algorithm = SignatureAlgorithm.sphincs_plus

# Nodes creation
node_1 = Node(sig_algorithm)
node_2 = Node(sig_algorithm)

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
    algorithm=sig_algorithm,
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
    algorithm=sig_algorithm,
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
    algorithm=sig_algorithm,
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

# Print all informations about one product
print("\nInformation about PRODUCT 1:")
infos = bc.get_product_information(product_1_id)
for info in infos:
    print(info.get_information())

# Check blockchain validity
if bc.is_chain_valid():
    print("\nThe chain is valid.\n")
else:
    print("\nThe chain is not valid!\n")

selected_algorithm = "The selected signature algorithm is {}."
print(selected_algorithm.format(sig_algorithm.value))

# Check if blockchain is quantum resistant
if sig_algorithm == SignatureAlgorithm.sphincs_plus:
    print("The blockchain is quantum resistant.")
else:
    print("The blockchain is not quantum resistant!")
