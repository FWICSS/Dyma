def fonction_test(dictionnaire, condition):
    if(condition & (len(dictionnaire) > 0)):
        dictionnaire.popitem()
    if(not condition):
        dictionnaire["nouveau"] = 42

    return dictionnaire