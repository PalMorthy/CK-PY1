from pprint import pprint


def representation_number_in_list_of_dict(list_size: int) -> list[dict]:
    """
    Create list of dict with number in any number systems  '\n'

    :param list_size: size of output list
    :return: list of dict that contained representation of numbers in 2, 10, 8 and 16 number systems
    """
    list_of_dict = [{'bin': bin(number),
                     'dec': number,
                     'hex': hex(number),
                     'oct': oct(number)} for number in range(list_size + 1)]
    return list_of_dict


if __name__ == "__main__":
    required_size = 15
    pprint(representation_number_in_list_of_dict(required_size))
