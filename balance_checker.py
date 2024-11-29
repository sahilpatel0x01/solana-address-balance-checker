from solana.rpc.async_api import AsyncClient
from solders.pubkey import Pubkey
import asyncio

# Solana cluster RPC endpoint
RPC_ENDPOINT = "https://api.mainnet-beta.solana.com"  # Mainnet
# Uncomment for Testnet or Devnet
# RPC_ENDPOINT = "https://api.testnet.solana.com"
# RPC_ENDPOINT = "https://api.devnet.solana.com"

async def get_balance(address: str) -> float:
    """
    Get the balance of a Solana address.
    :param address: Solana public address as a string
    :return: Balance in SOL as a float
    """
    async with AsyncClient(RPC_ENDPOINT) as client:
        try:
            # Convert the address to a Pubkey object
            public_key = Pubkey.from_string(address)
            # Fetch balance (in lamports)
            response = await client.get_balance(public_key)
            # Access the value attribute directly
            lamports = response.value  # `value` contains balance in lamports
            sol_balance = lamports / 1_000_000_000  # Convert lamports to SOL
            return sol_balance
        except Exception as e:
            print(f"An error occurred: {e}")
            return 0.0

# Replace this with the Solana address you want to check
solana_address = input("paste address here: ")

# Run the async function
balance = asyncio.run(get_balance(solana_address))
print(f"Balance for address {solana_address}: {balance} SOL")
