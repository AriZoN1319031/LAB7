
numbers = [4, 7, 12, 25, 33]
user_input = int(input("Введите число: "))

print("Список чисел:", numbers)
print("Вы ввели:", user_input)

if user_input in numbers:
    print("Поздравляю, Вы угадали число!")
else:
    print("Нет такого числа!")
