import pytest
from potter import get_price


def test_basics():
  assert 0 == get_price([])
  assert 8 == get_price([1])
  assert 8 == get_price([2])
  assert 8 == get_price([3])
  assert 8 == get_price([4])
  assert 8 * 3 == get_price([1, 1, 1])


def test_simple_discounts():
  assert 8 * 2 * 0.95 == get_price([0, 1])
  assert 8 * 3 * 0.9 == get_price([0, 2, 4])
  assert 8 * 4 * 0.8 == get_price([0, 1, 2, 4])
  assert 8 * 5 * 0.75 == get_price([0, 1, 2, 3, 4])
