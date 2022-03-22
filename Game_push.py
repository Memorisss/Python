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
queshon_fit =('\n Что будем делать \n....\n\n Атаковать (1) \n Убежать (2)\n.....')
yes = '1'
no = '2'
# Создание цикла
while Pobeda < 10:
    person_random = Process_Game_Person + Process_Game_Bonus_Live + Process_Game_Bonus_Attack  # рандомный персонаж / бонус в одной переменной
    person = random.choice(person_random)
    Process_Game_live = random.randint(1, 30)  # рандмоное число жизни
    Process_Game_atack = random.randint(1, 15)  # рандомное число атаки
    num = input('Отпровляемся в путь ........')




# функция Боя
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

#  если выпадает бонусные предметы
    if person == 'Зачарованный Мечь':
        attack_guardion += Process_Game_atack + 2
        print('Великолепно перед вами ,', '"', person, '"', 'Дполнительный урон увеличился на  +',
              Process_Game_atack + 2,
              '\n Ваша атака равна:', attack_guardion)


    elif person == 'Яблоко':
        live_guardion += Process_Game_live
        print('Вам попался Игровой бонус :', '"', person, '"', 'Дополнительная жизнь увеличина на +', Process_Game_live,
              '\n Ваша жизнь равна:', live_guardion)


# или на нашем пути встречаеться монстр
    elif person:
        print('\n\n\nНа вашем пути,', person, 'Его жизнь', Process_Game_live, 'Сила Атаки :', Process_Game_atack)
        queshon_fith = input(queshon_fit)
        if queshon_fith == yes:
            print('Погнали')
            fight(person)

        elif queshon_fith == no:
            print('Убежали')

#  если мы вводим не понятные символы
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