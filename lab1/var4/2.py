def is_palindrome(s):
    # Убираем пробелы и приводим строку к нижнему регистру
    cleaned_s = ''.join(s.split()).lower()
    # Проверяем, равна ли строка своему обратному значению
    return cleaned_s == cleaned_s[::-1]

# Пример использования
input_string = "A man a plan a canal Panama"
if is_palindrome(input_string):
    print(f'"{input_string}" является палиндромом.')
else:
    print(f'"{input_string}" не является палиндромом.')
