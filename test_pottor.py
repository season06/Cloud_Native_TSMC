import pytest
from potter import get_price

def test_ci():
    assert 1 == get_price([])
