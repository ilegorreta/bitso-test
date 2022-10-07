#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
from pycoingecko import CoinGeckoAPI

from utils.utils_test_1 import (
    get_bitso_markets,
    get_all_exchange_markets,
    get_exchanges_list,
    save_df_to_csv,
)


def main():
    print("Starting...")
    # Get CoinGeckoAPI object
    cg = CoinGeckoAPI()
    # Get bitso_markets dictionary
    bitso_markets = get_bitso_markets(cg, "bitso")
    # Get exchange_markets list
    exchange_markets = get_all_exchange_markets(cg, bitso_markets)
    # Convert exchange_markets list into Pandas DF
    exchange_markets_df = pd.DataFrame(
        exchange_markets, columns=["exchange_id", "base", "target"]
    )
    # Get all exchanges list
    exchanges_list = get_exchanges_list(cg)
    # Convert exchanges_list into Pandas DF, selecting and renaming certain columns
    exchanges_df = pd.DataFrame(exchanges_list)[
        ["id", "name", "trust_score", "trust_score_rank"]
    ].rename(columns={"id": "exchange_id", "name": "exchange_name"})
    # Filters exchanges_df based on exchange_id contained in exchange_markets_df
    exchanges_df = exchanges_df[
        exchanges_df.exchange_id.isin(exchange_markets_df.exchange_id)
    ]
    print("Writing DF to CSV...")
    # Save dataframes as CSV files
    save_df_to_csv(
        exchanges_df,
        "/home/runner/work/bitso-test/bitso-test/data/test_1/similar_exchanges.csv",
    )
    save_df_to_csv(
        exchange_markets_df,
        "/home/runner/work/bitso-test/bitso-test/data/test_1/markets.csv",
    )
    print("Finished!!")


if __name__ == "__main__":
    main()
