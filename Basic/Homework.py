# Объявить переменную типа list() со списком покупок,
# выводить список по одному элементу с  конце в виде строки "- <list_item>;"
# пока в списке есть элементы

purchases = list(("potatoes",'cucumber', 'tomato', 'apple','cherry'))

while purchases:
    item = purchases.pop()
    print(f"- {item}")
print("\n")

#- объявить переменную my_contacts с типом dict(), ключь - имя(строка), значение - номер(строка)
# Добавить 6 значений при инициализации переменной,
# добавлять по элементно значение пока длина словаря не будет 15, вывести конечный словарь на печать
# Имена могут повторяться

my_contacts = {'Alina': '111',
               'Klava': '222',
               'Sofa': '444',
               'Nina': '444',
               'Anya': '555'}
while len(my_contacts) < 5:
    name = input('Enter name ')
    phone = input('Enter number ')
    my_contacts[name] = phone
print(my_contacts, '\n')

#сделать копию из словаря my_contacts через deepcopy(),
# удалить последнее значение из нового словаря и получить список ключей,
# из полученного списка напечатать все уникальные имена в виде строки через запятую

import copy
copied_my_contact = copy.deepcopy(my_contacts)

my_contacts['Gigi'] = '777'
print(my_contacts)

print(copied_my_contact)

copied_my_contact.popitem()
val_list = copied_my_contact.values()

unique_val = ', '.join(set(val_list))
print(unique_val,'\n')

#Найти количество уникальный слов в тексте: "Harry Potter is a series of seven fantasy novels written by British author J. K. Rowling.
# The novels chronicle the lives of a young wizard, Harry Potter, and his friends Hermione Granger and Ron Weasley, all of whom are students at Hogwarts School of Witchcraft and Wizardry. The main story arc concerns Harry's struggle against Lord Voldemort, a dark wizard who intends to become immortal, overthrow the wizard governing body known as the Ministry of Magic and subjugate all wizards and Muggles (non-magical people).
# Since the release of the first novel, Harry Potter and the Philosopher's Stone, on 26 June 1997, the books have found immense popularity, positive reviews, and commercial success worldwide. They have attracted a wide adult audience as well as younger readers and are often considered cornerstones of modern young adult literature. As of February 2018, the books have sold more than 500 million copies worldwide, making them the best-selling book series in history, and have been translated into eighty languages. The last four books consecutively set records as the fastest-selling books in history, with the final instalment selling roughly 2.7 million copies in the United Kingdom and 8.3 million copies in the United States within twenty-four hours of its release.
# The series was originally published in English by two major publishers, Bloomsbury in the United Kingdom and Scholastic Press in the United States. All versions around the world are printed by Grafica Veneta in Italy.

# Найти количество вхождений каждого слова в текст, ответ напечатать в консоль"

text = """
Harry Potter is a series of seven fantasy novels written by British author J. K. Rowling. The novels chronicle the lives of a young wizard, Harry Potter, and his friends Hermione Granger and Ron Weasley, all of whom are students at Hogwarts School of Witchcraft and Wizardry. The main story arc concerns Harry's struggle against Lord Voldemort, a dark wizard who intends to become immortal, overthrow the wizard governing body known as the Ministry of Magic and subjugate all wizards and Muggles (non-magical people).
Since the release of the first novel, Harry Potter and the Philosopher's Stone, on 26 June 1997, the books have found immense popularity, positive reviews, and commercial success worldwide. They have attracted a wide adult audience as well as younger readers and are often considered cornerstones of modern young adult literature. As of February 2018, the books have sold more than 500 million copies worldwide, making them the best-selling book series in history, and have been translated into eighty languages. The last four books consecutively set records as the fastest-selling books in history, with the final instalment selling roughly 2.7 million copies in the United Kingdom and 8.3 million copies in the United States within twenty-four hours of its release.
The series was originally published in English by two major publishers, Bloomsbury in the United Kingdom and Scholastic Press in the United States. All versions around the world are printed by Grafica Veneta in Italy."""

t2 = text.lower()
t2_2 = t2.split()
t3 = []
for x in t2_2:
    if x not in t3:
        t3.append(x)
    else:
        pass
print(t2_2)
print(t3)
print(len(t3),'\n')

from collections import Counter
import re
new_text = re.findall(r'\b\w+\b', t2)
el_counts = Counter(new_text)

for x in new_text:
    print(f'unique itmes in {new_text} are {el_counts}','\n')



from collections import Counter
import re

# Исходный текст
text = """
Harry Potter is a series of seven fantasy novels written by British author J. K. Rowling. 
The novels chronicle the lives of a young wizard, Harry Potter, and his friends Hermione Granger and Ron Weasley, 
all of whom are students at Hogwarts School of Witchcraft and Wizardry. 
The main story arc concerns Harry's struggle against Lord Voldemort, 
a dark wizard who intends to become immortal, overthrow the wizard governing body known as the Ministry of Magic 
and subjugate all wizards and Muggles (non-magical people).
Since the release of the first novel, Harry Potter and the Philosopher's Stone, on 26 June 1997, 
the books have found immense popularity, positive reviews, and commercial success worldwide. 
They have attracted a wide adult audience as well as younger readers and are often considered cornerstones of modern young adult literature. 
As of February 2018, the books have sold more than 500 million copies worldwide, 
making them the best-selling book series in history, and have been translated into eighty languages. 
The last four books consecutively set records as the fastest-selling books in history, 
with the final installment selling roughly 2.7 million copies in the United Kingdom and 8.3 million copies in the United States within twenty-four hours of its release. 
The series was originally published in English by two major publishers, 
Bloomsbury in the United Kingdom and Scholastic Press in the United States. 
All versions around the world are printed by Grafica Veneta in Italy.
"""

# Приводим все слова к нижнему регистру и используем регулярное выражение для извлечения слов
words = re.findall(r'\b\w+\b', text.lower())

# Используем Counter для подсчета вхождений каждого слова
word_counts = Counter(words)

# Выводим результат
for word, count in word_counts.items():
    print(f"{word}: {count}")



