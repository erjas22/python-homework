#task 1
# for i in range(1,11):
#     print(i)

#task 2 
# for i in range (0,21,2):
#     print(i)

#task 3
# for i in range(1,20,2):
#     print(i)

#task 4
# for i in range(1, 11):
#     print(5, "*", i ,  "=",5*i)

#task5
# n = int(input("too og: "))
# for i in range(1, n):
#     print(i)

#task 6
# n = int(input("too og: "))
# for i in range(n,0, -1):
#     print(i)

#task 7
# for i in range(0,51):
#     if i % 3 == 0:
#         print(i)

#task 8
# for i in range(0,30):
#     if i % 5 != 0:
#         print(i)

#task 9
# a = 0
# for i in range(0,100):
#     if i % 2 == 0:
#         a += 1
# print(a)

#task 10 
# a = 0
# for i in range(1,100):
#     if i % 7 == 0:
#         a += 1
# print(a)

#task 11
# a = 0
# for i in range(1,101):
#     a += i
# print(a)

#task 12
# a = 0 
# for i in range(1,51):
#     if i % 2 == 0:
#         a+=i
# print(a)

#task 13
# a = 0
# while a < 10 :
#     a += 1
#     print(a)

#task 14
# i = 10
# while i >= 1:
#     print(i)
#     i -= 1

#task 15
# i = 2
# while i <= 20:
#     print(i)
#     i += 2

#task 16
# n = int(input("too og: "))
# a = 0
# total = 0
# while a < n:
#     total = total + a
#     a += 1
#     print(total)

#task 17
# n = int(input("too og: "))
# tsifr = 0
# while 0 < n:
#     n = n // 10
#     tsifr += 1
# print(tsifr)

#task 18
# n = int(input("too og: "))
# niilber = 0
# while n > 0:
#     tsifr = n % 10
#     niilber += tsifr
#     n = n // 10
# print(niilber)

#task 19
# i = 1
# while i <= 20:
#     if i == 5:
#         break
#     print(i)
#     i += 1

#task 20
# i = 10
# while i <= 100:
#     if i % 7 == 0:
#         break
#     print(i)
#     i += 1

#task 21
# i = int(input("eyreg too og: "))
# secret  = 8
# while 0 < i:
#     if i == 8:
#         print("zow bna ")
#         break
#     else:
#         i = int(input("buruu too bna ahiad oroldon uu: "))

    
#task 22
# i = int(input("eyreg too og: "))
# secret  = 0
# while 0 <= i:
#     if i == secret:
#         print("zow bna ")
#         break
#     else:
#         i = int(input("oor too og: "))

#task 23
# i = int(input("too oruulaa 0 avbal zogson: "))
# a = 0
# while 0 <= i:
#     a += i
#     if i == 0:
#         print(a)
#         break    
#     else:
#         i = int(input("too ogoodi: ")) 

#task 24
# a = 0
# while a < 10:
#     a += 1
#     if a == 5:
#         continue
#     else:
#         print(a)

#task 25
# a = 0 
# while a < 20:
#     a += 1
#     if a % 2 == 0:
#         continue
#     else:
#         print(a)

#task 26
# a = 0 
# while a < 30:
#     a += 1
#     if a % 3 == 0:
#         continue
#     else:
#         print(a)

#task 27
# i = int(input("niit oruulah too: "))
# a = 0
# c = 0
# while a < i:
#     a+= 1
#     b = int(input("too oruul: "))
#     if b < 0:
#         continue
#     else:
#        c += b 
#        print(c)

#task 28
# i = int(input('too og: '))
# a = 0 
# while a < i:
#     a += 1
#     if a % 7 == 0:
#         print(a)
#     else:
#         continue

#task 29
# i = int(input("too og: "))
# a = 0 
# while True:
#     i = int(input("too og: "))
#     if i == 0:
#         break
#     elif i % 2 != 0:
#         continue
#     elif i > 0:
#         print(i)

#task 30 
# i = int(input("toog ol: "))
# secret = 17 
# while True:
#     if  i < 0:
#          continue
#     elif secret > i:
#         print("baga bna")
#         i = int(input("toog ol: "))
#     elif secret < i:
#         print("ih bna")
#         i = int(input("toog ol: "))
#     else:
#         print("nice")
#         break