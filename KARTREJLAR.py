# # # # # # # numbers = (1, 2, 3, 4)
# # # # # # # print(type(numbers))
# # # # # # a = tuple([1, 2, 3, 4])
# # # # # # print(type(a))
# # # # # numbers = (1, 2, 3, 4)
# # # # # numbers = list(numbers)
# # # # # numbers[1] = 9
# # # # # numbers = tuple(numbers)
# # # # # print(numbers)
# # # # numbers = (1, 2, 3, 4)
# # # # i=0
# # # # while i < len(numbers):
# # # #     print(numbers[i])
# # # #     i+=1
# # # #
# # # # for i in numbers:
# # # #     print(i)
# # # #
# # # # for i in range(len(numbers)):
# # # #     print(numbers[i])
# # # numbers1 = (1, 2, 3)
# # # numbers2 = (4, 5, 6)
# # # numbersAll = numbers1 + numbers2
# # # print(numbersAll)
# # numbers = (1, 2, 3, 4)
# # myNumbers = numbers * 2
# # print(myNumbers)
# """ kortej metodlari   """
# numbers = (1, 2, 3, 4, 5, 2, 3, 1, 4)
# #count()
# print(numbers.count(2))
# #index()
# print(numbers.index(2))
# #masala:
# x  = (1)
# y=(1,)
# print(type(x))
# print(type(y))
# # yo'qlik qiymatlari
# a = None
# b = ''
# c = []
# d = ()
# e = 0
# h = False
# print(f"{bool(a)} {bool(b)} {bool(c)} {bool(e)} {bool(h)}")