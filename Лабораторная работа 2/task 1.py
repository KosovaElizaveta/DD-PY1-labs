money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

num = 0
bal = money_capital + salary - spend
while bal > 0:
    num += 1
    spend *= (1 + increase)
    bal += salary - spend

print("Количество месяцев, которое можно протянуть без долгов:", num)
