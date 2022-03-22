import random
# жизнь и сила атаки нашего героя
live_guardion = 10

attack_guardion = 10

# Создания списка с  монстрами
Process_Game_Person = ['Троль', 'Кутикула', 'Злой китаец', 'Украинец', 'Крип', 'Дотер']
# Создание бонусов
Process_Game_Bonus_Attack = [ 'Зачарованный Мечь']
Process_Game_Bonus_Live = ['Яблоко']


# начало игры ввод с клавиатуры для пользователя
def start_game():
    start_game = input('Герой и Чудовище.\n Введите "Start" для началы игры. \n....')
    if start_game == "Start":
        print('\n\n\nВаш персонаж : "Рыцарь" \nОписание  \n Жизней :', live_guardion, '\n Сила Удара : ',
              attack_guardion)
    else:
        start_game != "Start"
        print('Exec Game')
        exit()
        return


start_game()

# Цикл будет работать до тех пор пока Переменная Pobeda меньше 10
Pobeda = 0

# Создание цикла
while Pobeda < 10:
    person_random = Process_Game_Person + Process_Game_Bonus_Live + Process_Game_Bonus_Attack  # рандомный персонаж / бонус в одной переменной
    person = random.choice(person_random)
    Process_Game_live = random.randint(1, 30)  # рандмоное число жизни
    Process_Game_atack = random.randint(1, 15)  # рандомное число атаки
    num = input('Отпровляемся в путь ........')
    queshon_Yes = '1'
    queshon_No = '2'

    # print('Ваш нынещний урон ',attack_guardion) # Проверка добавился ли урон

    # Проверка бонусных предметов если выпадает даеться 2 выбора взять или не взять
    #         Зачарованный Мечь
    if person == 'Зачарованный Мечь':
        attack_guardion += Process_Game_atack + 2
        print('Великолепно перед вами ,', '"', person, '"', 'Дполнительный урон увеличился на  +', Process_Game_atack + 2,'\n Ваша атака равна:',attack_guardion)

    # Яблоко
    elif person == 'Яблоко':
        live_guardion += Process_Game_live
        print('Вам попался Игровой бонус :', '"', person, '"', 'Дополнительная жизнь увеличина на +', Process_Game_live,'\n Ваша жизнь равна:',live_guardion)


    # Если встречаеться монстр
    elif person:
        print('\n\n\nНа вашем пути,', person, 'Его жизнь', Process_Game_live, 'Сила Атаки :', Process_Game_atack)
        queshon_fith = input('\n Что будем делать \n....\n\n Атаковать (1) \n Убежать (2)\n.....')

        if queshon_fith == queshon_Yes:
            print('\n Рыцарь : "Будем ебашиться значит"')
            input('Нажми для удара.......')

            # Цикл длиться до тех пор пока жизнь врага больше 0
            while Process_Game_live >= 0:
                print('\nТыщь......')
                Process_Game_live -= attack_guardion
                print('осталось', Process_Game_live, 'Жизней у ', person)

                # Проверка если жизнь врага меньше или равна 0 то мы выграли нашего монстра и переменная pobeda пребовляеться на +1, цикл начинаеться заново

                if Process_Game_live <= 0:
                    Pobeda += 1
                    print('\n\t\t Вы победили по этому вам зачеслен', Pobeda, 'Уровень \n')

                    # Если наша перменная Pobeda  равна 10 то игра закончена
                    if Pobeda == 10:
                        print('\n\n\n\t\t\t Поздравляю вы закончили игру')

                #  Если жизнь врага после первого моего удара все еще больше 0 значит он жив и может нам ответить
                elif Process_Game_live > 0:
                    print('\n\nМоя Очередь ебнуть тебя')
                    num1 = input('Нажми что бы принять удар \n.....')
                    live_guardion -= Process_Game_atack
                    print('Хрясь..... от ', person)
                    print('оствашиеся количество жизней рыцаря',
                          live_guardion)  # прошлая функция где я бью первым
                    input('Нажми для продолжения \n....')

                    # если жизнь рыцаря меньше или равно 0 то мы проиграли цикл завершаеться
                    if live_guardion <= 0:
                        print('Вы проиграли')
                        exit()

        else:
            queshon_fith == queshon_No
            print('Убежали')

        # Если мы соглашаемся происходит  битва









# переменная с функции атаки и жизни рыцаря не сохраняються глобально в цикле а только локально





