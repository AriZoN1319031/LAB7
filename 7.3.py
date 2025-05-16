
days = ("Понедельник", "Вторник", "Среда", "Четверг",
        "Пятница", "Суббота", "Воскресенье")

count = int(input("Сколько выходных на неделе вы хотите? "))
weekends = days[-count:]

workdays = days[:-count]

print("Ваши выходные дни:", list(weekends))
print("Ваши рабочие дни:", list(workdays))
