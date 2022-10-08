list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
# TODO Оформить решение
sorted_list = sorted(list_numbers)

for index in range(len(list_numbers)):
    if list_numbers[index] == sorted_list[-1]:
        max_index = index
        list_numbers[max_index], list_numbers[-1] = list_numbers[-1], list_numbers[max_index]


print(list_numbers)