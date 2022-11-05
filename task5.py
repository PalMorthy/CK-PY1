from random import sample


def get_random_password(password_size: int = 8) -> str:
    __alphabet_lower__ = 'abcdefghigjklmnopqrstuvwxyz'
    __alphabet_upper__ = __alphabet_lower__.upper()
    __numbers__ = "0123456789"
    string_sample = ''.join(__alphabet_lower__ + __alphabet_upper__ + __numbers__)
    list_sample = [item for item in string_sample]
    password = ''.join(sample(list_sample, password_size))
    return password


if __name__ == "__main__":
    print(get_random_password())
