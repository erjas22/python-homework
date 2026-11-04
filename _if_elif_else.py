# # task 1
# y = int(input())

# if (y % 4 == 0 and y % 100 > 0) or (y % 400 == 0):
#     print("Yes")
# else:
#     print("No")
# #task 2,2
# a, b, c = map(int, input().split())

# if a + b <= c or a + c <= b or b + c <= a:
#     print("Not traingle")
# elif a == b == c:
#     print("Equilateral")
# elif a == b or a == c or b == c:
#     print("Isosceles")
# else:
#     print("Scalene")

# # task2,3 
# age, day = map(str, input("age , ner oruul : ").split())
# age = int(age)


# if age < 12 or age > 60:
#     print(5000)
# elif day == "weekend":
#     print(12000)
# else:
#     print(10000)

# # task2,4

# name , password , status = map(str, input("name , pass , status oruul : ").split())
# password = int(password)
# if name == "admin" and password == 1234:
#     if status == "blocked":
#         print("Account blocked")
#     else:
#         print("Welcome")
# else:
#     print("Login failed")

# # task2,5

# x1, y1, x2, y2 = map(int, input("x1 , y1 , x2 , y2 og ; ").split())
# x, y = map(int, input("x , y og : ").split())

# if x1 <= x <= x2 and y1 <= y <= y2:
#     print("INSIDE")
# else:
#     print("OUTSIDE")

# # task2,6

# a1, b1 = map(int, input("a1, b1 oruul : ").split())
# a2, b2 = map(int, input("a2, b2 oruul : ").split())
# if a1 <= a2 <= b1 or a1 <= b2 <= a2 or a2 <= a1 <= b2 or a2 <= b1 <= b2:
#     print("yes")
# else:
#     print("no")
    
# # task 2,7

# day, month, year = map(int, input("day month year: ").split())

# if month < 1 or month > 12 or day <= 0:
#     print("Invalid")

# elif month == (1,3,5,7,8,10,12):
#     if day <= 31:
#         print("Valid")
#     else:
#         print("Invalid")

# elif month == (4,6,9,11):
#     if day <= 30:
#         print("Valid")
#     else:
#         print("Invalid")

# elif month == 2:
#     if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#         if day <= 29:
#             print("Valid")
#         else:
#             print("Invalid")
#     else:
#         if day <= 28:
#             print("Valid")
#         else:
#             print("Invalid")


# # task8
# a, b = map(int, input("a, b og : ").split())
# if a >= 9 or  b >= 9:
#     print("Invalid")
# elif (a + b) % 2 == 0 :
#     print("Black")
# else:
#     print("white")

# # task 9
# d, i, s = map(int, input("d,i,s og : ").split())
# if d > 90 and i > 95 and s == 0:
#     print("FUll")
# elif d > 80 and i > 90 and s <= 1:
#     print("Half")
# else:
#     print("None")

# #task 10
# player1 = input("player 1 r,p,s og : ")
# player2 = input("player 2 r,p,s og : ")
# if player1 == ("r") and player2 == ("s"):
#     print("Player 1")
# elif player1 == ("r") and player2 == ("p"):
#     print("Player 2")
# elif player1 == ("s") and player2 == ("r"):
#     print("Player 2")
# elif player1 == ("s") and player2 == ("p"):
#     print("Player 1")
# elif player1 == ("p") and player2 == ("s"):
#     print("Player 2")
# elif player1 == ("p") and player2 == ("r"):
#     print("Player 1")
# elif player1 == ("s") and player2 == ("s"):
#     print("Draw")
# elif player1 == ("r") and player2 == ("r"):
#     print("Draw")
# elif player1 == ("p") and player2 == ("p"):
#     print("Draw")   


#task 11
# a, b ,c = map(int, input("3 buhel too : ").split())
# if a < b < c :
#     print(a, b, c)
# elif b < a < c :
#     print(b, a , c)
# elif b < c < a:
#     print(b , c , a)
# elif a < c < b:
#     print(a, c, b)
# elif c < a < b:
#     print(c, a ,b)
# else:
#     print(c, b, a)


#task  12
# a, b = map(int, input("Эхлэх цаг — цаг минут: ").split())
# c, d = map(int, input("Дуусах цаг — цаг минут: ").split())

# e = a * 60 + b
# f = c * 60 + d

# if e < f:
#     print((f - e) // 60, "цаг", (f - e) % 60, "минут")
# elif e == f:
#     print("0 цаг 0 минут")
# else:
#     print((e - f) // 60, "цаг", (e - f) % 60, "минут")

#task13

# a, b, c = map(int, input(3 too oruul : ).split())
# if a + b <= c or a + c <= b or b + c <= a:
#     print("NOT A TRIANGLE")
# else:
#     if a >= b and a >= c:
#         d = a
#         a = c
#         c = d
#     elif b >= a and b >= c:
#         d = b
#         b = c
#         c = d
#     if a * a + b * b == c * c:
#         print("Right")

#     elif a * a + b * b > c * c:
#         print("Acute")

#     else:
#         print("Obtuse")

#task 14

# a, b ,c = map(int, input("3 buhel too oruul : ").split())
# d = b * b - 4 * a * c
# if a == 0 and b == 0 and c == 0:
#     print("Inf")
# elif a == 0 and b == 0 and c != 0:
#     print("No Roots")
# elif a == 0 and b != 0:
#     print("One Roots")
# elif a != 0 and d > 0:
#     print("two roots")
# elif a != 0 and d == 0:
#     print("One root")
# elif a != 0 and d < 0:
#     print("No roots")




#task 15

# day, month, year = map(int, input("day month year oruul : ").split())

# if month == 2:
#     if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
#         mday = 29
#     else:
#         mday = 28
# elif month (4, 6 , 9, 11):
#     mday = 30
# else:
#     mday = 31
# if day < mday:
#     day += 1
# else:
#     day = 1
#     month += 1

#     if month > 12:
#         month = 1
#         year += 1

# print(day, month, year)


 #task 16

# x1, y1, x2 , y2 = map(int, input("x1 y1 x2 y2 oruul : ").split())
# x3, y3, x4, y4 = map(int, input("x3 y3 x4 y4 oruul : ").split())
# if x2 < x3:
#     print("No")
# elif x4 < x1 :
#     print("No")
# elif y2 < y3:
#     print("No")
# elif y4 <y1:
#     print("No")
# else:
#     print("Yes")
          
#task 17

# t, m = map(int, input("UB tsag min oruul : ").split())
# z = int(input("tsagiin zoruu : "))
# c = t + z
# if 0 <= c <= 24:
#     print(c)
# elif 0 >= c:
#     print(c + 24, m)
# else:
#     print(c - 24, m)
# if c > 24:
#     print("tomorrow")
# elif c < 24:
#     print("Yesterday")
# else:
#     print("today")

#task 18
# a, b = map(int, input().split())

# if a < 0 or a > 50 or b < 0 or b > 50:
#     print("Invalid")

# elif a >= 25 and b >= 25:
#     if abs(a - b) == 2:
#         if a > b:
#             print("Player 1")
#         else:
#             print("Player 2")
#     else:
#         print("Not finished")

# elif a >= 25:
#     if a - b == 2:
#         print("Player 1")
#     else:
#         print("Invalid")

# elif b >= 25:
#     if b - a == 2:
#         print("Player 2")
#     else:
#         print("Invalid")

# else:
#     print("Not finished")


#task 19

# a = input()
# r1, c1, r2, c2 = map(int, input().split())
# if r1 < 1 or r1 > 8 or c1 < 1 or c1 > 8 or r2 < 1 or r2 > 8 or c2 < 1 or c2 > 8:
#     print("INVALID")
# elif r1 == r2 and c1 == c2:
#     print("NO")
# else:
#     dr = r2 - r1
#     if dr < 0:
#         dr = 0 - dr

#     dc = c2 - c1
#     if dc < 0:
#         dc = 0 - dc
#     if a == "king":
#         if dr <= 1 and dc <= 1:
#             print("YES")
#         else:
#             print("NO")

#     elif a == "rook":
#         if dr == 0 or dc == 0:
#             print("YES")
#         else:
#             print("NO")

#     elif a == "bishop":
#         if dr == dc:
#             print("YES")
#         else:
#             print("NO")

#     elif a == "queen":
#         if dr == 0 or dc == 0 or dr == dc:
#             print("YES")
#         else:
#             print("NO")

#     elif a == "knight":
#         if (dr == 2 and dc == 1) or (dr == 1 and dc == 2):
#             print("YES")
#         else:
#             print("NO")


#task 20
# a1, a2, a3 = input().split()
# b1, b2, b3 = input().split()
# c1, c2, c3 = input().split()

# if a1 == a2 == a3 == "X" or b1 == b2 == b3 == "X" or c1 == c2 == c3 == "X" or a1 == b1 == c1 =="X" or a2 == b2 == c2 == "X" or a3 == b3 == c3 == "X" or a1 == b2 == c3 == "X" or a3 == b2 == c1 == "X":
#     print("X wins")
# elif a1 == a2 == a3 == "O" or b1 == b2 == b3 == "O" or c1 == c2 == c3 == "O" or a1 == b1 == c1 =="O" or a2 == b2 == c2 == "O" or a3 == b3 == c3 == "O" or a1 == b2 == c3 == "O" or a3 == b2 == c1 == "O":
#     print("O wins")
# elif a1 == "." or a2 == "." or a3 == "." or b1 == "." or b2 == "." or b3 == "." or c1 == "." or c2 == "." or c3 == ".":
#     print("Not finished")
# else:
#     print("Draw")

