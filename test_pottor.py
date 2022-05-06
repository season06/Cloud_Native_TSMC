import pytest
from potter import Potter


def test_basics():
  assert 0 == Potter([])()
  assert 8 == Potter([1])()
  assert 8 == Potter([2])()
  assert 8 == Potter([3])()
  assert 8 == Potter([4])()
  assert 8 * 3 == Potter([1, 1, 1])()


def test_simple_discounts():
  assert 8 * 2 * 0.95 == Potter([0, 1])()
  assert 8 * 3 * 0.9 == Potter([0, 2, 4])()
  assert 8 * 4 * 0.8 == Potter([0, 1, 2, 4])()
  assert 8 * 5 * 0.75 == Potter([0, 1, 2, 3, 4])()


def test_several_discounts():
  assert 8 + (8 * 2 * 0.95) == Potter([0, 0, 1])()
  assert 2 * (8 * 2 * 0.95) == Potter([0, 0, 1, 1])()
  assert (8 * 4 * 0.8) + (8 * 2 * 0.95) == Potter([0, 0, 1, 2, 2, 3])()
  assert 8 + (8 * 5 * 0.75) == Potter([0, 1, 1, 2, 3, 4])()


def test_edge_cases():
  assert 2 * (8 * 4 * 0.8) == Potter([0, 0, 1, 1, 2, 2, 3, 4])()
  assert 3 * (8 * 5 * 0.75) + 2 * (8 * 4 * 0.8) == \
            Potter([0, 0, 0, 0, 0,
                       1, 1, 1, 1, 1,
                       2, 2, 2, 2,
                       3, 3, 3, 3, 3,
                       4, 4, 4, 4])()
