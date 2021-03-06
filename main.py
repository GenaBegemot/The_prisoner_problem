# Разгадка, в которую невозможно поверить: задача о 100 заключённых [Veritasium] (https://youtu.be/wWQ9YdreY9c)
# 100 заключенных пронумерованы от 1 до 100
# Их номера записаны на бумажках и спрятаны случайным образом в 100 коробках, расставленных по комнате
# Каждый заключенный может зайти в комнату один раз и попробовать найти свой номер, открыв максимум 50 коробок
# После этого закрыть все коробки и оставить все как было, выйти из комнаты. Возможности общаться с другими нет.
# Если все 100 узников найдут свой номер - их отпустят. Если нет - казнят.
# Заключенные могут обсудить стратегию один раз до того, как первый зайдет в комнату с коробками.
# Какую стратегию выбрать?

import random

list_1, list_2, list_people, list_result = [], [], [], []         # создаем пустые списки

for i in range(1, 101):
    list_1.append(i)            # заполняем списки цифрами от 0 до 100
    list_2.append(i)            # заполняем списки цифрами от 0 до 100
    list_people.append(i)       # заполняем списки цифрами от 0 до 100


random.shuffle(list_1)          # перемешиваем значения в списках случайным образом
random.shuffle(list_2)          # перемешиваем значения в списках случайным образом


def find_box(my_num):
    count = 0
    new_dict = dict(zip(list_1,list_2))  # создаем новый словарь на основании списков
    # print(new_dict)                    # показать словарь
    s = new_dict[my_num]
    while my_num != s:          # если значение коробки не равно загданному числу, то повторит
        s = new_dict[s]         # переприсвоить значения
        # print(s)              # отладочные данные закомментированы
        count += 1              # посчитать попытки

    # print(f"Порядковый номер {my_num}")               # отладочные данные закомментированы
    # print(f"Поздравляю, вы нашли свое число {s}")     # отладочные данные закомментированы
    # print(f"Количество попыток составило {count}")    # отладочные данные закомментированы
    list_result.append(count)


for k in list_people:
    # print(find_box(k))
    find_box(k)

print(f"Максимальное количество попыток: {max(list_result)}")

if max(list_result) <= 50: print("Все заключенные спаслись")
else: print("Заключенных казнили. Всех до одного. 100 человек. Кошмар!")