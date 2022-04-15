import pytest

from smallest_number_in_circularly_ordered_list import *


class TestSmallerNumberInCircularlyOrderedList:

    @property
    def ordered_list(self):
        return self.__ordered_list

    @ordered_list.setter
    def ordered_list(self, ordered_list):
        self.__ordered_list = ordered_list

    def get_smallest_number_finder(self):
        smallest_number_finder = SmallestNumberInOrderedList(self.ordered_list)
        return smallest_number_finder

    @pytest.mark.parametrize("ordered_list, expected", [
        ([40, 50, 60, 70, 10, 20, 30], 3),
        ([10, 20, 30, 40, 50, 60, 70, 80], 4)
    ])
    def test_get_middle_index(self, ordered_list, expected):
        self.ordered_list = ordered_list
        middle_index = self.get_smallest_number_finder().get_middle_index()
        assert middle_index == expected

    @pytest.mark.parametrize("ordered_list, middle_index, expected", [
        ([40, 50, 60, 70, 10, 20, 30], 3, [[40, 50, 60, 70], [70, 10, 20, 30]]),
        ([10, 20, 30, 40, 50, 60, 70, 80], 4, [[10, 20, 30, 40], [50, 60, 70, 80]])
    ])
    def test_cut_in_two_by_index(self, ordered_list, middle_index, expected):
        self.ordered_list = ordered_list
        cut_ordered_list = self.get_smallest_number_finder().cut_in_two_by_index()
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
        self.ordered_list = ordered_list
        smallest_number_result = self.get_smallest_number_finder().find_smallest_number()
        assert smallest_number_result == expected
