import math

circularly_ordered_list_data_set = [
    [10, 20, 30, 40, 50, 60, 70],
    [20, 30, 40, 50, 60, 70, 10],
    [30, 40, 50, 60, 70, 10, 20],
    [40, 50, 60, 70, 10, 20, 30],
    [50, 60, 70, 10, 20, 30, 40],
    [60, 70, 10, 20, 30, 40, 50],
    [70, 10, 20, 30, 40, 50, 60],
    [10, 20, 30, 40, 50, 60, 70, 80],
    [20, 30, 40, 50, 60, 70, 80, 10],
    [30, 40, 50, 60, 70, 80, 10, 20],
    [40, 50, 60, 70, 80, 10, 20, 30],
    [50, 60, 70, 80, 10, 20, 30, 40],
    [60, 70, 80, 10, 20, 30, 40, 50],
    [70, 80, 10, 20, 30, 40, 50, 60],
    [80, 10, 20, 30, 40, 50, 60, 70],
]

ZERO = 0


def mod(dividend, divisor):
    return dividend % divisor


def get_middle_index(ordered_list):
    len_ordered_list = len(ordered_list)
    middle_index = math.floor(len_ordered_list / 2)
    return middle_index


def cut_in_two_by_index(ordered_list, middle_index):
    len_ordered_list = len(ordered_list)
    if mod(len_ordered_list, 2) != ZERO:
        next_index = middle_index + 1
        return [
            ordered_list[:next_index],
            ordered_list[middle_index:]
        ]
    return [
        ordered_list[:middle_index],
        ordered_list[middle_index:]
    ]


def find_smallest_number(ordered_list):
    middle_index = get_middle_index(ordered_list)
    middle_element = ordered_list[middle_index]
    len_ordered_list = len(ordered_list)
    if mod(len_ordered_list, 2) == ZERO:
        previous_index = middle_index - 1
        middle_element = ordered_list[previous_index]
    cut_ordered_list = cut_in_two_by_index(ordered_list, middle_index)
    first_part_cut = cut_ordered_list[0]
    second_part_cut = cut_ordered_list[1]
    if middle_element > second_part_cut[-1]:
        first_part_cut = second_part_cut
    len_first_part = len(first_part_cut)
    if len_first_part == 1:
        return first_part_cut[0]
    else:
        return find_smallest_number(first_part_cut)


if __name__ == '__main__':
    for current_ordered_list in circularly_ordered_list_data_set:
        smallest_number_in_ordered_list = find_smallest_number(current_ordered_list)
        print('The smallest number in circularly ordered list is: {}'.format(smallest_number_in_ordered_list))
