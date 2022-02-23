                                       # функция поиска наименьшего чилса
def fun1(val):
    min_number = val[0]
    for i in val:
        if i < min_number:
            min_number = i
    return min_number

                                                # фукнция перебера
def perebor (l):
    for i in range(len(l)):
        print('Елемент : ',l[i],end= ' : ')
        print('Индекс  = ', i)
    return i

message = int(input('Вас приветсвует Tom ! \n Введи длину словаря который хочешь создать  :'))
count = 0
user_list = []
while message > count:
    shablon = 'Element \t : '
    user_list.append(int(input(shablon)))
    count += 1
print('Ваш список содержит следующие елементы : ',user_list, '\n')
minimal = fun1(user_list)
print(' \n Наименьший елемент в вашем созданном списке : ',minimal,'\n')
print('Елменты и их Индексы :')
# переменная в которую передана функция перебора и опр список который будет перебираться
pr = perebor(user_list)

num = (1,3,4,5,7,10,23)
# print(type(num))
