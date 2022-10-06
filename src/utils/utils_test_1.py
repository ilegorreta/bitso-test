def get_bitso_markets(cg):
    """Retrieves all market tickers based on Bitso exchanger
        by calling the get_exchanges_tickers_by_id endpoint

    Args:
        cg: CoinGeckoAPI object

    Returns:
        bitso_markets: Dictionary of Dictionaries:
            - Key: Market's base coin
            - Value: Dictionary with the following keys:
                - id: String containg coin's ID
                - targets: List containing market's targets coin/currency
    """
    bitso_markets = {}
    exchanges_tickers = cg.get_exchanges_tickers_by_id("bitso", page=1)
    for market in exchanges_tickers["tickers"]:
        base = market["coin_id"]
        target = market["target"]
        if base in bitso_markets.keys():
            bitso_markets[base]["id"] = market["base"]
            bitso_markets[base]["targets"].append(target)
        else:
            bitso_markets[base] = {"targets": [target]}
    return bitso_markets


def get_all_exchange_markets(cg, bitso_markets):
    """Loops through the base coin's from Bitso's markets
        and retrieves all markets related on other exchanges
        by calling the get_coin_ticker_by_id endpoint

    Args:
        cg: CoinGeckoAPI object
        bitso_markets: Dictionary of Dictionaries:
            - Key: Market's base coin
            - Value: Dictionary with the following keys:
                - id: String containg coin's ID
                - targets: List containing market's targets coin/currency
    Returns:
        exchange_markets: List of tuples containing 3 elements each
            - exchange_id
            - base
            - target
    """
    # Starts as a set to avoid having duplicates
    exchange_markets = set()
    cont = 1
    for market in bitso_markets.keys():
        if market != "ethereum":
            continue
        # Starts pagination logic
        while True:
            print(f"Coin: {market}; page: {cont}:")
            coin_tickers = cg.get_coin_ticker_by_id(market, page=cont)
            # Get-out logic for pagination
            if len(coin_tickers["tickers"]) == 0:
                break
            for ticker in coin_tickers["tickers"]:
                if (
                    ticker["coin_id"] in bitso_markets.keys()
                    and ticker["target"] in bitso_markets[ticker["coin_id"]]["targets"]
                ):
                    exchange_markets.add(
                        (
                            ticker["market"]["identifier"],
                            ticker["base"],
                            ticker["target"],
                        )
                    )
            cont += 1
    # Converts back to list in order to be able to convert into dataframe
    exchange_markets = list(exchange_markets)
    return exchange_markets


def get_exchanges_list(cg):
    """List all exchanges

    Args:
        cg: CoinGeckoAPI object
    Returns:
        exchanges_list: List of containing all exchanges in Coingecko API
    """
    return cg.get_exchanges_list()
