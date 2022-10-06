#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv
from datetime import datetime

from utils.SpreadValidator import SpreadValidator

BOOK_1 = "btc_mxn"
BOOK_2 = "usd_mxn"


def main():
    total_times_above_threshold = 0
    utc_time = datetime.utcnow()
    book_1_validator = SpreadValidator(BOOK_1, utc_time)
    book_2_validator = SpreadValidator(BOOK_2, utc_time)
    if book_1_validator.is_above and book_2_validator.is_above:
        total_times_above_threshold = 2
    elif book_1_validator.is_above or book_2_validator.is_above:
        total_times_above_threshold = 1
    else:
        total_times_above_threshold = 0
    print(f"The total of order book above threshold was: {total_times_above_threshold}")


if __name__ == "__main__":
    main()
