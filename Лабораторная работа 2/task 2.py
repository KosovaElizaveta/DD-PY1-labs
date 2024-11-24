salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

loss = 0
for i in range(months):
    loss += spend - salary
    spend += spend * increase
loss = int(loss)

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", loss)
