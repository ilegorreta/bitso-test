#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv
import pathlib
from utils.Ticker import Ticker


def get_ticker_attributes(api_endpoint):
    """Creates Ticker object and populates its corresponding attributes

    Args:
        api_endpoint: String corresponding to the API Bitso API endpoint

    Returns:
        book: Ticker object with all the order_book information loaded
    """
    book = Ticker(api_endpoint)
    book.get_bitso_api_data()
    book.format_result()
    book.get_partition_path()
    return book


def save_book_to_lake(book):
    """Saves Ticker object information into the Lake as a partition in a CSV format

    Args:
        book: Ticker object with all the order_book information loaded
    """
    pathlib.Path(book.path).mkdir(parents=True, exist_ok=True)
    with open(f"{book.path}/files.csv", "w") as f:
        w = csv.DictWriter(f, book.result.keys())
        w.writeheader()
        w.writerow(book.result)
