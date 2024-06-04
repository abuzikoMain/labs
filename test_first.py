import pytest

from first import sumOfThree, AreaOfRightTriangle, applesInBox, clock

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

class TestApplesInBox:
    def test_apples_with_valid_input(self):
        base = 61
        height = 4
        assert applesInBox(base, height) == (15, 1)
        base = 50
        height = 6
        assert applesInBox(base, height) == (8, 2)
        base = 10
        height = 1
        assert applesInBox(base, height) == (10, 0)
        base = 25
        height = 5
        assert applesInBox(base, height) == (5, 0)
        base = 2
        height = 4
        assert applesInBox(base, height) == (0, 2)

class TestClock:
    def test_clocK_valid_input(self):
        data = {"150": "2 30", "1441": "0 1", "444": "7 24"}

        for key, value in data.items():
            assert clock(key) == value