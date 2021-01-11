# etherscan.io API
from etherscan import Etherscan
from etherscan_credentials import etherscanApikey

# etherscan.io personal API key
auth = Etherscan(etherscanApikey)


# call etherscan.io gas oracle
gasOni = auth.get_gas_oracle
print(f'Current Gas Prices', {gasOni})
print()

# Wallet Address variable
erc20Wallet = "0xddbd2b932c763ba5b1b7ae3b362eac3e8d40121a"


# get balance for wallet address
walletBalance = auth.get_eth_balance(address=erc20Wallet)
print(f'Eth Balance:', {walletBalance})
