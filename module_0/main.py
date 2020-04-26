import numpy as np


def game_core_v1(number):
    """Просто угадываем на random, не используя информацию о больше или меньше.

    Функция принимает загаданное число и возвращает число попыток
    """
    count = 0
    while True:
        count += 1
        predict = np.random.randint(1, 101)  # предполагаемое число
        if number == predict:
            return count  # выход из цикла, если угадали


def score_game(game_core):
    """Запускает игру 1000 раз.

    Используется для определения, как быстро игра угадывает число.
    """
    count_ls = []
    # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=1000)
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return score


# запускаем
score_game(game_core_v1)
