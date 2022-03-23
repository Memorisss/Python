import random
# жизнь и сила атаки нашего героя
live_guardion = 10
attack_guardion = 10

# Создания списка с  монстрами
Process_Game_Person = ['Троль', 'Кутикула', 'Злой китаец', 'Украинец', 'Крип', 'Дотер']
# Создание бонусов
Process_Game_Bonus = [ 'Зачарованный Мечь','Яблоко']



# функция Боя Рыцаря и Чудовишь
def fight(a: str):
    global Process_Game_live
    global attack_guardion
    global person
    global live_guardion
    global Pobeda
    global Process_Game_atack
    while Process_Game_live >= 0:
        print('\n Тыщь.........')
        Process_Game_live -= attack_guardion
        print('Осталось', Process_Game_live, 'жизней у', person)

        if Process_Game_live <= 0:
            Pobeda += 1
            print('Вам зачеслен ', Pobeda ,' уровень')
            if Pobeda == 10:
                print('Поздравляю вы закончили игру')

        elif Process_Game_live > 0:
            print('\n \t', person, ' : " Моя очередь отвечать тебе" ')
            live_guardion -= Process_Game_atack
            print('Хрясь...... от ', person, '\n\t Оставшиеся количество жизней у Рыцаря :', live_guardion)

            if live_guardion <= 0:
                print('Вы проиграли')
                exit()
    return








# Создание переменной для цикла
Pobeda = 0
# Создание переменных в ходе процесса игры с выбором действия
queshon_fit =('\n Что будем делать \n....\n\n Атаковать (1) \n Убежать (2)\n.....')
yes = '1'
no = '2'
queshon_bonus = ('Что делаем ? \n ..... \n Берем (1) \n Не берем (2) \n.... \t')


# Создание цикла ( Цикл будет длиться до тех пор пока переменная Pobeda меньше 10 )
while Pobeda < 10:

    person_random = Process_Game_Person + Process_Game_Bonus  # рандомный персонаж и бонусы в одной переменной
    person = random.choice(person_random) #  рандомное выпадание одного game процесса
    Process_Game_live = random.randint(1, 30)  # рандмоное число жизни
    Process_Game_atack = random.randint(1, 20)  # рандомное число атаки

    num = input('Отпровляемся в путь ........')

# Построение функции проверок

# Если выпадает "Зачарованный Мечь" предлагаеться выбор подобрать его или не брать в зависимости от количества урона меча

    if person == 'Зачарованный Мечь':
        print('Великолепно перед вами ,', '"', person, '"', 'его сила атаки равна :', Process_Game_atack + 2)
        queshon_b = input(queshon_bonus)

        if queshon_b == yes:
            attack_guardion = Process_Game_atack + 2
            print('Вы подобрали мечь, сила атаки равна :', attack_guardion)

        elif queshon_b == no:
            print('Вы не подобрали, ', '"', person, '"  c силой атаки :', Process_Game_atack + 2)

# Проверка если мы вводим не понятные символы
        elif queshon_b != yes or no:
            print('\n\t "Я вас не понял, введите (1) либо (2)" ')

            while queshon_b != yes or no:
                queshon_b = input(queshon_bonus)

                if queshon_b == yes:
                    attack_guardion = Process_Game_atack + 2
                    print('Ваша сила атаки теперь равна : ', attack_guardion)
                    break

                elif queshon_b == no:
                    print('Вы не подобрали, ', '"', person, '"', ',c cилой атаки :', Process_Game_atack + 2)
                    break


# Если выпадает яблоко автоматически персонаж его сьедает
    elif person == 'Яблоко':
        live_guardion += Process_Game_live
        print('Вам попался Игровой бонус :', '"', person, '"', 'Дополнительная жизнь увеличина на +', Process_Game_live,
              '\n Ваша жизнь равна:', live_guardion)


# Или на нашем пути встречаеться монстр
    elif person:
        print('\n\n\nНа вашем пути,', person, 'Его жизнь', Process_Game_live, 'Сила Атаки :', Process_Game_atack)
        queshon_fith = input(queshon_fit)
        if queshon_fith == yes:
            print('Погнали')
            fight(person)

        elif queshon_fith == no:
            print('Убежали')

#  Если мы вводим не понятные символы
        else:
            print('Я вас не понял ')
            if queshon_fith != yes:
                while queshon_fith != yes:
                    queshon_fith = input(queshon_fit)
                    if queshon_fith == yes:
                        fight(person)

                    elif queshon_fith == no:
                        print('Убежали')
                        break
