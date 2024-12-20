from typing import List

from helpers.hash import calculate_hash
from helpers.random_string_generator import get_random_string

from models.block import Block
from models.transaction import Transaction


class Blockchain:
    def __init__(
        self,
        difficulty: int,
    ):
        gen_block = self.create_genesis_block()
        self.__chain = [gen_block]
        self.__pending_transactions = []
        self.__difficulty = difficulty

    def create_genesis_block(self):
        return Block(
            transactions=[],
            previous_hash=calculate_hash(
                get_random_string(16),
            ),
        )

    def mine_pending_transactions(self):
        block = Block(
            transactions=self.__pending_transactions,
            previous_hash=self.__chain[-1].get_hash(),
        )

        if not (block.has_valid_transactions()):
            raise Exception("Block contains invalid transactions!")

        block.mine_block(self.__difficulty)
        print("Block successfully mined!")

        self.__chain.append(block)
        self.__pending_transactions = []

    def add_transaction(self, tx: Transaction):
        if not (tx.is_valid()):
            raise Exception("Cannot add invalid transaction to chain!")

        self.__pending_transactions.append(tx)

    def get_product_information(self, product_id: str):
        transactions_list: List[Transaction] = []

        for block in self.__chain:
            for transaction in block.get_transactions():
                if transaction.get_product_id() == product_id:
                    transactions_list.append(transaction)

        return transactions_list

    def is_chain_valid(self):
        for i in range(1, len(self.__chain)):
            current_block = self.__chain[i]
            previous_block = self.__chain[i - 1]

            if not (current_block.has_valid_transactions()):
                print("Not all transactions are valid!")
                return False

            curr_hash = current_block.get_hash()
            curr_calc_hash = calculate_hash(current_block.get_message())

            if curr_hash != curr_calc_hash:
                print("Invalid hash of the block!")
                return False

            curr_prev_hash = current_block.get_previous_hash()
            prev_hash = previous_block.get_hash()

            if curr_prev_hash != prev_hash:
                print("Hash linking not correct!")
                return False

        return True

    def break_chain(self, i, product_id, information):
        for tx in self.__chain[i].get_transactions():
            if tx.get_product_id() == product_id:
                tx.break_transaction(information)

    def break_mining(self, i, private_key):
        for tx in self.__chain[i].get_transactions():
            tx.sign_transaction(
                tx.get_from_address(),
                private_key,
            )

        self.__chain[i].mine_block(self.__difficulty)
