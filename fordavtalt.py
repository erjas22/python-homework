# # for i in range(5):
# #     print("Сайн уу")

# #task2

# # for i in range(10):
# #     print(i)

# #task3

# for i in range(1, 11):
#     print(i)

# #task4

# for i in range(10, 0, -1):
#     print(i)

# #task5

# ner = input()
# for i in range(5):
#     print(ner)

# #task6

# total = 0
# for i in range(1, 11):
#     total += i
# print(total)

# #task7

# total = 0
# for i in range(1, 101):
#     total += i
# print(total)

# #task8

# total = 0
# for i in range(1, 21):
#     if i % 2 == 0:
#         total += i
# print(total)

# #task9

# total = 0
# for i in range(1, 31):
#     if i % 3 == 0:
#         total += i
# print(total)

# #task10

# n = int(input())
# total = 0
# for i in range(1, n + 1):
#     total += i
# print(total)

# #task11

# count = 0
# for i in range(1, 21):
#     if i % 2 == 0:
#         count += 1
# print(count)

# #task12

# count = 0
# for i in range(1, 101):
#     if i % 5 == 0:
#         count += 1
# print(count)

# #task13

# count = 0
# for i in range(1, 51):
#     if i % 3 == 0:
#         count += 1
# print(count)

# #task14

# even = 0
# odd = 0

# for i in range(1, 21):
#     if i % 2 == 0:
#         even += 1
#     else:
#         odd += 1

# print("Тэгш:", even)
# print("Сондгой:", odd)

# #task15   for + if + total/count

# n = int(input())
# count = 0

# for i in range(1, n + 1):
#     if i % 7 == 0:
#         count += 1

# print(count)

#task16

# total = 0
# count = 0

# for i in range(1, 101):
#     if i % 2 == 0:
#         total += i
#         count += 1

# print("Нийлбэр:", total)
# print("Тоо:", count)

# #task17

# count = 0

# for i in range(1, 101):
#     if i % 3 == 0 or i % 5 == 0:
#         count += 1

# print(count)

# #task18

# total = 0

# for i in range(1, 101):
#     if i % 3 == 0:
#         total += i

# print(total)

# #task19

# n = int(input())
# total = 0
# count80 = 0

# for i in range(n):
#     dun = int(input())
#     total += dun

#     if dun > 80:
#         count80 += 1

# print("Нийлбэр:", total)
# print("Дундаж:", total / n)
# print("80-аас дээш:", count80)


# #task20      best

# n = int(input())
# best = 0

# for i in range(n):
#     dun = int(input())
#     if dun > best:
#         best = dun

# print("Хамгийн өндөр:", best)

# #task21

# n = int(input())
# smallest = int(input())

# for i in range(n - 1):
#     num = int(input())
#     if num < smallest:
#         smallest = num

# print("Хамгийн бага:", smallest)

# #task22   Challenge

# n = abs(int(input()))
# total = 0

# for digit in str(n):
#     total += int(digit)

# print(total)

# #task23

# n = int(input())
# result = 1

# for i in range(1, n + 1):
#     result *= i

# print(result)

# #task24

# n = int(input())
# total = 0

# for i in range(1, n):
#     if n % i == 0:
#         total += i

# if total == n:
#     print("YES")
# else:
#     print("NO")

# #task25

# n = int(input())
# prime = True

# if n < 2:
#     prime = False

# for i in range(2, n):
#     if n % i == 0:
#         prime = False

# if prime:
#     print("YES")
# else:
#     print("NO")

# #task26

# a = b = c = 0

# for i in range(1, 101):
#     if i % 2 == 0:
#         a += 1
#     if i % 3 == 0:
#         b += 1
#     if i % 5 == 0:
#         c += 1

# print("2-т:", a)
# print("3-т:", b)
# print("5-д:", c)

# #task27

# for i in range(1, 31):
#     if i % 2 == 0:
#         print(i, "2-т хуваагдана")
#     else:
#         print(i, "2-т хуваагдахгүй")

# #task28

# count = 0
# total = 0

# for i in range(1, 101):
#     if i % 5 == 0:
#         count += 1
#         total += i

# print("Тоо:", count)
# print("Нийлбэр:", total)

# #task29

# n = int(input())
# total = 0

# for i in range(n):
#     num = int(input())
#     total += num

# print("Нийлбэр:", total)
# print("Тоо:", n)
# print("Дундаж:", total / n)

#task30

# n = int(input())
# even_count = 0
# odd_count = 0
# even_total = 0
# odd_total = 0

# for i in range(1, n + 1):
#     if i % 2 == 0:
#         even_count += 1
#         even_total += i
#     else:
#         odd_count += 1
#         odd_total += i

# print("Тэгш тоо:", even_count)
# print("Сондгой тоо:", odd_count)
# print("Тэгш нийлбэр:", even_total)
# print("Сондгой нийлбэр:", odd_total)
# print("Хамгийн их:", n)
# print("Хамгийн бага:", 1)

































































































