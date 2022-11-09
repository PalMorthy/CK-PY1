from random import sample
from string import digits, ascii_uppercase, ascii_lowercase


def get_random_password(password_size: int = 8) -> str:
    __alphabet_lower__ = ascii_lowercase
    __alphabet_upper__ = ascii_uppercase
    __numbers__ = digits
    string_sample = ''.join(__alphabet_lower__ + __alphabet_upper__ + __numbers__)
    list_sample = [item for item in string_sample]
    password = ''.join(sample(list_sample, password_size))
    return password


if __name__ == "__main__":
    print(get_random_password())
