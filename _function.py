# #task 1
# def hello():
#     print("Hello Python!")

# hello()

# #task 2
# def greet(name):
#     print(f"Sain baina uu, {name}!")

# name = input("neree oruul: ")
# greet(name)

# #task 3
# def introduce(name, age):
#     print(f"{name} ni {age} nastai.")

# introduce("Bat", 18)

# #task 4
# def add(a, b):
#     print(a + b)

# a, b = map(int, input("2 too oruul: ").split())
# add(a, b)

# #task 5
# def square(num):
#     return num ** 2

# result = square(5)
# print(result)

# #task 6
# def max_num(a, b):
#     if a > b:
#         return a
#     return b

# a, b = map(int, input("2 too oruul: ").split())
# print(max_num(a, b))

# #task 7
# def check_even(num):
#     if num % 2 == 0:
#         return "Even"
#     return "Odd"

# num = int(input("too oruul: "))
# print(check_even(num))

# #task 8
# def check_age(age):
#     if age >= 18:
#         return "Adult"
#     return "Minor"

# age = int(input("nasaa oruul: "))
# print(check_age(age))

# #task 9
# def get_grade(score):
#     if score >= 90:
#         return "A"
#     elif score >= 80:
#         return "B"
#     elif score >= 70:
#         return "C"
#     elif score >= 60:
#         return "D"
#     else:
#         return "F"

# score = int(input("onoogoo oruul: "))
# print(get_grade(score))

# #task 10
# def print_numbers(n):
#     for i in range(1, n + 1):
#         print(i, end=" ")
#     print()

# n = int(input("n oruul: "))
# print_numbers(n)

# #task 11
# def sum_numbers(n):
#     total = 0
#     for i in range(1, n + 1):
#         total += i
#     return total

# n = int(input("n oruul: "))
# print(sum_numbers(n))

# #task 12
# def count_even(n):
#     count = 0
#     for i in range(1, n + 1):
#         if i % 2 == 0:
#             count += 1
#     return count

# n = int(input("n oruul: "))
# print(count_even(n))

# #task 13
# def count_digits(num):
#     if num == 0:
#         return 1
#     count = 0
#     while num > 0:
#         num //= 10
#         count += 1
#     return count

# num = int(input("too oruul: "))
# print(count_digits(num))

# #task 14
# def find_max(nums):
#     biggest = nums[0]
#     for num in nums:
#         if num > biggest:
#             biggest = num
#     return biggest

# nums = [4, 8, 2, 15, 6]
# print(find_max(nums))

# #task 15
# def find_min(nums):
#     smallest = nums[0]
#     for num in nums:
#         if num < smallest:
#             smallest = num
#     return smallest

# nums = [7, 3, 9, 1, 5]
# print(find_min(nums))

# #task 16
# def count_even(nums):
#     count = 0
#     for num in nums:
#         if num % 2 == 0:
#             count += 1
#     return count

# nums = [1, 2, 4, 7, 8, 10]
# print(count_even(nums))

# #task 17
# def list_sum(nums):
#     total = 0
#     for num in nums:
#         total += num
#     return total

# nums = [10, 20, 30, 40]
# print(list_sum(nums))

# #task 18
# def get_age(students, name):
#     return students[name]

# students = {
#     "Bat": 18,
#     "Sara": 19,
#     "Bold": 20
# }
# print(get_age(students, "Sara"))

# #task 19
# def find_student(students, name):
#     if name in students:
#         return "Found"
#     return "Not found"

# students = {
#     "Bat": 18,
#     "Sara": 19,
#     "Bold": 20
# }
# name = input("neree oruul: ")
# print(find_student(students, name))

# #task 20
# def average_score(students):
#     total = 0
#     for score in students.values():
#         total += score
#     return total / len(students)

# students = {
#     "Bat": 80,
#     "Sara": 90,
#     "Bold": 70
# }
# print(average_score(students))

# #task 21
# def unique_count(nums):
#     return len(set(nums))

# nums = [1, 2, 2, 3, 3, 3, 4]
# print(unique_count(nums))

# #task 22
# def unique_numbers(nums):
#     return set(nums)

# nums = [1, 2, 2, 3, 3, 4]
# print(unique_numbers(nums))

# #task 23
# def greet(name="Guest"):
#     print(f"Hello {name}")

# greet()
# greet("Bat")

# #task 24
# def power(num, exponent=2):
#     return num ** exponent

# print(power(5))
# print(power(2, 3))

# #task 25
# def discount(price, percent=10):
#     return price * (100 - percent) // 100

# print(discount(10000))
# print(discount(10000, 20))

# #task 26
# def sum_all(*args):
#     total = 0
#     for num in args:
#         total += num
#     return total

# print(sum_all(1, 2, 3))
# print(sum_all(10, 20, 30, 40))

# #task 27
# def find_max(*args):
#     biggest = args[0]
#     for num in args:
#         if num > biggest:
#             biggest = num
#     return biggest

# print(find_max(5, 8, 2, 10, 3))

# #task 28
# def count_even(*args):
#     count = 0
#     for num in args:
#         if num % 2 == 0:
#             count += 1
#     return count

# print(count_even(1, 2, 4, 7, 8, 10))

# #task 29
# def show_info(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")

# show_info(name="Bat", age=18, city="Ulaanbaatar")

# #task 30
# def calculate_total(**prices):
#     total = 0
#     for price in prices.values():
#         total += price
#     return total

# print(calculate_total(
#     apple=2000,
#     banana=3000,
#     orange=2500
# ))

# #task 31
# def analyze_numbers(nums):
#     biggest = nums[0]
#     smallest = nums[0]
#     total = 0
#     even = 0
#     odd = 0
#     for num in nums:
#         if num > biggest:
#             biggest = num
#         if num < smallest:
#             smallest = num
#         total += num
#         if num % 2 == 0:
#             even += 1
#         else:
#             odd += 1
#     return {
#         "max": biggest,
#         "min": smallest,
#         "sum": total,
#         "even": even,
#         "odd": odd
#     }

# nums = [3, 8, 2, 7, 10]
# print(analyze_numbers(nums))

# #task 32
# def student_average(students, name):
#     scores = students[name]
#     return sum(scores) / len(scores)

# students = {
#     "Bat": [80, 90, 70],
#     "Sara": [100, 90, 95],
#     "Bold": [60, 70, 80]
# }
# print(student_average(students, "Bat"))

# #task 33
# def student_average(students, name):
#     scores = students[name]
#     return sum(scores) / len(scores)

# def best_student(students):
#     best_name = ""
#     best_avg = -1
#     for name in students:
#         avg = student_average(students, name)
#         if avg > best_avg:
#             best_avg = avg
#             best_name = name
#     return best_name

# students = {
#     "Bat": [80, 90, 70],
#     "Sara": [100, 90, 95],
#     "Bold": [60, 70, 80]
# }
# print(best_student(students))

# #task 34
# def calculate(*args, **kwargs):
#     base = 0
#     for num in args:
#         base += num
#     bonus = kwargs.get("bonus", 0)
#     tax = kwargs.get("tax", 0)
#     return base + bonus - tax

# print(calculate(10, 20, 30, bonus=100, tax=20))