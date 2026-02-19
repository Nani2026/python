# a=4
# A='ambika'
# print(A)


'''
x=int("5"),
y=float("3.14"),
z=str(200)

print(type(x))
print(type(y))
print(type(z))
'''
#----------------------dictionery--------------
# a={
#     "name":"ambika",
#     "age":20,
#     "address":"dhading"
#     }
# print(a)
# print(type(a))
# print(len(a))


# #-------------List-----------------------
# a=[1,2,3,4,5,'ambik',6,7.5,8,None]
# print(a[-1])
# print(a[7])

# # Length check chai 1 index batw start hunxa..---------->
# #----------Slicing------------
# print(a[0:4])
# print(a[:4])
# print(a[4:])
# print(a[:])

# #------------>List ma data add garne tarika------------->
# data=[1,2,3,4,5,"ambika"]
# data.append(2)
# data.insert(2,'dangol')
# print(data)


# # --------------> Extend-------->
# a=[1,2,3,4,5,5]
# b=[10,20,30]
# a.extend(b)
# b.extend(a)
# print(a)
# print(b)

#-------------------> Concat------------->
# a=[1,3,4]
# b=[2,3,4]
# c=(a+b)
# print(c)
# print(a,b)

# #--------------> del/remove/pop/clear------------>
# a=[20,1,3,4,5,3]
# b=[3,40,5,6,]
# del a[0]
# del a[-1]
# print(a)

# a=[20,1,3,4,5,3]
# a.remove(20)
# a.pop()
# a.clear()
# print(a)

# a=int(input("Enter the first number: "))
# b=float(input("Enter the second number: "))
# module=a%b
# print(module)

#--------------->Loop----------------->
# i= 100
# while i>=200:
#     print(i)
#     i += 1
    
    
# def add(*args):
#     total = 0
#     for n in args:
#         total += n
#     return total

# print(add(1, 2))
    

#Write a function that takes one number and returns its square.
# def square(num):
#     return num * num

# n = int(input("Enter one number: "))
# print(square(n))

#Write a function that takes two numbers and returns their sum.
# def add(a,b):
#     return a+b
# a= int(input("Enter the first number: "))
# b= int(input("Enter the second number: "))
# print(add(a,b))

# Write a function that prints “Hello World”.

# Write a function that takes one number and returns its square.

# Write a function that takes two numbers and returns their sum.

# Write a function that checks if a number is even or odd.

# Write a function that takes a name and prints
# Write a function that takes a list and returns the largest number.

# Write a function that counts how many vowels are in a string.

# Write a function that uses *args to find the sum of any number of values.

# Write a function that takes a number and returns factorial.

# Write a function that checks if a string is a palindrome.
# Write a function that accepts any number of arguments and returns their average.

# Write a function that accepts **kwargs and prints
# key : value format.

# Write a function that takes *args and returns maximum value.

# Write a function that accepts student details using **kwargs and prints them nicely.
# Write a function that returns second largest number from a list.

# Write a function that removes duplicate values from a list.

# Write a recursive function to find Fibonacci series.

# Write a function that checks whether a number is prime.

# Write a function that takes a sentence and returns word count.

# Write a function that uses another function inside it (nested function).


# ----------------------->Write a function that checks if a number is even or odd.-------->
# def check(a):
#     if a % 2 == 0:
#         print("even")
#     else:
#         print("odd")
# num= int(input("the number is: "))
# print(check(num))

#--------------------++----------------------------->
# Write a function that takes a name and prints
# def name():
#     return name
# a=str(input("My name is : "))
# print(name(a))

#Write a function that prints “Hello World”.
# def greet():
#     print("Hello world!!!")
# greet()

#Write a function that takes a list and returns the largest number.
# def check(large_num):
#     return max(large_num)
# list1 = [1,2,3,4,5,6,7,8,9,10]
# print(check(list1))

# a=int(input("Enter your age : "))
# if a > 20:
#      print("You are eligible for vote.")
# else:
#     print("you are not eligible for vote")

# list = [1,3,30,40,50,60,100]
# list.append(70)
# print(list)
# list = [1,3,30,40,50,60,100]
# list.insert(12,7)
# print(list)
# list = [1,3,30,40,50,60,100]
# list.remove(40)
# print(list)
# list = [1,3,30,40,50,60,100]
# list.pop(3)
# # print(list)
# list1 = [1,3,2,6,8,7,30,40,1010,60,100]
# total=sum(list1)
# print(total)



#------------------------>>>>>>>>>>>>>>>>>>------------------------
# def a1(name,age):
#     print(name,age)
# name=input("Enter your name: ")
# age=int(input("Enter your age: "))
# a1(name, age)


# def al(sathi):
#     print(sathi)

# al('manju')



#Write a function that takes a string and returns its length.
def check_length(name):
    return len(name)
nam=input("Enter your name: ")
print(check_length(nam))