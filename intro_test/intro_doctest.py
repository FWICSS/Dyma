#  Copyright (c) 2022. Code by Dimitri AIGLE
import doctest


def my_split(str,char=' '):
    """
    >>> my_split('je suis une str',' ')
    ['je', 'suis', 'une', 'str']
    >>> my_split('je suis une str')
    ['je', 'suis', 'une', 'str']
    >>> my_split('je suis une str','')
    ['je suis une str']
    """
    res = []
    current_list = []
    for c in str:
        if c != char:
            current_list.append(c)
        else:
            res.append("".join(current_list))
            current_list = []
    res.append("".join(current_list))
    return res



doctest.testmod()