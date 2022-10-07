#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import pytest

script_dir = os.path.dirname(__file__)
mymodule_dir = os.path.join(script_dir, "..", "src", "utils")
sys.path.append(mymodule_dir)
import SpreadValidator


def test_raises_utc_time_exception():
    """Raises a UTCTimeException"""
    sv = SpreadValidator.SpreadValidator("mxn_btc", 2022)
    with pytest.raises(SpreadValidator.UTCTimeException):
        SpreadValidator.SpreadValidator.validate_spread(sv)
