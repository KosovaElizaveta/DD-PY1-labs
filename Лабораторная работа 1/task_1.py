numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

#numbers[4] = 0 - а так нельзя?

missing = 4
sum_n = sum(numbers[:missing]) + sum(numbers[missing+1:])
count_n = (len(numbers))

averange = sum_n / count_n
numbers[missing] = averange

print("Измененный список:", numbers)
