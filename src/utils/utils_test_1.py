#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class CustomException(Exception):
    """Base class for other exceptions regarding Bitso Sr. Data Engineer Challenge"""

    pass


class ExchangeIdException(CustomException):
    """Raised when the exchange id is not recognized by CoinGecko"""

    pass


class ExchangeMarketsException(CustomException):
    """Raised when the base coin's from Bitso's markets are null"""

    pass


class ExchangeListException(CustomException):
    """Raised when the CoinGeckoAPI object is not well defined and not able to return list of exchanges"""

    pass


class DfPathException(CustomException):
    """Raised when path to save the Pandas DF is not valid"""

    pass


def get_bitso_markets(cg, exchange):
    """Retrieves all market tickers based on Bitso exchanger
        by calling the get_exchanges_tickers_by_id endpoint

    Args:
        cg: CoinGeckoAPI object
        exchange: Exchange ID

    Returns:
        bitso_markets: Dictionary of Dictionaries:
            - Key: Market's base coin
            - Value: Dictionary with the following keys:
                - id: String containg coin's ID
                - targets: List containing market's targets coin/currency
    """
    bitso_markets = {}
    try:
        exchanges_tickers = cg.get_exchanges_tickers_by_id(exchange, page=1)
    except ValueError as e:
        raise ExchangeIdException(f"Invalid exchange ID: {exchange}")
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
            try:
                coin_tickers = cg.get_coin_ticker_by_id(market, page=cont)
                # Get-out logic for pagination
                if len(coin_tickers["tickers"]) == 0:
                    break
                for ticker in coin_tickers["tickers"]:
                    if (
                        ticker["coin_id"] in bitso_markets.keys()
                        and ticker["target"]
                        in bitso_markets[ticker["coin_id"]]["targets"]
                    ):
                        exchange_markets.add(
                            (
                                ticker["market"]["identifier"],
                                ticker["base"],
                                ticker["target"],
                            )
                        )
                cont += 1
            except ValueError as e:
                raise ExchangeMarketsException(f"Invalid Coin ID: {market}")
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
    try:
        return cg.get_exchanges_list()
    except AttributeError as e:
        raise ExchangeListException("Invalid CoinGeckoAPI object")


def save_df_to_csv(df, path):
    try:
        df.to_csv(
            path,
            index=False,
            index_label=False,
        )
    except Exception as e:
        raise DfPathException("Invalid path to save DF")
