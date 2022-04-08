from typing import List

from helper import Timestamp, calculate_hash

from models.transaction import Transaction


class Block:
    def __init__(
        self,
        transactions: List[Transaction],
        previous_hash: str,
        nonce: int = 0,
    ):
        self.__transactions = transactions
        self.__previous_hash = previous_hash
        self.__nonce = nonce
        self.__timestamp = Timestamp.unix_time_millis_now()

        message = str(
            str(self.__timestamp)
            + self.__transactionListToString(self.__transactions)
            + self.__previous_hash
            + str(self.__nonce)
        )

        self.__hash = calculate_hash(message=message)

    def get_transactions(self):
        return self.__transactions

    def get_previous_hash(self):
        return self.__previous_hash

    def get_message(self) -> str:
        return str(
            str(self.__timestamp)
            + self.__transactionListToString(self.__transactions)
            + self.__previous_hash
            + str(self.__nonce)
        )

    def get_hash(self):
        return self.__hash

    def mine_block(self, difficulty: int):
        self.__hash = calculate_hash(self.get_message())

        zeros = "0" * difficulty
        while not (self.__hash.startswith(zeros)):
            self.__nonce += 1
            self.__hash = calculate_hash(self.get_message())

        print("Block mined: " + str(self.__hash))

    def has_valid_transactions(self) -> bool:
        for tx in self.__transactions:
            if not (tx.is_valid()):
                return False
        return True

    def __transactionListToString(self, list: List[Transaction]) -> str:
        temp = ""
        for element in list:
            temp += element.get_message()
        return temp
