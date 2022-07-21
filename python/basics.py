#  My first python statement 
# single line comment
''' 
multi 
line 
comment
'''

# # print(type(5))
# # print(type(5.0))
# # print(5==5.0)
# # word = "hello world"
# # print(len(word))
# # print(word[:])
# number1 = float(input("enter number 1: "))
# number2 = float(input("enter number 2: "))

# if number1 == 0:
#     print("you entered 0")

# # print(type(number1))

# print(number1 + number2)

# print(10/3)
# print(10//3)
# print(10%3)

# print((31**331)%20)
# print(1==1)

# print((99/3) % 2 != 0)
# word = "hello"
# if "h" in word:
#     print("yes")
# elif "x" not in word:
#     print("something else")
# else:
#     print("another thing")
#
#price=int(input("enter the price: "))
#if price>=300:
# discount= price*0.3
#elif price>=200 and price<300:
# discount =price*0.2
#elif price>=100 and price<200:
#   discount =price*0.1
#elif price<100 and price>=0:
#  discount =price*0.05
#else:
#  discount=0
#print("Your discount is: ",discount)
#
#

word = "Hello Python"

# for l in word:
#     print(l)

# for i in range(1, 11, 2):
#     print(i)


names = ['James', 'Jane', 'Patrick', 'Pamela']
other_names = ['Xavier', 'Magneto']
# for name in names:
#     print(name)

# print(names[0])
# print(names[0:2])
# print(names + other_names)

# list methods
names.append("Storm")
names.insert(0, "Richard")
names.pop(5)
# other_names.clear()
# print(names.reverse())



# Dictionary

names = dict()
persons = {'names': ['peter', 20], 'test': {'test1': 20, 'test2': 22}}

# print(persons['test']['test2'])


name =  "James"

print("Hello " + name)
print(f"Hello {name}")





