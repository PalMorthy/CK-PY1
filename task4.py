salary = 5000  # зарплата
spend = 6000  # траты
months = 5  # количество месяцев
increase = 0.05  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев

# TODO Оформить решение
i = 0
while i <= months - 1:
    need_money += spend - salary
    spend *= 1 + increase
    i += 1

print(round(need_money))
