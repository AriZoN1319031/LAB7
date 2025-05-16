# 7.2 — Проверка на повторяющиеся элементы

my_list = [1, 5, 3, 5, 7, 9, 1]

duplicates = []
for item in my_list:
    if my_list.count(item) > 1 and item not in duplicates:
        duplicates.append(item)

if duplicates:
    print("Повторяющиеся элементы в списке:", duplicates)
else:
    print("Повторяющихся элементов нет.")
