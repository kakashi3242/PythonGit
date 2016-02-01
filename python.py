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


# >>>>>>>>>>>>>>>>>>>> python 数据库操作 <<<<<<<<<<<<<<<<<<<<


# import random
#
# a = random.randrange(1, 7)
# b = random.randrange(1, 7)
# c = random.randrange(1, 7)
#
# print(a, b, c)

# coding=utf-8


# 连接数据库
# import MySQLdb
#
#
# db = MySQLdb.connect("localhost", "root", "123", "TESTDB" )
#
# cursor = db.cursor()
#
# cursor.execute("SELECT VERSION()")
#
# data = cursor.fetchone()
#
# print "Database version : %s " % data
#
# db.close()


# 数据库建表
# import MySQLdb
#
# # 打开数据库连接
# db = MySQLdb.connect("localhost", "root", "123", "TESTDB" )
#
# # 使用cursor()方法获取操作游标
# cursor = db.cursor()
#
# # 如果数据表已经存在使用 execute() 方法删除表。
# cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
#
# # 创建数据表SQL语句
# sql = """CREATE TABLE EMPLOYEE (
#          FIRST_NAME  CHAR(20) NOT NULL,
#          LAST_NAME  CHAR(20),
#          AGE INT,
#          SEX CHAR(1),
#          INCOME FLOAT )"""
#
# cursor.execute(sql)
#
# # 关闭数据库连接
# db.close()


# 数据库插入
# import MySQLdb
#
#
# db = MySQLdb.connect('localhost', 'root', '123', 'TESTDB')
#
# cursor = db.cursor()
#
# sql = """insert into EMPLOYEE(FIRST_NAME,
#          LAST_NAME, AGE, SEX, INCOME)
#          VALUES ('Mar', 'Mark', 18, 'M', 2800)"""
#
# try:
#     cursor.execute(sql)
#     db.commit()
#     print('Done')
# except:
#     db.rollback()
#
# db.close()


# 数据库查询
# >>>>>>>>>> python2.7 <<<<<<<<<<
# import MySQLdb
#
#
# db = MySQLdb.connect('localhost', 'root', '123', 'TESTDB')
#
# cursor = db.cursor()
#
# sql = "SELECT * FROM EMPLOYEE WHERE INCOME > 1000"
#
# try:
#     cursor.execute(sql)
#
#     result = cursor.fetchall()
#     for row in result:
#         fname = row[0]
#         lname = row[1]
#         age = row[2]
#         sex = row[3]
#         income = row[4]
#
#         print(fname, lname, age, sex, income)
# except:
#     print('ERROR!')
#
# db.close()



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


# phone_book = {
#     'Alex':{
#         'phone':'123',
#         'adrr':'ningbo'
#     },
#
#     'MAR':{
#         'phone':'15757870527',
#         'addr':'anhui'
#     },
#
#     'MT':{
#         'phone':'15726816113',
#         'addr':'hangzhou'
#     }
#
# }
# name = input('Input your name:\n')
# print(phone_book[name]['phone'])
# print(phone_book[name]['addr'])

# update
# MT = {
#    'phone':'15726816113',
#    'addr':'hangzhou',
#     'nickname':'mtt'
# }
# print('old dict:', MT)
#
# ph = {'phone':'15555555'}
# MT.update(ph)
# print('new dict:', MT)


# popitem 移除(弹出)字典中随机一项

# MT = {
#     'phone':'15726816113',
#     'addr':'hangzhou',
#     'nickname':'mtt',
#     'school':'NIT'
# }
# print('old dict:', MT)
# num = len(MT)
# print(num)
# i = 0
# 逐项移除
# while i < num:
#     print(i, MT)
#     MT.popitem()
#     i += 1

# print('new dict:', MT)
# print('移除的项1:', MT.popitem())
# print('new dict1', MT)
# print('移除的项2:', MT.popitem())
# print('new dict2', MT)
# print('移除的项3:', MT.popitem())
# print('new dict3', MT)


# >>>>>>>>>> chapter 5 <<<<<<<<<<

# for i in range(10):
#     print(i)
#     i += 1

# name = ''
# while not name or name.isspace():
#     name = input('Input your name :')
# print('Hello %s' % name)

# 并行迭代
# name = ['JJ', 'KK', 'MM', 'TT']
# age = [12, 15, 16, 22]

# for i in range(len(name)):
#     print(name[i] + "'s age is " + str(age[i]) )
# zz = zip(name, age)
# print(zz)

# zip解包元组
# name = ['JJ', 'KK', 'MM', 'TT']
# age = [12, 15, 16, 22]
#
# for name, age in zip(name, age):
#     print(name + "'s age is " + str(age))

while True:
    name = input('Input your name:')
    if not name:
        break
    print('Your name is ', name)




