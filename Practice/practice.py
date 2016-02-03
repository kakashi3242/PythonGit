# 1.有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？

# for a in range(1, 5):
#     for b in range(1, 5):
#         for c in range(1, 5):
#             if a != b and b != c and a != c:
#                 number = a*100 + b*10 + c
#                 print(number)


# 2.输入三个整数x,y,z，请把这三个数由小到大输出。

# l = []
#
# for i in range(3):
#     x = int(input('Input the number:\n'))
#     l.append(x)
# l.sort() # 把list从小到大排序,当reverse = True时是逆向排序
# print(l)


# 3.将一个列表的数据复制到另一个列表中。

# a = [1, 2, 3, 4, 5]
# b = a[ : ]
# print(b)


# 4.输出9*9乘法口诀表。

# for i in range(1, 10):
#     for j in range(1, 10):
#         result = i * j
#         print('%d * %d = %d' %(i, j, result) )
#     print(' ')


# 5.利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。

# score = int(input('Input the score:\n'))
#
# if score in range(0, 101):
#     if 90 <= score <= 100:
#         print('His record is A')
#     elif 60 <= score < 89:
#         print('His record is B')
#     elif 0 <= score < 60:
#         print('His record is C')
# else:
#     print('Input correctly score!')


# 6.求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加有键盘控制。

# times = input('Input the times:\n')
# from legacy import reduce
#
# Tn = 0
# Sn = []
# n = int(input('n = \n'))
# a = int(input('a = \n'))
# for count in range(n):
#     Tn += a
#     a *= 10
#     Sn.append(Tn)
#     print(Tn)
#
# Sn = reduce(lambda x,y : x + y,Sn)
# print(Sn)


# 7.一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？

# meters = 50
# total_meters = 100
# for times in range(2,11):
#     total_meters += meters
#     meters /= 2
#
# print('第十次反弹 %f 米' %meters)
# print('共经过 %d 米' %total_meters)


# 8.题目：请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。

# letter = input("please input:")
#while letter  != 'Y':
# if letter == 'S':
#     print ('please input second letter:')
#     letter = input("please input:")
#     if letter == 'a':
#         print ('Saturday')
#     elif letter  == 'u':
#         print ('Sunday')
#     else:
#         print ('data error')
#
# elif letter == 'F':
#     print ('Friday')
#
# elif letter == 'M':
#     print ('Monday')
#
# elif letter == 'T':
#     print ('please input second letter')
#     letter = input("please input:")
#
#     if letter  == 'u':
#         print ('Tuesday')
#     elif letter  == 'h':
#         print ('Thursday')
#     else:
#         print ('data error')
#
# elif letter == 'W':
#     print ('Wednesday')
# else:
#     print ('data error')







