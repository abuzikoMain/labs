import pytest

from first import sumOfThree, AreaOfRightTriangle

class TestSumOfThree:
    def test_sumOfThree_with_valid_input(self):
        nums = [1, 2, 3]
        assert sumOfThree(nums) == 6

    def test_sumOfThree_with_mixed_input(self):
        nums = [1, "2", 3]
        assert sumOfThree(nums) == 6

    def test_sumOfThree_with_invalid_input(self):
        nums = [1, "a", 3]
        assert sumOfThree(nums) == 4  # Sum should exclude the invalid input

    def test_sumOfThree_with_empty_list(self):
        nums = []
        assert sumOfThree(nums) == 0

    def test_sumOfThree_with_negative_numbers(self):
        nums = [-1, -2, -3]
        assert sumOfThree(nums) == -6

    def test_sumOfThree_with_float_numbers(self):
        nums = [1.5, 2.5, 3.5]
        assert sumOfThree(nums) == 7.5


class TestAreaOfRightTriangle:
    def test_area_with_valid_input(self):
        base = 3
        height = 4
        assert AreaOfRightTriangle(base, height) == 6

    def test_area_with_float_input(self):
        base = 2.5
        height = 4.5
        assert AreaOfRightTriangle(base, height) == 5.625

    def test_area_with_zero_input(self):
        base = 0
        height = 5
        assert AreaOfRightTriangle(base, height) == 0

    def test_area_with_negative_input(self):
        base = -3
        height = 4
        assert AreaOfRightTriangle(base, height) == 0

    def test_area_with_invalid_input(self):
        base = "a"
        height = 4
        assert AreaOfRightTriangle(base, height) == 0  # Invalid input should be ignored, so area should still be calculated correctly
