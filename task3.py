from typing import Union

money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05
# TODO Оформить решение


def time_to_bankrupt(capital_par: Union[int, float], salary_par: Union[int, float],
                     spend_par: [int, float], increase_par: float, month_counter: int = 0) -> int:
    debt = 0
    while capital_par - debt > 0:
        debt += spend_par - salary_par
        spend_par *= 1 + increase_par
        month_counter += 1
    return month_counter - 1


month = time_to_bankrupt(money_capital, salary, spend, increase)
print(month)
