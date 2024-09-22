from collections import Counter


def most_common_letter(s):
    # Убираем пробелы и приводим строку к нижнему регистру
    cleaned_s = ''.join(s.split()).lower()
    # Используем Counter для подсчета частоты букв
    counter = Counter(cleaned_s)

    # Находим букву с максимальной частотой
    most_common = counter.most_common(1)

    if most_common:
        letter, frequency = most_common[0]
        return letter, frequency
    return None, 0  # Если строка пустая


# Пример использования
input_string = "Hello World"
letter, frequency = most_common_letter(input_string)

if letter:
    print(f'Буква "{letter}" встречается чаще всего: {frequency} раз(а).')
else:
    print("Строка пуста.")
