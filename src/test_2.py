#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from utils.utils_test_2 import get_ticker_attributes, save_book_to_lake

BITSO_API_URL_BTC_MXN = os.getenv("BITSO_API_URL_BTC_MXN")
BITSO_API_URL_USD_MXN = os.getenv("BITSO_API_URL_USD_MXN")


def main():
    print("Starting...")
    book_1 = get_ticker_attributes(BITSO_API_URL_BTC_MXN)
    save_book_to_lake(book_1)
    book_2 = get_ticker_attributes(BITSO_API_URL_USD_MXN)
    save_book_to_lake(book_2)
    print("Finished test 2!")


if __name__ == "__main__":
    main()
