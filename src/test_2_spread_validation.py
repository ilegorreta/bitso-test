#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv
from datetime import datetime

book_1 = "btc_mxn"
book_2 = "usd_mxn"


def main():
    utc_time = datetime.utcnow()
    year = utc_time.strftime("%Y")
    month = utc_time.strftime("%m")
    day = utc_time.strftime("%d")
    hour = utc_time.strftime("%H")
    path_1 = f"/workspaces/bitso-test/data/bitso/{book_1}/{year}/{month}/{day}/{hour}/files.csv"
    path_2 = f"/workspaces/bitso-test/data/bitso/{book_1}/{year}/{month}/{day}/{hour}/files.csv"

    with open(path_1, "r") as data:
        for line in csv.DictReader(data):
            print(line)


if __name__ == "__main__":
    main()
