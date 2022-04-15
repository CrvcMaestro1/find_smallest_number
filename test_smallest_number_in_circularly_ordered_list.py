import pytest

from smallest_number_in_circularly_ordered_list import *


class TestSmallerNumberInCircularlyOrderedList:

    @pytest.mark.parametrize("ordered_list, expected", [
        ([40, 50, 60, 70, 10, 20, 30], 3),
        ([10, 20, 30, 40, 50, 60, 70, 80], 4)
    ])
    def test_get_middle_index(self, ordered_list, expected):
        middle_index = get_middle_index(ordered_list)
        assert middle_index == expected

    @pytest.mark.parametrize("ordered_list, middle_index, expected", [
        ([40, 50, 60, 70, 10, 20, 30], 3, [[40, 50, 60, 70], [70, 10, 20, 30]]),
        ([10, 20, 30, 40, 50, 60, 70, 80], 4, [[10, 20, 30, 40], [50, 60, 70, 80]])
    ])
    def test_cut_in_two_by_index(self, ordered_list, middle_index, expected):
        cut_ordered_list = cut_in_two_by_index(ordered_list, middle_index)
        assert cut_ordered_list == expected

    @pytest.mark.parametrize("ordered_list, expected", [
        ([10, 20, 30, 40, 50, 60, 70], 10),
        ([20, 30, 40, 50, 60, 70, 10], 10),
        ([30, 40, 50, 60, 70, 10, 20], 10),
        ([40, 50, 60, 70, 10, 20, 30], 10),
        ([50, 60, 70, 10, 20, 30, 40], 10),
        ([60, 70, 10, 20, 30, 40, 50], 10),
        ([70, 10, 20, 30, 40, 50, 60], 10),
        ([10, 20, 30, 40, 50, 60, 70, 80], 10),
        ([20, 30, 40, 50, 60, 70, 80, 10], 10),
        ([30, 40, 50, 60, 70, 80, 10, 20], 10),
        ([40, 50, 60, 70, 80, 10, 20, 30], 10),
        ([50, 60, 70, 80, 10, 20, 30, 40], 10),
        ([60, 70, 80, 10, 20, 30, 40, 50], 10),
        ([70, 80, 10, 20, 30, 40, 50, 60], 10),
        ([80, 10, 20, 30, 40, 50, 60, 70], 10),
    ])
    def test_find_smallest_number(self, ordered_list, expected):
        smallest_number = find_smallest_number(ordered_list)
        assert smallest_number == expected
