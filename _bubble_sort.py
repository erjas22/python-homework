# #task 1
# numbers = list(map(int, input("toonuudaa oruul: ").split()))
# n = len(numbers)

# for i in range(n - 1):
#     for j in range(n - 1 - i):
#         if numbers[j] > numbers[j + 1]:
#             numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

# print(numbers)

# #task 2
# numbers = list(map(int, input("toonuudaa oruul: ").split()))
# n = len(numbers)

# for i in range(n - 1):
#     for j in range(n - 1 - i):
#         if numbers[j] < numbers[j + 1]:
#             numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

# print(numbers)

# #task 3
# numbers = list(map(int, input("toonuudaa oruul (sorog too orj bolno): ").split()))
# n = len(numbers)

# for i in range(n - 1):
#     for j in range(n - 1 - i):
#         if numbers[j] > numbers[j + 1]:
#             numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

# print(numbers)

# #task 4
# numbers = list(map(int, input("toonuudaa oruul (davhardsan too orj bolno): ").split()))
# n = len(numbers)

# for i in range(n - 1):
#     for j in range(n - 1 - i):
#         if numbers[j] > numbers[j + 1]:
#             numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

# print(numbers)

# #task 5
# numbers = list(map(int, input("toonuudaa oruul: ").split()))
# n = len(numbers)

# for i in range(n - 1):
#     for j in range(n - 1 - i):
#         if numbers[j] > numbers[j + 1]:
#             numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

# print(numbers)

# #task 6
# names = input("neruudee oruul: ").split()
# n = len(names)

# for i in range(n - 1):
#     for j in range(n - 1 - i):
#         if names[j] > names[j + 1]:
#             names[j], names[j + 1] = names[j + 1], names[j]

# print(names)

# #task 7
# scores = list(map(int, input("onoonuudaa oruul: ").split()))
# n = len(scores)

# for i in range(n - 1):
#     for j in range(n - 1 - i):
#         if scores[j] > scores[j + 1]:
#             scores[j], scores[j + 1] = scores[j + 1], scores[j]

# print(scores)

# #task 8
# numbers = list(map(int, input("toonuudaa oruul: ").split()))

# for j in range(len(numbers) - 1):
#     if numbers[j] > numbers[j + 1]:
#         numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

# print(numbers)

# #task 9
# numbers = list(map(int, input("toonuudaa oruul: ").split()))
# n = len(numbers)
# toirog = 0

# for i in range(n - 1):
#     toirog += 1
#     for j in range(n - 1 - i):
#         if numbers[j] > numbers[j + 1]:
#             numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

# print(toirog, "toirog ajillasan")
# print(numbers)

# #task 10
# numbers = list(map(int, input("toonuudaa oruul: ").split()))
# n = len(numbers)
# swap_count = 0

# for i in range(n - 1):
#     for j in range(n - 1 - i):
#         if numbers[j] > numbers[j + 1]:
#             numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
#             swap_count += 1

# print(numbers)
# print("niit solilts:", swap_count)

# #task 11
# numbers = list(map(int, input("toonuudaa oruul: ").split()))
# n = len(numbers)

# for i in range(n - 1):
#     for j in range(n - 1 - i):
#         if numbers[j] < numbers[j + 1]:
#             numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

# print(numbers[1])

# #task 12
# numbers = list(map(int, input("eyreg, sorog toonuudaa oruul: ").split()))
# n = len(numbers)

# for i in range(n - 1):
#     for j in range(n - 1 - i):
#         if numbers[j] > numbers[j + 1]:
#             numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

# print(numbers)

# #task 13
# numbers = list(map(int, input("toonuudaa oruul: ").split()))
# n = len(numbers)

# for i in range(n - 1):
#     for j in range(n - 1 - i):
#         if numbers[j] > numbers[j + 1]:
#             numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
#     print(f"{i + 1}-r toirog: {numbers}")

# #task 14
# numbers = list(map(int, input("toonuudaa oruul: ").split()))
# n = len(numbers)

# for i in range(n - 1):
#     swapped = False
#     for j in range(n - 1 - i):
#         if numbers[j] > numbers[j + 1]:
#             numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
#             swapped = True
#     if not swapped:
#         print("neg ch solilts hiigdeegui, erembelegdsen baina")
#         break

# print(numbers)

# #task 15
# numbers = list(map(int, input("toonuudaa oruul: ").split()))
# n = len(numbers)
# toirog = 0

# for i in range(n - 1):
#     toirog += 1
#     swapped = False
#     for j in range(n - 1 - i):
#         if numbers[j] > numbers[j + 1]:
#             numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
#             swapped = True
#     if not swapped:
#         break

# zov = True
# for i in range(n - 1):
#     if numbers[i] > numbers[i + 1]:
#         zov = False
#         break

# print(numbers)
# if zov:
#     print("zov erembelegdsen")
# else:
#     print("buruu erembelegdsen")
# print(toirog, "toirog ajillasan")

# #task 16
# n = int(input("heden oyutan: "))
# students = []
# for i in range(n):
#     name, score = input(f"  {i + 1}-r oyutan (ner onoo): ").split()
#     students.append([name, int(score)])

# for i in range(n - 1):
#     for j in range(n - 1 - i):
#         if students[j][1] > students[j + 1][1]:
#             students[j], students[j + 1] = students[j + 1], students[j]

# print(students)

# #task 17
# n = int(input("heden hun: "))
# people = []
# for i in range(n):
#     name, age = input(f"  {i + 1}-r hun (ner nas): ").split()
#     people.append([name, int(age)])

# for i in range(n - 1):
#     for j in range(n - 1 - i):
#         if people[j][1] > people[j + 1][1]:
#             people[j], people[j + 1] = people[j + 1], people[j]

# print(people)
# print("hamgiin zaluu:", people[0][0])
# print("hamgiin ahmad:", people[-1][0])

# #task 18
# numbers = list(map(int, input("toonuudaa oruul: ").split()))
# target = int(input("ali toog toolokh: "))
# n = len(numbers)

# for i in range(n - 1):
#     for j in range(n - 1 - i):
#         if numbers[j] > numbers[j + 1]:
#             numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

# count = 0
# for num in numbers:
#     if num == target:
#         count += 1

# print(numbers)
# print(target, "too", count, "udaa baina.")

# #task 19
# n = int(input("heden baraa: "))
# products = []
# for i in range(n):
#     name, price = input(f"  {i + 1}-r baraa (ner une): ").split()
#     products.append([name, int(price)])

# for i in range(n - 1):
#     for j in range(n - 1 - i):
#         if products[j][1] < products[j + 1][1]:
#             products[j], products[j + 1] = products[j + 1], products[j]

# print("hamgiin unetei 3 baraa:")
# for i in range(min(3, n)):
#     print(f"  {products[i][0]}: {products[i][1]}")

# #task 20
# numbers = list(map(int, input("toonuudaa oruul: ").split()))
# n = len(numbers)
# compare_count = 0
# swap_count = 0
# toirog = 0

# for i in range(n - 1):
#     toirog += 1
#     swapped = False
#     for j in range(n - 1 - i):
#         compare_count += 1
#         if numbers[j] > numbers[j + 1]:
#             numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
#             swap_count += 1
#             swapped = True
#     if not swapped:
#         break

# print("niit hartsuulalt:", compare_count)
# print("niit solilts:", swap_count)
# print("niit toirog:", toirog)
# print(numbers)

# #task 21
# numbers = list(map(int, input("toonuudaa oruul: ").split()))
# n = len(numbers)

# for i in range(n - 1):
#     for j in range(n - 1 - i):
#         if numbers[j] > numbers[j + 1]:
#             numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

# print(numbers)

# #task 22
# words = input("ugsee oruul: ").split()
# n = len(words)

# for i in range(n - 1):
#     for j in range(n - 1 - i):
#         if len(words[j]) > len(words[j + 1]):
#             words[j], words[j + 1] = words[j + 1], words[j]

# print(words)

# #task 23
# numbers = list(map(int, input("toonuudaa oruul: ").split()))

# for j in range(len(numbers) - 1, 0, -1):
#     if numbers[j] < numbers[j - 1]:
#         numbers[j], numbers[j - 1] = numbers[j - 1], numbers[j]

# print(numbers)

# #task 24
# numbers = list(map(int, input("toonuudaa oruul: ").split()))
# n = len(numbers)

# for i in range(n - 1):
#     for j in range(n - 1 - i):
#         if numbers[j] % 2 == 1 and numbers[j + 1] % 2 == 0:
#             numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

# print(numbers)

# #task 25
# a = list(map(int, input("1-r jagsaalt: ").split()))
# b = list(map(int, input("2-r jagsaalt: ").split()))
# numbers = a + b
# n = len(numbers)

# for i in range(n - 1):
#     for j in range(n - 1 - i):
#         if numbers[j] > numbers[j + 1]:
#             numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

# print(numbers)

# #task 26
# numbers = list(map(int, input("toonuudaa oruul: ").split()))
# n = len(numbers)
# swap_count = 0

# for i in range(n - 1):
#     toirog_swap = 0
#     for j in range(n - 1 - i):
#         if numbers[j] > numbers[j + 1]:
#             numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
#             toirog_swap += 1
#     swap_count += toirog_swap
#     print(f"{i + 1}-r toirog: {toirog_swap} solilts")

# print("niit solilts:", swap_count)

# #task 27
# numbers = list(map(int, input("toonuudaa oruul: ").split()))
# n = len(numbers)

# for i in range(n - 1):
#     for j in range(n - 1 - i):
#         if numbers[j] > numbers[j + 1]:
#             numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

# print(numbers[2])

# #task 28
# n = int(input("heden suragch: "))
# students = []
# for i in range(n):
#     name, score = input(f"  {i + 1}-r suragch (ner onoo): ").split()
#     students.append([name, int(score)])

# for i in range(n - 1):
#     for j in range(n - 1 - i):
#         if students[j][1] < students[j + 1][1]:
#             students[j], students[j + 1] = students[j + 1], students[j]

# print(students)

# #task 29
# numbers = list(map(int, input("toonuudaa oruul: ").split()))
# n = len(numbers)
# compare_count = 0
# swap_count = 0
# hooson_toirog = 0

# for i in range(n - 1):
#     swapped = False
#     for j in range(n - 1 - i):
#         compare_count += 1
#         if numbers[j] > numbers[j + 1]:
#             numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
#             swap_count += 1
#             swapped = True
#     if not swapped:
#         hooson_toirog = i + 1
#         break

# print("niit hartsuulalt:", compare_count)
# print("niit solilts:", swap_count)
# if hooson_toirog != 0:
#     print(f"solilts hiigdeegui ehnii toirog baina: {hooson_toirog}-r toirog")
# else:
#     print("solilts hiigdeegui toirog baihgui")
# print(numbers)

# #task 30
# n = int(input("heden baraa: "))
# products = []
# for i in range(n):
#     name, price, stock = input(f"  {i + 1}-r baraa (ner une uldegdel): ").split()
#     products.append([name, int(price), int(stock)])

# for i in range(n - 1):
#     for j in range(n - 1 - i):
#         if products[j][1] < products[j + 1][1]:
#             products[j], products[j + 1] = products[j + 1], products[j]
#         elif products[j][1] == products[j + 1][1] and products[j][2] > products[j + 1][2]:
#             products[j], products[j + 1] = products[j + 1], products[j]

# for product in products:
#     print(product)