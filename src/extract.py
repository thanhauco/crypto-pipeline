def fetch_eth():
    return requests.get('https://api.coingecko.com/api/v3/simple/price?ids=ethereum').json()