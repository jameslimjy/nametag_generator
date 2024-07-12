import pandas as pd

data = {
    'name': [
        'Alice Maria Johnson', 'Robert Smith', 'Carol White', 
        'David Benjamin Brown', 'Evelyn Alexandra Davis', 'Franklin Theodore Wilson', 
        'Grace Elizabeth Lee', 'Henry Michael Thompson', 'Ivy Gabriella Martinez', 
        'Jackson William Anderson', 'Karen Walker', 'Lawrence Anthony Scott', 
        'Mona Isabelle Harris', 'Nina Catherine Lewis', 'Oscar Jonathan Clark', 
        'Paul Alexander Martinez', 'Quincy Nathaniel Adams', 'Rachel Emily Young', 
        'Samuel Gregory Peterson', 'Tina Kimberly Rogers'
    ],
    'occupation': [
        'Blockchain Developer', 'Smart Contract Auditor', 'DeFi Product Manager', 
        'Crypto Community Manager', 'NFT Artist', 'DAO Operations Coordinator', 
        'Web3 Research Analyst', 'Metaverse Architect', 'Decentralized Finance Advisor', 
        'Cryptocurrency Trader', 'Blockchain Consultant', 'Web3 Project Lead', 
        'Tokenomics Expert', 'Blockchain Infrastructure Engineer', 'Web3 Ecosystem Manager', 
        'Smart Contract Developer', 'DeFi Protocol Engineer', 'Crypto Marketing Strategist', 
        'Blockchain Legal Advisor', 'Crypto Venture Capitalist'
    ],
    'organization': [
        'Chainlink Labs', 'Uniswap Foundation', 'Aave Protocol', 
        'OpenSea Marketplace', 'CryptoPunks Collective', 'MakerDAO Organization', 
        'Telegram Open Network Foundation', 'Decentraland Inc.', 'SushiSwap Treasury', 
        'Binance Exchange', 'ConsenSys Solutions', 'Web3 Foundation', 
        'Ethereum Foundation', 'Solana Labs', 'Avalanche Research Group', 
        'Algorand Association', 'Polkadot Network', 'Cardano', 
        'Stellar Development Foundation', 'Ripple Labs'
    ]
}

df = pd.DataFrame(data)
df.to_csv('nametag_input_data.csv', index=False)
