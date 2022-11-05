from random import sample
from typing import List


def get_unique_list_numbers(border: List[int], list_size: int) -> List[int]:
    """
    The function is generated the list of random unique type INT value '\n'
    :param border: The range in which random numbers are given
    :param list_size: The size of a list of random unique numbers
    :return: List that collected random unique numbers
    """
    list_numbers = [value for value in range(border[0], border[-1])]
    list_rndm_num = sample(list_numbers, list_size)
    return list_rndm_num


if __name__ == "__main__":
    list_unique_numbers = get_unique_list_numbers([-10, 10], 15)
    print(list_unique_numbers)
    print(len(list_unique_numbers) == len(set(list_unique_numbers)))
