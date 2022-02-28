# import random
# import string
#
# dlina = 10
# collections = [string.ascii_lowercase]
# collections2 = [string.ascii_uppercase]
# collections3 = [string.digits]
# punctuations = ['!','@','#','$']
# full = random.choice(collections) + random.choice(punctuations) + random.choice(collections2) + random.choice(
#         collections3)
#
# passw = ''
#
# # цикл создания пароля с определенной длиной
# for i in range(dlina):
#     passw += random.choice(full)
#
# print('Длина пароля :',len(passw),'\n','passw : ',passw,'\n Если пароль будет надежный программа скажет: correct')
#
#
# for x in passw:
#     if   x.islower() + x.isdigit() + x.isupper() :
#         print()
#     elif x in string.punctuation:
#         print('corect password')
#



######################################################################################################################
######################################################################################################################
######################################################################################################################
######################################################################################################################
######################################################################################################################
######################################################################################################################


# import random
# import string

# dlina = 10
# collections = [string.ascii_lowercase]
# collections2 = [string.ascii_uppercase]
# collections3 = [string.digits]
# punctuations = ['!','@','#','$']
# passw = ''

#
# # цикл создания пароля с определенной длиной

# for i in range(dlina):
#     full = random.choice(collections) + random.choice(punctuations) + random.choice(collections2) + random.choice(
#         collections3)
#     passw += random.choice(full)
#
# print('Длина пароля :',len(passw),'\n','passw : ',passw)


# # перебор циклами и условиями  нашего пароля для каждого из условий если все проверки True в конце выведется пароль коректный и программа закроеться
#
# num = print('Next.')
#
# for simvl in passw:
#     if simvl in string.punctuation:
#         for digit in passw:
#             if digit.isdigit():
#
#                 for upper in passw:
#                     if upper.isupper():
#
#                         for lower in passw:
#                             if lower.islower():
#                                 print('" \t Yes this is password correct !"')
#                                 exit()
#



# доп перебор как вариант


# # перебор  циклами  которые выводят определенные значения из проверки
# for ps in passw:
#     if ps in string.punctuation:
#         print('Символы : ',ps)
#
# for digit in passw:
#     if digit.isdigit():
#         print('Цифры :',digit)
#
# for upper in passw:
#     if upper.isupper():
#         print('Upper :',upper)
#
# for lower in passw:
#     if lower.islower():
#         print('Lower :',lower)




######################################################################################################################
######################################################################################################################
######################################################################################################################
######################################################################################################################
######################################################################################################################
######################################################################################################################


# 1 используеться один список включающий все содержимое но вместо опр символов используеться  string.punctuation

# import random
# import string

# dlina = random.randint(10,10)
# collections = [string.ascii_lowercase,string.ascii_uppercase,string.digits,string.punctuation]
# passw = ''

# for i in range(dlina):
#     collection = random.choice(collections)
#     passw += random.choice(collection)
#

# print('Длина пароля :',len(passw),'\n','passw : ',passw)
#

# # Перебор passw с условием проверки
# for x in passw:
#     if   x.islower() + x.isdigit() + x.isupper() :
#         print(x)
#     elif x in string.punctuation:
#         print(x)
