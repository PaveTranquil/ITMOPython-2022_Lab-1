import csv
import random

# Задание №1 (ознакомиться с основами работы с таблицами в Python)
with open('books.csv', encoding='windows-1251') as f:
    reader = csv.DictReader(f, delimiter=';', quotechar='"')
    books = list(reader)


# Задание №2
print(len(books), end='\n----------\n')


# Задание №3
print(len(list(filter(lambda book: len(book['Название']) > 30, books))), end='\n----------\n')


# Задание №4
request = input('Введите запрос: ')
response = list(filter(lambda book: ((request in book['Автор'] or request in book['Автор (ФИО)']) and
                                     float(book['Цена поступления'].replace(',', '.')) >= 150),
                       books))
print('\n'.join([book['Название'] for book in response]), end='\n----------\n')


# Задание №5
is_random = input('Случайный запрос? (y/n) ').lower() == 'y'
if is_random:
    resp = random.choices(books, k=20)
else:
    request = input('Введите запрос: ')
    #! TODO Выбрать одно из двух
    resp = list(filter(lambda book: request in book['Название'], books))[:20]
    # resp = list(filter(lambda book: request in book['Автор'] or request in book['Автор (ФИО)'], books))[:20]

with open('task5.txt', 'w', encoding='utf-8') as f:
    #? Уточнить, что такое <год> в формате вывода
    f.write('\n'.join([f'{b["Автор"]}. {b["Название"]} - {b["Дата поступления"]}' for b in resp]))
    print('Файл task5.txt успешно создан', end='\n----------\n')


# Допзадание №1
tags = []
for book in books:
    tags.extend(book['Жанр книги'].split('# '))
print(', '.join(set(tags)), end='\n----------\n')


# Допзадание №2
sorted_books = sorted(books, key=lambda book: int(book['Кол-во выдач']), reverse=True)
print('\n'.join([f'{b["Автор"]} - {b["Название"]}' for b in sorted_books[:20]]), end='\n----------\n')
