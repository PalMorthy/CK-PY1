src = not False and True or False and not True

# TODO расписать упрощение выражения
"""
not False and True == True and True == True
False and not True == False and False == False
False or True == True
"""

result = True  # TODO подставить результат выражения

print(src == result)
