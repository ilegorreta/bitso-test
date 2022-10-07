#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv


class CustomException(Exception):
    """Base class for other exceptions regarding Bitso Sr. Data Engineer Challenge"""

    pass


class UTCTimeException(CustomException):
    """Raised when the UTC Time provided is not a string"""

    pass


class SpreadValidator:
    """Class template for validating bid-ask spread for a giveen order book

    Constructor Args:
        book: String corresponding to the given order book
        utc_time: Datetime object indicating the current UTC time
    """

    def __init__(self, book, utc_time):
        self.book = book
        self.utc_time = utc_time
        self.path = None
        self.is_above = None

    def validate_spread(self):
        """Validate if the bid-ask spread is above the given threshold"""
        if not isinstance(self.utc_time, str):
            raise UTCTimeException("UTC Time provided is not string")
        year = self.utc_time.strftime("%Y")
        month = self.utc_time.strftime("%m")
        day = self.utc_time.strftime("%d")
        hour = self.utc_time.strftime("%H")
        self.path = f"/workspaces/bitso-test/data/bitso/{self.book}/{year}-{month}-{day}/{hour}/files.csv"
        with open(self.path, "r") as data:
            for line in csv.DictReader(data):
                if line["is_above"] == "True":
                    self.is_above = True
                else:
                    self.is_above = False
