from web3 import Web3


def get_latest_block(node_url:str):
    w3: Web3 = Web3(Web3.HTTPProvider(node_url))
    return w3.eth.block_number
