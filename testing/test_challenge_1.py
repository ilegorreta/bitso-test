#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import pytest
import pandas as pd
from pycoingecko import CoinGeckoAPI

script_dir = os.path.dirname(__file__)
mymodule_dir = os.path.join(script_dir, "..", "src", "utils")
sys.path.append(mymodule_dir)
import utils_test_1


def test_raises_exchange_id_error():
    """Raises a ExchangeIdException"""
    cg = CoinGeckoAPI()
    exchange = "bitsop"
    with pytest.raises(utils_test_1.ExchangeIdException):
        utils_test_1.get_bitso_markets(cg, exchange)


# def test_raises_exchange_markets_error():
#     """Raises a ExchangeMarketsException"""
#     cg = CoinGeckoAPI()
#     bitso_markets = {
#         "bytcoyyyyn": {
#             "targets": ["MXN", "USD", "USDT", "DAI", "BRL", "ARS"],
#             "id": "BTC",
#         }
#     }
#     with pytest.raises(utils_test_1.ExchangeMarketsException):
#         utils_test_1.get_all_exchange_markets(cg, bitso_markets)


def test_raises_exchange_list_error():
    """Raises a ExchangeListException"""
    cg = "coin_gecko_object"
    with pytest.raises(utils_test_1.ExchangeListException):
        utils_test_1.get_exchanges_list(cg)


def test_raises_invalid_df_path():
    """Raises a DfPathException"""
    df = "pandas_df"
    path = "dummy"
    with pytest.raises(utils_test_1.DfPathException):
        utils_test_1.save_df_to_csv(df, path)
