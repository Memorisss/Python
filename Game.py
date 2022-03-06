import random

# жизнь и сила атаки нашего героя
live_guardion = 10
attack_guardion = 10

# Создания списка с  монстрами
Process_Game_Person = ['Троль', 'Кутикула', 'Злой китаец', 'Украинец', 'Крип', 'Дотер']
# Создание бонусов
Process_Game_Bonus_Attack = ['Лук', 'Зачарованный Мечь']
Process_Game_Bonus_Live = ['Яблоко', 'Золотое яблоко']


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
    queshon_bonus_Yes = '1'
    queshon_bonus_No = '2'

    # print('Ваш нынещний урон ',attack_guardion) # Проверка добавился ли урон

    # Проверка бонусных предметов если выпадает даеться 2 выбора взять или не взять
    # Лук
    if person == 'Лук':
        print('Повезло вы нашли, ', '"', person, '"', 'Дополнительный урон +', Process_Game_atack)
        queshon_bonus = input('Что делаем ? \n ..... \n Берем (1) \n Не берем (2) \n.... \t')

        if queshon_bonus == queshon_bonus_Yes:
            attack_guardion += Process_Game_atack
            print('Ваша сила атаки теперь увеличина на ', attack_guardion)


        elif queshon_bonus == queshon_bonus_No:
            print('Вы не подобрали, ', '"', person, '"', ',урон мог увеличиться на +', Process_Game_atack)


        # Повторяющийся цикл если мы вводим не то значение при ответе на вопрос берем или нет
        elif queshon_bonus != queshon_bonus_Yes and queshon_bonus_No:
            print('\n\t "Я вас не понял, введите (1) либо (2)" ')
            while queshon_bonus != queshon_bonus_Yes and queshon_bonus_No:
                queshon_bonus = input('Что делаем ? \n ..... \n Берем (1) \n Не берем (2) \n.... \t')

                # Если  отвечаем да  то цикл завершаеться изменения вступают в силу
                if queshon_bonus == queshon_bonus_Yes:
                    attack_guardion += Process_Game_atack
                    print('Ваша сила атаки теперь увеличина на ', attack_guardion)
                    break
                # если отвечаем нет то цикл заканчиваеться все отсаеться не изменным
                elif queshon_bonus == queshon_bonus_No:
                    print('Вы не подобрали, ', '"', person, '"', ',урон мог увеличиться на +', Process_Game_atack)
                    break

    #  для всех бонуссынх предметов анологично

    #         Зачарованный Мечь
    elif person == 'Зачарованный Мечь':
        print('Великолепно перед вами ,', '"', person, '"', 'Дполнительный урон +', Process_Game_atack + 2)
        queshon_bonus = input('Что делаем ? \n ..... \n Берем (1) \n Не берем (2) \n.... \t')

        if queshon_bonus == queshon_bonus_Yes:
            attack_guardion += Process_Game_atack + 2
            print('Ваша сила атаки теперь увеличина на', attack_guardion)


        elif queshon_bonus == queshon_bonus_No:
            print('Вы не подобрали, ', '"', person, '"', ',урон мог увеличиться на +', Process_Game_atack + 2)

        # Повторяющийся цикл если мы вводим не то значение при ответе на вопрос берем или нет
        elif queshon_bonus != queshon_bonus_Yes and queshon_bonus_No:
            print('\n\t "Я вас не понял, введите (1) либо (2)" ')

            while queshon_bonus != queshon_bonus_Yes and queshon_bonus_No:
                queshon_bonus = input('Что делаем ? \n ..... \n Берем (1) \n Не берем (2) \n.... \t')

                if queshon_bonus == queshon_bonus_Yes:
                    attack_guardion += Process_Game_atack
                    print('Ваша сила атаки теперь увеличина на ', attack_guardion)
                    break

                elif queshon_bonus == queshon_bonus_No:
                    print('Вы не подобрали, ', '"', person, '"', ',урон мог увеличиться на +', Process_Game_atack)
                    break


    # Яблоко
    elif person == 'Яблоко':
        print('Вам попался Игровой бонус :', '"', person, '"', 'Дополнительная жизнь +', Process_Game_live)
        queshon_bonus = input('Что делаем ? \n ..... \n Берем (1) \n Не берем (2) \n.... \t')

        if queshon_bonus == queshon_bonus_Yes:
            live_guardion += Process_Game_live
            print('Ваше здоровье теперь равно = ', live_guardion)


        elif queshon_bonus == queshon_bonus_No:
            print('Вы не взяли,', person, 'жизнь могла увеличиться на +', Process_Game_live)

        elif queshon_bonus != queshon_bonus_Yes and queshon_bonus_No:
            print('\n\t "Я вас не понял, введите (1) либо (2)" ')

            # Повторяющийся цикл если мы вводим не то значение при ответе на вопрос берем или нет
            while queshon_bonus != queshon_bonus_Yes and queshon_bonus_No:
                queshon_bonus = input('Что делаем ? \n ..... \n Берем (1) \n Не берем (2) \n.... \t')

                if queshon_bonus == queshon_bonus_Yes:
                    attack_guardion += Process_Game_atack
                    print('Ваша сила атаки теперь увеличина на ', attack_guardion)
                    break

                elif queshon_bonus == queshon_bonus_No:
                    print('Вы не подобрали, ', '"', person, '"', ',урон мог увеличиться на +', Process_Game_atack)
                    break


    #     Золотое яблоко
    elif person == 'Золотое яблоко':
        print('Поздравляю вам попалось, ', '"', person, '"', 'Дополнительная жизнь +', Process_Game_live + 4)
        queshon_bonus = input('Что делаем ? \n ..... \n Берем (1) \n Не берем (2) \n.... \t')

        if queshon_bonus == queshon_bonus_Yes:
            live_guardion += Process_Game_live + 4
            print('Ваше здоровье теперь равно = ', live_guardion)


        elif queshon_bonus == queshon_bonus_No:
            print('Вы не взяли,', person, 'жизнь могла увеличиться на +', Process_Game_live + 4)

        elif queshon_bonus != queshon_bonus_Yes and queshon_bonus_No:
            print('\n\t "Я вас не понял, введите (1) либо (2)" ')

            # Повторяющийся цикл если мы вводим не то значение при ответе на вопрос берем или нет
            while queshon_bonus != queshon_bonus_Yes and queshon_bonus_No:
                queshon_bonus = input('Что делаем ? \n ..... \n Берем (1) \n Не берем (2) \n.... \t')

                if queshon_bonus == queshon_bonus_Yes:
                    attack_guardion += Process_Game_atack
                    print('Ваша сила атаки теперь увеличина на ', attack_guardion)
                    break

                elif queshon_bonus == queshon_bonus_No:
                    print('Вы не подобрали, ', '"', person, '"', ',урон мог увеличиться на +', Process_Game_atack)
                    break

    # Если встречаеться монстр
    elif Process_Game_Person:
        print('\n\n\nНа вашем пути,', person, 'Его жизнь', Process_Game_live, 'Сила Атаки :', Process_Game_atack)
        queshon_fith = input('\n Что будем делать \n....\n\n Атаковать (1) \n Убежать (2)\n.....')

        # Если мы соглашаемся происходит  битва
        if queshon_fith == '1':
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
                    print('оствашиеся количество жизней рыцаря', live_guardion)  # прошлая функция где я бью первым
                    input('Нажми для продолжения \n....')

                    # если жизнь рыцаря меньше или равно 0 то мы проиграли цикл завершаеться
                    if live_guardion <= 0:
                        print('Вы проиграли')
                        exit()


        else:
            queshon_fith == '2'
            print('Убежали')
