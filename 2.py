# Попробовать написать задачку в которой ты загадываешь свое число точнее пишешь его в терминале и пк говорит выграл ты или нет если выграл значит твое число больше чем у пк если нет значит меньше
import random
num1 = input("Введите имя:\n\t")
print ("Приветствую в нашу небольшую семью:",num1)
print ("\t Для вас есть одна задачка.\n\t Ответь мне пожалуйста 'Yes' или 'No':")
num2 = input("Вы готовы?\n\t")
num3 = "Yes"
num4 = "No"
# result = num2 if num3  and num4 else num4 #тернарный способ
# print(result) №тернарный способ
result = num2
if num2 == num3:
    print ("\t Отлично!")
    num5 = input("Введите число! \n\t")
    print("Ваше число",num5,"хорошо!.""\n\t Есть мысли какое может быть число у меня :-) ?")
    num6 = input("\t")
    num7 = "Yes"
    num8 = "No"
    if num7 == num6:
        print("А ты смельчак конечно.")
    elif num8==num6:
        print ("Ну не всем же обладать такой штукой как смелостью")
    print ("\nХорошо,давай проверим теперь. \n Кто же из нас выграл.\n")
    num9= input("\t\tНажми 'Enter' для продолжения.")
    num10 = 55
    if int(num5) > num10:
        print("\t Мои поздравления,ты победил,чёртов гений!")
    elif int(num5) == num10:
        print("Ну как говориться, Победила дружба!")
    else:
        print("Оп,вот ты и проиграл")
elif num2 == num4:
    print("\t Очень Жаль")
else:
    print ("Мне кажеться вы что-то перепутали,попробуйте еще раз.")
# нужно задать список и в условие поставить сравнение с этим списком
    for i in num10: #цикл for при котром два варианты выграл или проиграл
        if int(num5) > i:
            print ("Ты победил тове число больше")
        else:
            print ("Ты проиграл")



#Конец