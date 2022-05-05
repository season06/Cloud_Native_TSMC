import pytest
from potter import get_price


def test_basics():
  assert 0 == get_price([])
  assert 8 == get_price([1])
  assert 8 == get_price([2])
  assert 8 == get_price([3])
  assert 8 == get_price([4])
  assert 8 * 3 == get_price([1, 1, 1])
