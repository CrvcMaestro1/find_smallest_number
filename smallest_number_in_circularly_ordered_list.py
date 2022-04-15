import math

from fixture import circularly_ordered_list_data_set
from utils import mod, get_element_by_index


class SmallestNumberInOrderedList:

    def __init__(self, ordered_list):
        self.__ordered_list = ordered_list

    @property
    def ordered_list(self):
        return self.__ordered_list

    @ordered_list.setter
    def ordered_list(self, ordered_list):
        self.__ordered_list = ordered_list

    def len_ordered_list(self) -> int:
        return len(self.ordered_list)

    def list_is_pair(self) -> bool:
        return mod(self.len_ordered_list(), 2) == 0

    def get_middle_index(self) -> int:
        middle_index = math.floor(self.len_ordered_list() / 2)
        return middle_index

    def has_a_single_element(self) -> bool:
        return self.len_ordered_list() == 1

    def cut_in_two_by_index(self) -> list:
        ordered_list = self.ordered_list
        middle_index = self.get_middle_index()
        start_index = middle_index
        end_index = middle_index
        if not self.list_is_pair():
            end_index = end_index + 1
        return [ordered_list[:end_index], ordered_list[start_index:]]

    def find_smallest_number(self) -> int:
        middle_index = self.get_middle_index()
        middle_element = get_element_by_index(self.ordered_list, middle_index)

        if self.list_is_pair():
            previous_index = middle_index - 1
            middle_element = get_element_by_index(self.ordered_list, previous_index)

        cut_ordered_list = self.cut_in_two_by_index()
        first_part_cut = get_element_by_index(cut_ordered_list, 0)
        second_part_cut = get_element_by_index(cut_ordered_list, 1)
        last_element_in_second_part = get_element_by_index(second_part_cut, -1)

        if middle_element > last_element_in_second_part:
            first_part_cut = second_part_cut

        self.ordered_list = first_part_cut

        if self.has_a_single_element():
            return get_element_by_index(self.ordered_list, 0)
        else:
            return self.find_smallest_number()


if __name__ == '__main__':
    for current_ordered_list in circularly_ordered_list_data_set:
        smallest_number_in_ordered_list = SmallestNumberInOrderedList(current_ordered_list)
        smallest_number = smallest_number_in_ordered_list.find_smallest_number()
        print('The smallest number in circularly ordered list is: {}'.format(smallest_number))
