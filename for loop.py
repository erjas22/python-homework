# for i in range(5):
#     print("sainu")

#task 2
# for i in range(0, 10):
#     print(i)

#task 3
# for i in range(1, 11):
#     print(i)

#task 4
# for i in range(10, 0, -1):
#     print(i)
# print("hasah")

#task 5
# a = input("ner og : ")
# for i in range(5):
#     print(a)

#task 6
# total = 0
# for i in range(11):
#     total += i
# print(total)

#task 7
# total = 0 
# for i in range(1,101):
#     total += i
# print(total)

#task 8
# total = 0 
# for i in range(0,21,2):
#     total += i
# print(total)

#task 9
# total = 0 
# for i in range(0,31,3):
#     total += i
# print(total)

#task 10
# n = int(input("too og : "))
# for i in range(1,n):
#     n += i
# print(n)

#task 11
# a = 0
# for i in range(1, 21):
#     if i % 2 == 0:
#         a += 1
# print(a)

#task 12
# a = 0
# for i in range(1, 101):
#     if i % 5 == 0:
#         a += 1
# print(a)

#task 13
# a = 0
# for i in range(1, 51):
#     if i % 3 == 0:
#         a += 1
# print(a)

#task 14
# a = 0
# b = 0
# for i in range(1, 21):
#     if i % 2 == 0:
#         a += 1
#     else:
#         b += 1
# print("tegsh",a)
# print("sondgoi",b)

#task 15
# n = int(input("too og ; "))
# a = 0
# for i in range(1, n):
#     if i % 7 == 0 :
#         a += 1
# print(a)

#task 16
# a = 0
# b = 0
# for i in range(1, 101,2):
#     a += i
#     b += 1
# print("Niilber : ",a)
# print("Too : ",b)
    
#task 17
# a = 0
# for i in range(1, 101):
#     if i % 3 == 0 or i % 5 == 0:
#         a += 1
# print(a)

#task 18
# a = 0 
# for i in range(0, 101, 3):
#     a += i
# print(a)

#task 19
# a =int(input("heden suragchin dun oruulah : "))

# b = 0
# c = 0
# for i in range(a):
#     d = int(input("dun iruul : "))
#     b += d
#     if d > 80:
#         c += 1
# dundaj = b // a
# print("niilber : ", b)
# print("dundaj : ",dundaj)
# print("80-aas deesh : ",c)

#task 20
# a = int(input("heden dun oroh : "))
# best = 0
# for i in range(a):
#     d = int(input("dun oruul : "))
#     if d > best:
#         best = d
# print(best)

#task 21
# a = int(input("heden dun oroh : "))
# lowest = 10000000000000000000000000
# for i in range(a):
#     d = int(input("dun oruul : "))
#     if d < lowest:
#         lowest = d
# print(lowest)

#task 22
# n = int(input("too og : "))

# b= 0

# for i in range(10):
#     b = b + n % 10
#     n = n // 10

# print(b)

#task 23
# n = int(input("too og : "))
# for i in range(1,n):
#     n *= i
# print(n)

#task 24
# n = int(input("too og : "))
# a = 0
# for i in range(1, n):
#     if n % i == 0:
#         a += i
# if  a == n:        
#     print("Yes")
# else:
#     print("No")


#task 2,21
# for i in range(10, 51):
#     if i % 3 == 0:
#         print(i)

#task 2,22
# n = int(input())

# for i in range(2, n + 1, 2):
#     print(i)

#task 2,23
# a = 0 
# for i in range(1, 50,2):
#     a += i
# print(a)


#task 2,24
# a = 0
# for i in range(1,101,4):
#     a += 1
# print(a)

#task 2,25
# total = 0
# a = int(input("niit toog oruul: "))
# for i in range(a):
#     b = int(input("nemeg toog oruul: "))
#     if b > 0 :
#         total += b
#         print("uyereg tooni niilber : ", total)

#task 2,26
# a = 0 
# for i in range(10, 101):
#     if i % 5 == 0:
#         a += i
# print(a)

#tsak 2,27
# n = int(input("too og : "))
# b= 0
# for i in range(10):
#     b = b + n % 10
#     n = n // 10
# print(b)



#task 2.28
# count = 0
# for i in range(1, 101):
#     if i % 7 == 0 and count < 5:
#         print(i)
#         count += 1

#task 2,29
# a = 0
# for i in range(0, 50):
#     if i % 2 == 0:
#         a = i
# print(a)

# #task 2,30
# a = int(input("niitoruulah too: "))
# c = 0
# for i in range(a):
#     b = int(input("too og: "))
#     if b > 0:
#         if c == 0 or b < c:
#             c = b 
# print(c) 