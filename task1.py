from typing import List


def get_dict(list1: List, list2: List) -> dict:
    """
    Generate dictionary from two lists with keys and values
    If length list2 < length list1, extra values are None

    :param list1: keys list
    :param list2: values list
    :return: dictionary

    >>> list1 = ['key1', 'key2', 'key3', 'key4']
    >>> list2 = ['val1', 'val2', 'val3']
    >>> print(get_dict(list1, list2))
    {'key1': 'val1', 'key2': 'val2', 'key3': 'val3', 'key4': None}

    >>> list1 = ['key1', 'key2', 'key3']
    >>> list2 = ['val1', 'val2', 'val3', 'val4']
    >>> print(get_dict(list1, list2))
    {'key1': 'val1', 'key2': 'val2', 'key3': 'val3'}
    """
    new_dict = {}

    for i in range(len(list1)):
        if i < len(list2):
            new_dict[list1[i]] = list2[i]
        else:
            new_dict[list1[i]] = None

    return new_dict
