# smart_contracts/artifacts/reputation/reputation_client.py

from algokit_utils import ApplicationClient
from algosdk.v2client.algod import AlgodClient
from algosdk.v2client.indexer import IndexerClient
from algosdk.future.transaction import ApplicationNoOpTxn

class ReputationClient(ApplicationClient):
    def __init__(self, algod_client: AlgodClient, creator, indexer_client: IndexerClient):
        super().__init__(algod_client, creator, indexer_client)
        self.app_id = None  # Will be set upon deployment

    def initialize_reputation(self, reputation: int):
        # Example method to initialize reputation
        return self.call_app(
            "initialize_reputation",
            reputation,
        )

    def increase_reputation(self, user: str, amount: int):
        # Example method to increase reputation
        return self.call_app(
            "increase_reputation",
            user,
            amount,
        )

    def decrease_reputation(self, user: str, amount: int):
        # Example method to decrease reputation
        return self.call_app(
            "decrease_reputation",
            user,
            amount,
        )

    def get_reputation(self, user: str) -> int:
        # Example method to get reputation
        return self.query_app(
            "get_reputation",
            user,
        )
