from typing import List


def delete(list_: List, index=None) -> List:

    """
    This function delete element of list with index = args. If args is not set, it defaults to removing the
    last element of the list
    :param list_: The list in which to remove the element
    :param index:  Optional, if args is None index of deleted element of list equal list[-1]
    :return: Modified list
    """

    list_len = len(list_)
    if index is None or index > list_len:
        list_ = list_[: -1]
        return list_
    else:
        lst_before_dlt_index = list_[:index]
        lst_after_dlt_index = list_[index + 1:]
        list_ = lst_before_dlt_index + lst_after_dlt_index
        return list_


print(delete([0, 0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 1, 2, 3], index=10))  # [0, 1, 2]
print(delete([0, 1, 2, 3, 4, 4]))  # [0, 1, 2, 3]
