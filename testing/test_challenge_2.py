#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import pytest

script_dir = os.path.dirname(__file__)
mymodule_dir = os.path.join(script_dir, "..", "src", "utils")
sys.path.append(mymodule_dir)
import utils_test_2


def test_raises_exchange_list_error():
    """Raises a TinkerException"""
    book = "TinkerObject"
    with pytest.raises(utils_test_2.TinkerException):
        utils_test_2.save_book_to_lake(book)
