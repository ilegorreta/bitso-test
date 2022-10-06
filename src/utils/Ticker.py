#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import requests

EXCHANGE = "bitso"
SPREAD_THRESHOLD = 0.1


class Ticker:
    """Class template for retrieving and storing ticker information

    Constructor Args:
        endpoint_url: String corresponding to the API Bitso API endpoint
    """

    def __init__(self, endpoint_url):
        self.endpoint_url = endpoint_url
        self.ask = None
        self.bid = None
        self.book = None
        self.day = None
        self.hour = None
        self.timestamp = None
        self.spread = None
        self.result = None
        self.is_above = None
        self.path = None

    def get_bitso_api_data(self):
        """Fetch data from Bitso API and assign the corresponding instance attributes"""
        response = requests.request("GET", self.endpoint_url)
        order_book = json.loads(response.text)["payload"]
        self.ask = float(order_book["ask"])
        self.bid = float(order_book["bid"])
        self.book = order_book["book"]
        self.day = order_book["created_at"][:10]
        self.hour = order_book["created_at"][11:13]
        self.timestamp = order_book["created_at"]
        self.spread = ((self.ask - self.bid) * 100) / self.ask

    def format_result(self):
        """Create the Dict result attribute"""
        self.result = {
            "orderbook_timestamp": self.timestamp,
            "book": self.book,
            "bid": self.bid,
            "ask": self.ask,
            "spread": self.spread,
            "is_above": True if self.spread > SPREAD_THRESHOLD else False,
        }

    def get_partition_path(self):
        """Format the partition path where the file will be saved within the lake"""
        self.path = f"/workspaces/bitso-test/data/{EXCHANGE}/{self.book}/{self.day}/{self.hour}/"
