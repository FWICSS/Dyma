#  Copyright (c) 2022. Code by Dimitri AIGLE
class MyCustomTypeError(Exception):
    def __int__(self,message):
        self.message = message

def my_split(string, char=None):
    if not isinstance(string, str):
        raise MyCustomTypeError("Mauvais Type")
    if char is None:
        return string
    res = []
    current_list = []
    for c in string:
        if c != char:
            current_list.append(c)
        else:
            res.append("".join(current_list))
            current_list = []
    res.append("".join(current_list))
    return res