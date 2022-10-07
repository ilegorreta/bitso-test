#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import pytest

script_dir = os.path.dirname(__file__)
mymodule_dir = os.path.join(script_dir, "..", "src", "utils")
sys.path.append(mymodule_dir)
import Ticker


def test_raises_endpoint_not_valid():
    """Raises a BitsoEndpointException"""
    tk = Ticker.Ticker("https://dummy")
    with pytest.raises(Ticker.BitsoEndpointException):
        Ticker.Ticker.get_bitso_api_data(tk)


def test_raises_endpoint_not_valid():
    """Raises a IsAboveNotBooleanException"""
    tk = Ticker.Ticker("https://dummy")
    tk.is_above = "Yes"
    with pytest.raises(Ticker.IsAboveNotBooleanException):
        Ticker.Ticker.format_result(tk)


def test_raises_path_not_valid():
    """Raises a PathNotValidException"""
    tk = Ticker.Ticker("https://dummy")
    tk.book = "mxn_btc"
    tk.day = 10
    tk.hour = "18"
    with pytest.raises(Ticker.PathNotValidException):
        Ticker.Ticker.get_partition_path(tk)
