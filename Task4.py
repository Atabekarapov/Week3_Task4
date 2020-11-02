# TASK4  HOMEWORK ------> ATABEK
# 1)

# num = int(input('Enter your number: '))
# num2 = int(input ('Enter your second number: '))
# try:
#     res = num / num2
#     print(res)
# except ZeroDivisionError:
#     print('Divide to zero PROHIBITED!!!🤓')
# else:
#     print('WOW good job!')
# finally:
#     print('Program ended')

# 2)
# flag = True
# while flag:
#     num1 = input('Enter the first number: ')
#     num2 = input('Enter the second number: ')
#     try:
#         res = int(num1) + int(num2)
#         print(res)
#         break
#     except ValueError:
#         print('Вы задали неправильный параметр, инпут ожидает число!🤓')
#         continue
#     finally:
#         print('Program ended!😂')

# 3)

# dict_ = {'key1': 'value1', 'key2': 'value2'}
# try :
#     dict_['key3']
# except KeyError :
#     raise Exception('No words like this in dictionary!')

# 4)
# int_ = input('Enter your number: ')
# try:
#     if int_.startswith('(') and int_.endswith(')'):
#         print('WOOOOOW!!!')
#     elif int_ != int_.startswith('('):
#         raise TypeError ('Данная программа принимает только integer!!')
# finally:
#     print('Byeeee')

# 5)
# list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# length = len(list_) - 0
# try:
#     list_[10]
# except IndexError:
#     raise Exception (f'{length} - last index')