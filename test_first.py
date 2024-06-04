import pytest

from your_module import sumOfThree

def test_sumOfThree_with_valid_input():
    nums = [1, 2, 3]
    assert sumOfThree(nums) == 6

def test_sumOfThree_with_mixed_input():
    nums = [1, "2", 3]
    assert sumOfThree(nums) == 6

def test_sumOfThree_with_invalid_input():
    nums = [1, "a", 3]
    assert sumOfThree(nums) == 4  # Sum should exclude the invalid input

def test_sumOfThree_with_empty_list():
    nums = []
    assert sumOfThree(nums) == 0

def test_sumOfThree_with_negative_numbers():
    nums = [-1, -2, -3]
    assert sumOfThree(nums) == -6

def test_sumOfThree_with_float_numbers():
    nums = [1.5, 2.5, 3.5]
    assert sumOfThree(nums) == 7
