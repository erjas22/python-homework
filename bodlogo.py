# #task 1
# n = int(input())

# if n == 0:
#     print("Teg")
# else:
#     if n > 0:
#         temdeg = "Eereg"
#     else:
#         temdeg = "Surug"
#     if n % 2 == 0:
#         tegsh = "tegsh"
#     else:
#         tegsh = "sondgoi"
#     print(temdeg, tegsh)

# #task 2
# x = int(input())

# if x < 0 or x > 100:
#     print("Buruu onoo")
# elif x >= 90:
#     print("A")
# elif x >= 80:
#     print("B")
# elif x >= 70:
#     print("C")
# elif x >= 60:
#     print("D")
# else:
#     print("F")

# #task 3
# on = int(input())

# if (on % 4 == 0 and on % 100 != 0) or on % 400 == 0:
#     print("Undur jil")
# else:
#     print("Engiin jil")

# #task 4
# a, b, c = map(int, input().split())

# if a + b <= c or a + c <= b or b + c <= a:
#     print("Gurvaljin uusehgui")
# elif a == b == c:
#     print("Tegsh talt")
# elif a == b or a == c or b == c:
#     print("Adil hajuut")
# else:
#     print("Engiin")

# #task 5
# km, tsag = map(int, input().split())

# if km <= 2:
#     tulbur = 3000
# else:
#     tulbur = 3000 + (km - 2) * 1500

# if tsag >= 22 or tsag <= 5:
#     tulbur += 2000

# print(tulbur)

# #task 6
# n = int(input())
# niilber = 0

# for i in range(2, n + 1, 2):
#     niilber += i

# print(niilber)

# #task 7
# n = int(input())
# niilber = 0

# while n > 0:
#     niilber += n % 10
#     n //= 10

# print(niilber)

# #task 8
# n = int(input())
# urvuu = 0

# while n > 0:
#     urvuu = urvuu * 10 + n % 10
#     n //= 10

# print(urvuu)

# #task 9
# n = int(input())

# for i in range(1, n + 1):
#     if i % 15 == 0:
#         print("FizBazz", end=" ")
#     elif i % 3 == 0:
#         print("Fiz", end=" ")
#     elif i % 5 == 0:
#         print("Bazz", end=" ")
#     else:
#         print(i, end=" ")
# print()


# #task 10
# secret = 37
# oroldlogo = 0

# while True:
#     x = int(input())
#     oroldlogo += 1
#     if x == secret:
#         print(f"Zuv! {oroldlogo} oroldlogoor")
#         break
#     elif x > secret:
#         print("Ih baina")
#     else:
#         print("Baga baina")

#     if oroldlogo == 5:
#         print("Yalagdlaa")
#         break

# #task 11
# n = int(input())

# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         print(i * j, end=" ")
#     print()

# #task 12
# n = int(input())

# for i in range(1, n + 1):
#     for j in range(n - i):
#         print(" ", end="")
#     for j in range(2 * i - 1):
#         print("*", end="")
#     print()

# #task 13
# def find_pairs(arr, target):
#     pairs = []
#     for i in range(len(arr)):
#         for j in range(i + 1, len(arr)):
#             if arr[i] + arr[j] == target:
#                 pairs.append((arr[i], arr[j]))
#     return pairs


# print(find_pairs([2, 7, 4, 5, 1], 6))
# print(find_pairs([1, 2, 3], 10))

# #task 14
# def most_frequent(arr):
#     best = arr[0]
#     best_count = 0
#     for i in range(len(arr)):
#         count = 0
#         for j in range(len(arr)):
#             if arr[j] == arr[i]:
#                 count += 1
#         if count > best_count:
#             best = arr[i]
#             best_count = count
#     return (best, best_count)


# print(most_frequent([4, 1, 4, 2, 1, 4]))
# print(most_frequent([7, 3, 3, 7]))

# #task 15
# def row_col_sums(matrix):
#     rows = []
#     for i in range(len(matrix)):
#         niilber = 0
#         for j in range(len(matrix[i])):
#             niilber += matrix[i][j]
#         rows.append(niilber)

#     cols = []
#     for j in range(len(matrix[0])):
#         niilber = 0
#         for i in range(len(matrix)):
#             niilber += matrix[i][j]
#         cols.append(niilber)

#     return (rows, cols)


# print(row_col_sums([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
# print(row_col_sums([[2, 0], [1, 5], [3, 3]]))

# #task 16
# def remove_duplicates(arr):
#     harsan = set()
#     result = []
#     for x in arr:
#         if x not in harsan:
#             harsan.add(x)
#             result.append(x)
#     return result


# print(remove_duplicates([3, 1, 3, 2, 1, 5]))
# print(remove_duplicates(["a", "b", "a"]))

# #task 17
# def word_count(text):
#     count = {}
#     for word in text.split():
#         if word in count:
#             count[word] += 1
#         else:
#             count[word] = 1
#     return count


# print(word_count("alim banana alim jurj banana alim"))

# #task 18
# def averages(grades):
#     dundaj = {}
#     best_name = ""
#     best_avg = -1
#     for name in grades:
#         dundaj[name] = sum(grades[name]) / len(grades[name])
#         if dundaj[name] > best_avg:
#             best_avg = dundaj[name]
#             best_name = name
#     return (dundaj, best_name)


# print(averages({"Anar": [80, 90, 70], "Bold": [60, 75, 90], "Saraa": [95, 85, 90]}))

# #task 19
# python = {"Anar", "Bold", "Saraa", "Dorj"}
# math = {"Bold", "Gerel", "Dorj"}

# print("Hoyuland:", python & math)
# print("Zuvhun Python:", python - math)
# print("Zuvhun matematik:", math - python)
# print("Niit:", len(python | math))

# #task 20
# def farthest_point(points):
#     best = points[0]
#     x, y = points[0]
#     best_dist = x ** 2 + y ** 2
#     for point in points:
#         x, y = point
#         dist = x ** 2 + y ** 2
#         if dist > best_dist:
#             best = point
#             best_dist = dist
#     return (best, best_dist)


# print(farthest_point([(1, 2), (3, 4), (-1, 5), (0, 0)]))

# #task 21
# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             return False
#     return True


# def primes_up_to(n):
#     primes = []
#     for i in range(2, n + 1):
#         if is_prime(i):
#             primes.append(i)
#     return primes


# print(is_prime(17))
# print(is_prime(1))
# print(is_prime(21))
# print(primes_up_to(20))

# #task 22
# def find_all(arr, x):
#     indexes = []
#     for i in range(len(arr)):
#         if arr[i] == x:
#             indexes.append(i)
#     return indexes


# print(find_all([5, 3, 5, 1, 5], 5))
# print(find_all([5, 3, 5, 1, 5], 9))

# #task 23
# def find_phone(book, name):
#     for ner, dugaar in book:
#         if ner == name:
#             return dugaar
#     return "Oldsongui"


# book = [("Anar", "99112233"), ("Bold", "88001122"), ("Saraa", "95553344")]

# print(find_phone(book, "Bold"))
# print(find_phone(book, "Dorj"))

# #task 24
# def bs_steps(arr, x):
#     low = 0
#     high = len(arr) - 1
#     alham = 0
#     while low <= high:
#         mid = (low + high) // 2
#         alham += 1
#         if arr[mid] == x:
#             return (mid, alham)
#         elif arr[mid] < x:
#             low = mid + 1
#         else:
#             high = mid - 1
#     return (-1, alham)


# arr = [1, 3, 5, 7, 9, 11, 13, 15]

# print(bs_steps(arr, 11))
# print(bs_steps(arr, 4))
# print(bs_steps(arr, 7))

# #task 25
# def search_insert(arr, x):
#     low = 0
#     high = len(arr) - 1
#     while low <= high:
#         mid = (low + high) // 2
#         if arr[mid] == x:
#             return mid
#         elif arr[mid] < x:
#             low = mid + 1
#         else:
#             high = mid - 1
#     return low


# arr = [1, 3, 5, 6]

# print(search_insert(arr, 5))
# print(search_insert(arr, 2))
# print(search_insert(arr, 7))
# print(search_insert(arr, 0))

# #task 26
# def bubble_sort(arr):
#     n = len(arr)
#     swap_count = 0
#     for i in range(n - 1):
#         swapped = False
#         for j in range(n - 1 - i):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#                 swap_count += 1
#                 swapped = True
#         if not swapped:
#             break
#     return (arr, swap_count)


# print(bubble_sort([5, 1, 4, 2, 8]))
# print(bubble_sort([1, 2, 3]))
# print(bubble_sort([3, 2, 1]))

# #task 27
# def selection_sort(arr):
#     n = len(arr)
#     for i in range(n - 1):
#         min_index = i
#         for j in range(i + 1, n):
#             if arr[j] < arr[min_index]:
#                 min_index = j
#         arr[i], arr[min_index] = arr[min_index], arr[i]
#         print(f"{i + 1}-r alham: {arr}")


# selection_sort([64, 25, 12, 22, 11])

# #task 28
# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     mid = len(arr) // 2
#     left = merge_sort(arr[:mid])
#     right = merge_sort(arr[mid:])

#     result = []
#     i = j = 0
#     while i < len(left) and j < len(right):
#         if left[i] <= right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
#     result.extend(left[i:])
#     result.extend(right[j:])
#     return result


# def sort_unique(arr):
#     arr = merge_sort(arr)
#     result = []
#     for x in arr:
#         if len(result) == 0 or result[-1] != x:
#             result.append(x)
#     return result


# print(sort_unique([4, 2, 4, 1, 2, 9]))
# print(sort_unique([7, 7, 7]))

# #task 29
# def top_three(scores):
#     pairs = []
#     for name in scores:
#         pairs.append((scores[name], name))
#     pairs.sort(reverse=True)

#     result = []
#     for score, name in pairs[:3]:
#         result.append(name)
#     return result


# print(top_three({"Anar": 85, "Bold": 92, "Saraa": 78, "Dorj": 88, "Gerel": 95}))

#task 30
# n = int(input())
# onoonuud = []
# for i in range(n):
#     onoonuud.append(int(input()))

# onoonuud.sort()
# dundaj = sum(onoonuud) / n

# deesh = 0
# for x in onoonuud:
#     if x > dundaj:
#         deesh += 1

# print("Erembelsen:", onoonuud)
# print("Hamgiin ih:", onoonuud[-1])
# print("Hamgiin baga:", onoonuud[0])
# print("Dundaj:", dundaj)
# print("Dundjaas deesh:", deesh)