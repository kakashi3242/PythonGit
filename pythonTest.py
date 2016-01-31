#
# album = ['Black', 'Back', 'Kill', 24, True]
# album.append('MAR')
# print(album)
# print(album[0])
# print(album[-1])


# if语句
# def account_login():
#     password = input('Password:')
#     password_correct = password == '111'
#     if password_correct:
#         print('LOGIN SUCCEED')
#     else:
#         print('LOGIN FAILED')
#
# account_login()


# 密码重置
# password_list = ['*#*#', '111111']
#
#
# def account_login():
#     password = input('PASSWORD:')
#     password_correct = password == password_list[-1]
#     password_reset = password == password_list[0]
#
#     if password_correct:
#         print('LOGIN SUCCEED!')
#
#     elif password_reset:
#         new_password = input('ENTER NEW PASSWORD:')
#         password_list.append(new_password)
#         print('CHANGE SUCCESS!')
#         account_login()
#
#     else:
#         print('LOGIN FAILED')
#         account_login()
#
# account_login()


# for循环
# for i in range(11):
#     print(str(i) + ' + 1 = ', i + 1)

# songList = ['Holy Shit', 'Thunder', 'Rebel']
# for song in songList:
#     if song == 'Holy Shit':
#         print(song, '01')
#     elif song == 'Thunder':
#         print(song, '02')
#     elif song == 'Rebel':
#         print(song, '03')


# 乘法口诀
# for i in range(1, 10):
#     for j in range(1, 10):
#         print('{} × {} = {}'.format(i, j, i*j))


# while循环
# i = 0
# while i < 3:
#     i+= 1
#     print('i < 3')


# 出错三次就禁止输入密码
# password_list = ['*#*#', '111111']
#
#
# def account_login():
#     tries = 3
#     while tries > 0:
#         password = input('PASSWORD:')
#         password_correct = password == password_list[-1]
#         password_reset = password == password_list[0]
#
#         if password_correct:
#             print('LOGIN SUCCEED!')
#
#         elif password_reset:
#             new_password = input('ENTER NEW PASSWORD:')
#             password_list.append(new_password)
#             print('CHANGE SUCCESS!')
#             account_login()
#
#         else:
#             print('LOGIN FAILED')
#             tries-= 1
#             print(tries, 'times left')
#     else:
#         print('NOT ALLOW')
#
# account_login()


# import random
#
# a = random.randrange(1, 7)
# b = random.randrange(1, 7)
# c = random.randrange(1, 7)
#
# print(a, b, c)




# >>>>>>>>>>>>>>>>>>>> python foundation <<<<<<<<<<<<<<<<<<<<

#
# d = {
#     'name':'JJ',
#     'skill':'no-dead',
#     'keyi':'ky'
# }
# # d.pop('keyi')
# # print(d)
#
# List = list('fuckyou')
# # print(List)
#
# from string import Template
#
# words = Template('Everything will be $x')
# word = words.substitute(x = 'ok')
# print(word)
#
#
# def getpage():
#     return None
# import math
#
# print(math.pi)


# name = 'This is my way'
# name = name.replace('my', 'your')
# print(name)

# a = 'foot'
# b = 'ball'
# c = a + b
# print(c)

# name = input('What is your name?\n')
# if name.endswith('Mar'):
#     print('Hello Mr.Mar!')

# word = ['my', 'name', 'is', 'your', 'dad']
# number = ['139', '123', '234', '4555', '666']
# for w in word:
#     print(w)
# print(word.index('my'))
# num = number[word.index('name')]
# print(num)

# from pip._vendor.distlib.compat import raw_input
#
# while True:
#     word = raw_input('Enter a word: \n')
#     if not word: break
#     print('Your word is ' + word)

# def chage_name(n):
#     n = 'Mr.J'


# a = [1, 2, 3, 4]
# a.append(0)
# print(a)


phone_book = {
    'Alex':{
        'phone':'123',
        'adrr':'ningbo'
    },

    'MAR':{
        'phone':'15757870527',
        'addr':'anhui'
    },

    'MT':{
        'phone':'15726816113',
        'addr':'hangzhou'
    }

}
name = input('Input your name:\n')
print(phone_book[name]['phone'])
print(phone_book[name]['addr'])







