# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

from random import *
import os


welcome_text = ('Приветствуем вас на игре в конфеты\n'
                'Правила игры не сложные:\n'
                'На столе лежат 2023 конфеты, вы берете их поочереди,\n'
                'причем, за один раз можно взять не больше 28 конфет.\n'
                'Выигрывает тот, кто последним ходом заберет все конфеты.\n'
                "'Let's go!!!'")
print(welcome_text)

message = ['бери,твоя очередь', 'да бери уже не стесняйся', 'бери больше', 
           'бери быстрее, здесь все свои', 'бери пока дают']

def player_vs_bot():
    candies_total = 200
    max_take = 28
    player_1 = input('\nКак тебя зовут?: ')
    player_2 = 'Бот'
    players = [player_1, player_2]
    print(f'\nНу чтож {player_1} и  {player_2} начинаем игру!\n')
    print('\nЖребий покажет, чей ход первый\n')

    lucky = randint(-1, 0)

    print(f'Поздравляю {players[lucky+1]} ты ходишь первым !')

    while candies_total > 0:
        lucky += 1

        if players[lucky % 2] == 'Бот':
            print(
                f'\nХодит {players[lucky%2]} \nНа столе {candies_total}. \n{choice(message)}: ')

            if candies_total < 29:
                step = candies_total
            else:
                delenie = candies_total//28
                step = candies_total - ((delenie*max_take)+1)
                if step == -1:
                    step = max_take -1
                if step == 0:
                    step = max_take
            while step > 28 or step < 1:
                step = randint(1,28)
            print(step)
        else:
            step = int(input(f'\nНу чтож ходи,  {players[lucky%2]} \nНа столе {candies_total} {choice(message)}:  '))
            while step > max_take or step > candies_total:
                step = int(input(f'\nЗа один ход можно взять {max_take} конфет, попробуй еще раз: '))
        candies_total = candies_total - step

    print(f'На столе осталось {candies_total} \nПобедил {players[lucky%2]}')

player_vs_bot()

