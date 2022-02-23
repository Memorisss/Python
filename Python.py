#sep="" разделитель между значениями пишеться вконце строки
#end="" устанавлиевает конец для самой строки "\n" новая строка. ( засчет end можем указать что будет конекретно находиться в самом конце самой этой строки

# print("result sep/end: ", 7,15, sep="", end="!\n")
# print (" \"Second \t \n line")

# Спец символы: \n-(новая строка), \"-(вывод кавычек как символ), \t-(табуляция)

# --------
# Математические Операции
# возведение в степень **
# Округление к целому числу при делении //
# print ("Result //:", 5 // 2)
# ---------

 # Математическии функции min max позволяют найти максимальное или минимальное число
# print ("result max: ", max(5, 6, 3, 2, 0, -1))



# abs - находит число по модулю :если передать отрицательное число будет выводиться положительно -5>5
# print ("result abs: ", abs(-5))

# pow функция возведения число в степень
# print ("result pow: ", pow(5, 3))

# round функция округления числа ( к  ближайшему целому числу)
# print ("result round: ", round(5 / 3))


#abs() находит число по модулю :если передать отрицательное число будет выводиться положительно -5>5
#pow() число возведения в степень анологично 8**3
#round() округление числа
#min() минимальное число
#max() максимальное число



# Получения Данных От пользователя
# input("Введите свой возраст: ")



 # -------------------- 2 урок переменные типы данных

# number = 5 #int
#
# digit = 4.55542 #float
# word = "Result word/digit: " #string
# print (word,digit)
#
# print ("result peremenoy:", number)

# del удаление переменых (дерективой del)
# del number
#
# number = 7
# print ("result peremenoy: ", number)

# булевый тип данных хранения одно их двух значений true false
# boolean = True #bool

# сложение типов данных с помошью функции str преобразует число к строке
# print(word + str(digit))

# int приводит определенную  строку к числу
# str_num ="5" #string
# print (number + int(str_num))
#
# print(word + str(number + int(str_num)))

#print (word,number,str_num) # можно через пробел

# Float bool string int типы данны
# -----------------------------------


# Рабочий пример с выводом пользовательских данных с помошью input

# num1 = int(input("Введите первое число: "))

# num2 = int(input("Введите второе число: "))

# num1 +=5 #добавление к переменной num1

# print ("Result: ", num1 + num2)
# print ("Result: ", num1 - num2)
# print ("Result: ", num1 / num2)
# print ("Result: ", num1 * num2)
# print ("Result: ", num1 ** num2)
# print ("Result: ", num1 // num2)


# word = "Hi"
# print(word * 2)



 # Урок Условные операторы --
# условная конструкция
# if -если
# else -иначе

# if 5 == 5: #Если 5 будет равен 5 то выполниться тот кусочек кода который идет после :  и что отделен одинаковым количеством отступов
#     print ("yes")
#     print ("!!!")

# Значения < меньше, <= меньше или равно , > больше , >= больше или равно , == равенство , != не равенство
#
# user_data = int(input("Введите число: "))
#    if user_data > 5:
#        print ("Number is bigger than 5")



 # Булевые переменные
# isHappy == True сократить можно так isHappy:
# isHappy == False сократить можно так if not isHappy

# user_data = int(input("Введите число: "))
# isHappy = True
# if  isHappy and user_data == 6:
#     print("User  is Happy")
# elif user_data ==5:
#     print ("number is 5")
# else:
#     print ("User is unnhappy")

# Операторы  else в самом конце пишеться сработает елси не сработал код в if
# промежуточный оператор записываеться между if и else   elif дополнительное условие
# если мы хотим проверить две переменных  используем оператор and  if isHappy and user_data == 6: мы говорим что два условия должны быть TRUE
# Оператор OR  or  ему важно что бы хотябы одна из частей являлась верной



 # Тернарный Оператор +
#
# data = input()
#
# number =  5 if data == "Five" else 0

#без теранарного оператора
# if data == 'five':
#     number = 5
# else:
#     number = 0
# print(number)

# print(number)




#----Самостоятельная работа ------------------------------------------------------------------------------------
# Типы данных переменные , условные операторы if elif else . тернарне операторы

# num1 = 12 #int
# num2 = '15' #str
# num3 = 7.25 #float
# num4 = True #bool
# print(  num1 * num3 + int(num2) , num4)



# Main = input("Введите число")
#
# if int(Main)  > 6:
#     print ("ваше число больше  6")
# elif int(Main) == 6:
#     print ("ваше число равно 6")
# else:
#     print (" ты что то перепутал  ")




#обьявление переменной a num1 Тернарный оператор пишеться в одной строке
# num1=11
# #обьявление переменной a num2
# num2=10
# #использование тернарного оператора для проверки наибольшего значения
# result= num1 if num1>num2 else num2
# print("Самое высокое значение: ",result)


#без тернарного оператора с добавлением elif
# num5 = input()
# num6 = input()
# if int(num5)>int(num6):
#     print (num5,"num5 больше чем num6:",num6)
#
# elif int(num5)==int(num6):
#     print (num5,"num5 и",num6,"num6 равны")
#
# else:
#     result = num6
#     print(result,"num6:это число больше чем в num5:" ,num5)



#Тернарный оператор
# num10 = input()
# num11 = 25
# result = int(num10) if int(num10) >= num11 else num11
# print("Самое выское значение", "\n \t:", result )

# Вложенный тернарный оператор
# import random
# num1=random.random()
# num2=random.random()
# print((f"num1:{num1}",f"num2:{num2}") [num1>num2])


#Условные операторы or and
#переменные и типы данных
#Логические  выражения и операторы
#
#
# Попробовать написать задачку в которой ты загадываешь свое число точнее пишешь его в терминале и пк говорит выграл ты или нет если выграл значит твое число больше чем у пк если нет значит меньше
# import random
#
# num1 = input("Введите имя:\n\t")
# print ("Приветствую в нашу небольшую семью:",num1)
# print ("\t Для вас есть одна задачка.\n\t Ответь мне пожалуйста 'Yes' или 'No':")
# num2 = input("Вы готовы?\n\t")
# num3 = "Yes"
# num4 = "No"
# # result = num2 if num3  and num4 else num4 #тернарный способ
# # print(result) №тернарный способ
# result = num2
# if num2 == num3:
#     print ("\t Отлично!")
#     num5 = input("Введите число! \n\t")
#     print("Ваше число",num5,"хорошо!.""\n\t Есть мысли какое может быть число у меня :-) ?")
#     num6 = input("\t")
#     num7 = "Yes"
#     num8 = "No"
#     if num7 == num6:
#         print("А ты смельчак конечно.")
#     elif num8==num6:
#         print ("Ну не всем же обладать такой штукой как смелостью")
#     print ("\nХорошо,давай проверим теперь. \n Кто же из нас выграл.\n")
#     num9= input("\t\tНажми 'Enter' для продолжения.")
#     num10 = 55
#     if int(num5) > num10:
#         print("\t Мои поздравления,ты победил,чёртов гений!")
#     elif int(num5) == num10:
#         print("Ну как говориться, Победила дружба!")
#     else:
#         print("Оп,вот ты и проиграл")
# elif num2 == num4:
#     print("\t Очень Жаль")
# else:
#     print ("Мне кажеться вы что-то перепутали,попробуйте еще раз.")

    # нужно задать список и в условие поставить сравнение с этим списком
    # for i in num10: #цикл for при котром два варианты выграл или проиграл
    #     if int(num5) > i:
    #         print ("Ты победил тове число больше")
    #     else:
    #         print ("Ты проиграл")



#Конец



#----------------------урок 6 циклы и операторы в них-------------------------------


# цикл for переменная i  диапазон метод range() указываем начальное значени 0, конечное значени 6, и оперделенный шаг 2 (1,3,5) ( for удобен для перебора )

# for i in range(1,6, 2):
#     print(i)

# count = 0
# word = "hello world!"
# for i in word:
#     if i == "l":
#         count += 1
# print("Count",count)

# цикл while ) удобно прописать условие и дальше выполнять определенный  цикл
# i = 5
# while i <= 21:
#     print(i)
#     i += 2


# Carsher = True
# while Carsher:
#     if input("Enter data:") == "stop":
#         Carsher = False


# Оператора в Циклах (break оператор берет и выходит из цикла  при определенном условии )
# for i in range(1, 11):
#     if i >= 5: #  если переменная больше или равно 5 то используеться оператор break
#         break
#
#     if i % 2 == 0: # есо при делении на 2 остаток равен 0 используеться continue
#         continue
#
#
#     print(i)

#Нахождение опр символа в строке
# Found = None
# for i in "hello":
#     if i == "R":
#         found = True
#         break #говорим  как только значение true закончить цикл
# else:
#     found = False
# print (found)


#  циклы for  и while ( опереторы break и continue) ( range())


#
# count = 0
# spisok = ['test1','test2','test3','test4']
# for X in spisok:
#     if X == "test2":
#         count += 1
#         print ('Yes',count,X)

#  continue break
# edibles = ["отбивные", "пельмени", "яйца", "орехи"]
#
# for food in edibles:
#     if food == "пельмени":
#         print("Я не ем пельмени!")
#         continue # оператор пропуска  отличаеться от оператора прерывания break тем что не прерывает цикл а продолжает его
#     print("Отлично, вкусные " + food)
# else:
#     print("Хорошо, что не было пельменей!")
# print("Ужин окончен.") #continue break

#функция range() в сочетании с функцие лины len() для получения индекса  и списка
# sliv = ['men','sen','siz','al']
# for i in range(len(sliv)):
#     print(sliv[i],i)




# фнкция enumerate позволяет нам счиать автоматически считать итерации цикла
# my_list = ['яблоко', 'банан', 'вишня', 'персик']
# for c, koll  in enumerate(my_list, 0):
#     print(c,'это индекс','\t\n',koll,'это список')#функция enumirate()

#
#  for num in range(0, 15):
#      print (num)
# функция len для подсчета индекса вместе с функцие range
# car = ['toyta','mers','bmw']
# for i in range(len(car)):
#     print(i,car[i]) # range(len())


### while цикл будет выполняться до тех пор пока условие будет верно  continue и break
#continue функция пропускания пропустить i когда она станет равна 3 и выводить дальше
# i = 0
# while i < 11:
#     i += 1
#     if i == 3:
#         continue
#     print (i)
# break функция перывания выводить пока j  не будет равна 2 как только j станет равно 2 остановить
# j = 0
# while j < 5:
#     print(j)
#     j += 1
#     if j == 2:
#         break
# while просто  пока 30 больше 19 выводить переменную num1 но при этом после каждого сравнения отнимать -2
# num1 = 30
# while num1 > 19:
#     print (num1)
#     num1 -= 2

#цикл бесконечный пока не введшь stop
#
# num1 = True
# while num1:
#     print("остановиться можно вести stop")
#     if input("enter data ") == 'stop':
#         num1 = False
#     else:
#         print('ты ввел неправильно')




# Правильное условие for
# found = None
# car = ['Python','C++','C#','Perl']
# for i in car:
#     if i == 'C#$':
#         found = True
#         break
# else:
#     found = False
# print(found)


#                                       след урок списки----------------------

# nums = [5, 7, 10, 12, 15, True,[1, 5]]
#
# nums[0] = 50
# nums[5] = 1.01
#
# print (nums[-1][1])



#функции метод .append() / .insert(индекс,значение) , extend([])
# number = [1, 2, 7]
# number.append(100)
# number.insert(1,55)
# number.insert(4,234)
# number.extend([False,True])
#
#
# b = [ 11, 22, 33, 11]
# number.extend(b)
#
# number.sort() #sort()  с начала с 0 до макс и reverse()  с конца
# number.pop() # удаляет последний елемент или по индексу если передать
# number.remove(False)
# number.remove(True) #удаляет опр элемент
# number.remove(True)

# number.clear() # очищение полного списка

# print(len(number)) #len() передаем в скобки название списка и выводит его длину сколько в списке элементов
# print(number.count(11)) # count() количество совпадений например в условие пишем 2 и ищет сколько в списке двое2к




# n = int(input("Enter lenght: "))
#
# user_list = []
#
# i = 0
#
# while i < n:
#     stroc = "Enter Element #" + str(i + 1) + ": "
#     user_list.append(input(stroc))
#     i += 1
#
# print(user_list)




#----------------работа со списками

# num10 = [10, 2, 15, 1, 25]
# # num10.append(3)#добавление элемента в конец списка
# # num10.insert(2,21)# добавление эелемента под определенным индексом
# # num10.extend([8,7,6])
# # b = [4,False,True,4.2]
# # num10.extend(b) #Добавление нескольких элементов в список
# # num10.reverse() # сортировка с конца.Анологичная команда num10.sort()
# # num10.pop(1) #удаляет последний элемент из списка.Или под определенным индексом
# # num10.remove(False) #удаляет елемент из списка по его названию
# num10.clear() # полное очищение списка
# num10.extend([True,False,10,50,60,2,4,9,23,'Helloy'])
# #
# User = int(input('Введите елемент который хотите проверить  :\t')) # переменная в которой пользователь вводит данные на проверку

#цикл который проверяет вводимые данные от пользователя на наличии их в списке, в случае не нахождения елемента, можно добавить в список эелемент пользователя
# for i in range(len(num10)):
#     if User == num10[i]:
#         print('Элемент :\t' , num10[i] ,': присуствует ')
#         print('Элемент :', num10[i], '\t :Индекс\t', i)
#         break
# else:
#     print('Erorr,not found element. \t\n ')
#     what = input('\tХотите ли вы добавить этот элемент в список? \t:')
#     yes = "Yes"
#     no = "No"
#     if what == yes:
#         num10.append(User)
#         print("Елемент :",User," добавлен в список ")
#     elif what != no:
#         print('Что то пошло не так, я вас не понял :\t',what,'\n Я понимаю только:',yes,'/',no)
#     else:
#         what == no
#         print("Вы,не добавили елемент в список :")
#
# print('\n\tДлина списка состовляет :',len(num10),' Елементов','\n\t',num10)

# print('\nколичество совпадений: ',num10.count(True),'\nДлина списка :',len(num10),'\n\t',num10)





#создание списка задаем длину и елемента урок 7 списки
# user = int(input('Длина списка'))
# count = 0
# user_list = []
#
# while count < user :
#     string = 'Элемент ' + str(count) + ' :'
#     user_list.append(input(string))
#     count += 1
#     if count > 15:
#         print ("Длина вышего списка превысила порог ")
#         exit(user_list)
# print(user_list)




############################                               функции строк индесы и срезы
#word.upper() функция ввода в верхнем регистре
#word.lower() вывод в нижнем регистре
#islower () проверка в нижнем регистре
#isupper() являеть ли элемент в верхнем регистре
#capitalize() первый символ в верхнем регистре
#find('l') поиск и воврат индекса
#split (',') разбивание строки на список
#join узнать что за это метод ??????????????????????????????????????????????????????????????????????????????????????
# word = 'helloy vlad rizjal'
# spisok = word.split()
# #print(len(spisok),'\n',spisok[1])
#
# for i in range(len(spisok)): # до длины самого списка будет идти список
#     spisok[i] = spisok[i].capitalize()
#
# result = ', '.join(spisok)
# print(result)




###################################                                     Индексы и срезы
#
# word = 'Football'
# #срезы
# print(word[0:-1:2]) # срезы стартовый элемент и конечный елемент также можно пересскакивать через симво 0:-1:2 один индекс будет пропускать (шаг)


# lis = [6, 5, 'Stroka', True, 4.5]
# print(lis[2:5:2])
# print(lis[::-1]) # список начинаеться с конца
# print(lis[::-2]) # список  начинаеться сконца пропуская элемент через 1
# print(lis[::2]) # список начинаеться с начала пропуска элеент черзе 1
#


# imp = 'Helloy Vladislav this is test message'
# list = imp.split()
#
# for i in range(len(list)):
#     list[i] = list[i].capitalize()
#     # print(i,': ',list[i])
#
# result = ', '.join(list) # join обьединяет список обратно в строку
# print(result)


# test = [1,2,4, 'True+',False,4.5]
# print(test[0:3:2])


# #find
# fin = 'bradabra'
# print(fin.find('d')) # поиск символа в строке с возлрпатом его индекса


#                                                        кортежи
#Кортежи теже самые списки только весят меньше и нельзя видо изменять как списки присваивать новое значение уже существующему эелементу в кортеже

#tuple с англиского это именно кортеж


#data = (3,4,5,10,True,4.5,'False')
#data[0] = 4        вот так нельзя делать как со списком в кортеже

#print(data[1:5])

#print(data.count(4))
#print(len(data))


#data = 5,6,True
#print(data)

#data = (5,)# (5) один елемент не кортеж . нужно добавить запятую после 5 тогда будет считаться элементом
#print(data)



# kortezh = 5,10,False,'Helloy'
# for i in kortezh:
#     print(i)
# #
# list_kortezh = [5,6,7,10,True,'list']
# new_kortezh = tuple(list_kortezh)
#
# word = tuple('Helloy world !')
#
# print(new_kortezh,' - это кортеж','\n',
#       list_kortezh,' - это список','\n',
#       word,' - это кортеж изи строки ')



#                                                   Словари dict и работа с ними


#при созаднии словаря  указываеться ключ и его елемент {4: 3}
#country = {'code': 'RU','name':'Russian','popelation':144}
#print(country['code'])

#dict функция
#country = dict(code='Ru',name='Russian')


#country = {'code': 'RU','name':'Russian','popelation':144}

#print(country.items()) фукнция items получае каждый елмент ключ + значение

#for key, value in country.items(): # если мы хотим обращаться к елементам словоря а не только к ключам создаем две переменных и добавляем функцию .items()
#     print(key,' - ',value)


# country = {'code': 'RU','name':'Russian','popelation':144}
#функции при работе со словорями
#.get('name') метод get анологичен ['name'] и позволяет получить елемент по определенному ключу
# country.clear() очищение словаря
#
#
#country.clear()
#country.pop('name') # удаление опр елемента по ключу
#country.popitem() #удаление последнего елемента в нашем словаре без указания определенного ключа


#print(country.keys()) если мы хотим получить исключительно ключи обращаемся к фукнции .keys()
#print(country.values()) если мы хотим получить значение а не ключи обращаемся к функции .values()
#print(country.items()) если мы хотим получить и ключи и значение обращаемся к фукнции items где каждый елемент это опр картеж состоящий из двух элементов ключ и значение

#country['code'] = 'None' обновление или изменение значения по обращению  к ключу
#code = {5:3,10:True}
#country.update(code) #фукнция обновления словаря
#print(country.items())



#                                   Внутрь словаря вместо значения можно помещать еще один словарь


# person = {
#     'User_1': {
#         'firs_name':'john',
#         'last_name':'Marley',
#         'age':45,
#         'adder':['r. Moscow','улица. какя - то','45'],
#         'grades':{'Matem':45,'physic':50}
#
#     },
#     'User_2':{
#
#     }
# }
# #задача из словаря person где создан еще один словарья User_1  вывести adder  где создан список . вывести   улица. какя - то индекс 1
#
# print(person['User_1']['adder'][1])




# словарь
# data2 = {
#     'User_1': {
#         'ima':'vlad',
#         'fam':'zelenskiy',
#         'age':23,
#         'region':['kz','ru','almaty','kzo'],
#         'adress':{'kv':18,'dom':13,'kv2':31,'dom2':'502A'}
#     },
#     'User_2':{
#         'Oficial':'Kazahstan'
#     }
# }
# print(data2['User_1']['adress']['dom2'])


#country = dict(code='RU',name='Russian') #анологичный способ использования словоря
#print(country)



#                                       Множества
#data = set('helloy') #перывый способ создания множества через set

# data = {5,2,3,5,2,1,6,8,9,10,2} # второй способ создания множества без ключа как в словаре
# data.update([50,'32',True])
# data.remove(True)
# data.pop()
# data.add(100)
#data.clear()



#пример испольхования множества в списке

# nums = [5,10,20,30,40,50,5,10,5]
# nums_new = set(nums)
#
# print(len(nums),'\n',
#       len(nums_new),':',
#       nums_new)

#----               Frozenset - замороженное множество
# что такое frozenset это кортеж + множество нельзя видоизменять добовлять так же как и в кортеже


# new_data = frozenset([5,10,5,6,'32',True,20,5,6,50,10,'32'])
# new_data.add(5) #нельзя
# print(new_data)


#                                           ------- функции def lambda

# def test_func():
#     print('Hello')
#
#
# test_func()



# def test_func():
#     print('Hello')
#
#
# test_func()

#
# def test_func(word):
#     print(word)
# test_func("Hi")

#return  что конкретно будет возвращаться из функции
# def summa(a, b):
#     # res = a + b # мможно сократить передав сложение сразу return
#     return a + b
# res = summa(5.5, 7.7)
# print(res)
# print(summa('H', 'i'))


# nums1 = [5,7,9,1.99]
# min = nums1[0]
# for i in nums1:
#     if i < min:
#         min = i
# print(min)


#  вынесли код в отдельную функцию, который позволяет сылаться к нему а не писать один и тот же код для каждого списка и тд тп
# def minimal (l):
#     min_number = l[0]
#     for i in l:
#         if i < min_number:
#             min_number = i
#     return min_number
#
# min1 = minimal(nums1)
# nums2 = [5,7,9,4,2.1,8.5,2.0]
# min2 = minimal(nums2)
#
# if min1 < min2:
#     print(min1)
# else:
#     print(min2)



# анонимные функции lambda

# func = lambda  x, y: x * y
# res = func(5, 8)
# print(res)
#
#
# def fucnkscion(num1, num2,num3):
#     res = num1 * num2 + num3
#     return res
#
# res = fucnkscion(5,10,5)
# print(res)
# # fucnkscion('hi','fo','t')


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



                                                       # python innopolis

# # Проверака начинаеться ли строка  с starswith(" ") и заканчиваеться ли строка на endswith(" ")
# num = 'Первая строка'
# print(num.startswith('Первая'))
# print(num.endswith('строка'))

