def get_count_char(str_: str) -> dict:
    list_ = (str_.lower()).split(' ')
    str_ = ''.join(list_)
    dict_ = {symbol: str_.count(symbol) for symbol in str_ if symbol.isalpha()}
    return dict_


def keys_pr(dict_: dict) -> dict:
    sum_key = 0
    for key in dict_:
        sum_key += dict_[key]
    dict_1 = {key: (dict_[key] / sum_key) * 100 for key in dict_}
    return dict_1


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""

if __name__ == "__main__":
    print(get_count_char(main_str))
    print(keys_pr(get_count_char(main_str)))
