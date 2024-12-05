#Светкин Никита Евгеньевич ФИТ-221

import pandas as pd
from data import vgsales, metacritic_games


# 1. Вывести все доступные платформы
def get_unique_platforms():
    platforms = vgsales['Platform'].unique()
    print("Доступные платформы:")
    for platform in platforms:
        print(platform)
    return platforms


# 2. Добавить столбец metacritic_rating
def add_metacritic_rating():
    print("Столбцы в metacritic_games.csv:", metacritic_games.columns.tolist())

    # Создаем копию набора данных
    vgsales_copy = vgsales.copy()

    try:
        # Объединяем данные по названию игры
        merged_data = pd.merge(
            vgsales_copy,
            metacritic_games[['name', 'metascore', 'rating']],  # Используем rating из metacritic_games
            left_on='Name',
            right_on='name',
            how='left'
        )

        # Удаляем лишний столбец (name из metacritic_games)
        merged_data.drop(columns=['name'], inplace=True)

        # Переименовываем столбцы
        merged_data.rename(columns={'metascore': 'metacritic_rating', 'rating': 'Rating'}, inplace=True)

        print("Новый набор данных с рейтингом Metacritic:")
        print(merged_data.head())
        return merged_data

    except KeyError as e:
        print(f"Ошибка: {e}")
        print("Проверьте названия столбцов в metacritic_games.csv и измените код в соответствии с ними.")
        return vgsales_copy


# 3. Вывести список игр с рейтингом "M" и годом выпуска не ранее 2012 года
def get_mature_games_after_2012(data):

    # Фильтрация по условиям
    mature_games = data[(data['Rating'] == 'M') & (data['Year'] >= 2012)]

    print("Игры с рейтингом 'M', выпущенные не ранее 2012 года:")
    print(mature_games[['Name', 'Year', 'Platform', 'Rating']])
    return mature_games


# 4. Рассчитать описательные статистики
def calculate_statistics(data):
    print("Описательные статистики:")
    stats = data.describe(include='all')
    print(stats)
    return stats


# 5. Вывести жанры игр с количеством игр (условие по гласным)
def get_genres_with_vowel_count():
    def count_unique_vowels(string):
        vowels = {'a', 'e', 'i', 'o', 'u'}
        return len(set(filter(lambda char: char in vowels, string.lower())))

    genres = vgsales['Genre'].value_counts()
    filtered_genres = genres[genres.index.map(count_unique_vowels) >= 3]

    print("Жанры с >= 3 различными гласными:")
    for genre, count in filtered_genres.items():
        print(f"{genre} - {count}")


if __name__ == '__main__':
    # Вывод доступных платформ
    platforms = get_unique_platforms()

    # Добавление рейтинга Metacritic
    vgsales_with_rating = add_metacritic_rating()

    # Фильтрация игр с рейтингом 'M' и годом >= 2012
    mature_games = get_mature_games_after_2012(vgsales_with_rating)

    # Описательные статистики
    if not mature_games.empty:
        stats = calculate_statistics(mature_games)
    else:
        print("Нет подходящих игр для анализа.")

    get_genres_with_vowel_count()

