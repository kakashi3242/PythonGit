# 类与CocaCola

# <-------------1.------------->

# class CocaCola:
#     formula = ['caffeine','sugar','water','soda']
#     def __init__(self):
#         for element in self.formula:
#             print('Coke has {}!'.format(element))
#     def drink(self):
#         print('Energy!')
# coke = CocaCola()
# coke.drink()


# <-------------2.------------->

# class TestA:
#     attr = 1
#
# obj_a = TestA()
#
# TestA.attr = 33
#
# print(obj_a.attr)


# <-------------3.------------->

# class TestA:
#     attr = 1
# obj_a = TestA()
# obj_b = TestA()
#
# obj_a.attr = 23
# print(obj_b.attr)


# <-------------3.------------->

class TestA:
    attr = 1
    def __init__(self):
        self.attr = 42
obj_a = TestA()
print(obj_a.attr)





