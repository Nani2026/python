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
i= 100
while i>=200:
    print(i)
    i += 1