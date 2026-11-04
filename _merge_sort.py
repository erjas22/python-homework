def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


numbers = [38, 27, 43, 3, 9, 82, 10]

print("Өмнө:", numbers)
print("Дараа:", merge_sort(numbers))


# #task 1
# def merge(left, right):
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


# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     mid = len(arr) // 2
#     left = merge_sort(arr[:mid])
#     right = merge_sort(arr[mid:])
#     return merge(left, right)


# numbers = list(map(int,input("toonuud og: ").split()))

# print("Өмнө:", numbers)
# print("Дараа:", merge_sort(numbers))

# # #task 2
# # def merge_sort_desc(arr):
# #     if len(arr) <= 1:
# #         return arr
# #     mid = len(arr) // 2
# #     left = merge_sort_desc(arr[:mid])
# #     right = merge_sort_desc(arr[mid:])

# #     result = []
# #     i = j = 0
# #     while i < len(left) and j < len(right):
# #         if left[i] >= right[j]:
# #             result.append(left[i])
# #             i += 1
# #         else:
# #             result.append(right[j])
# #             j += 1
# #     result.extend(left[i:])
# #     result.extend(right[j:])
# #     return result


# # numbers = list(map(int,input("toonuud og: ").split()))

# # print("Өмнө:", numbers)
# # print("Дараа:", merge_sort_desc(numbers))


# #task 3
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


# numbers = list(map(int,input("toonuud og: ").split()))

# print("Өмнө:", numbers)
# print("Дараа:", merge_sort(numbers))


#task 4
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


# numbers = list(map(int,input("toonuud og: ").split()))

# print("Өмнө:", numbers)
# print("Дараа:", merge_sort(numbers))


#task 5
# def even_odd_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     mid = len(arr) // 2
#     left = even_odd_sort(arr[:mid])
#     right = even_odd_sort(arr[mid:])

#     result = []
#     i = j = 0
#     while i < len(left) and j < len(right):
#         a = left[i]
#         b = right[j]
#         if (a % 2 == 0 and b % 2 != 0) or (a % 2 == b % 2 and a <= b):
#             result.append(a)
#             i += 1
#         else:
#             result.append(b)
#             j += 1
#     result.extend(left[i:])
#     result.extend(right[j:])
#     return result


# numbers = list(map(int,input("toonuud og: ").split()))

# print("Өмнө:", numbers)
# print("Дараа:", even_odd_sort(numbers))

#task 6
# def merge(a, b):
#     result = []
#     i = j = 0
#     while i < len(a) and j < len(b):
#         if a[i] <= b[j]:
#             result.append(a[i])
#             i += 1
#         else:
#             result.append(b[j])
#             j += 1
#     result.extend(a[i:])
#     result.extend(b[j:])
#     return result


# a = list(map(int,input("a-d toonuud og: ").split()))
# b = list(map(int,input("b-d toonuud og: ").split()))

# print("Өмнө:", a, b)
# print("Дараа:", merge(a, b))

#task 7
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


# def smallest_three(arr):
#     return merge_sort(arr)[:3]


# numbers = list(map(int,input("toonuud og: ").split()))

# print("Hamgiin baga 3:", smallest_three(numbers))

#task 8
# def merge_sort_count(arr):
#     if len(arr) <= 1:
#         return arr, 0, 0
#     mid = len(arr) // 2
#     left, left_count, left_merge = merge_sort_count(arr[:mid])
#     right, right_count, right_merge = merge_sort_count(arr[mid:])

#     result = []
#     i = j = 0
#     count = left_count + right_count
#     while i < len(left) and j < len(right):
#         count += 1
#         if left[i] <= right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
#     result.extend(left[i:])
#     result.extend(right[j:])
#     return result, count, left_merge + right_merge + 1


# numbers = list(map(int,input("toonuud og: ").split()))

# erembelsen, count, merge_count = merge_sort_count(numbers)
# print("Эрэмбэлсэн:", erembelsen)
# print("Харьцуулалт:", count)
# print("Merge:", merge_count)


#task 9
# def merge_sort_desc(arr):
#     if len(arr) <= 1:
#         return arr
#     mid = len(arr) // 2
#     left = merge_sort_desc(arr[:mid])
#     right = merge_sort_desc(arr[mid:])

#     result = []
#     i = j = 0
#     while i < len(left) and j < len(right):
#         if left[i] >= right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
#     result.extend(left[i:])
#     result.extend(right[j:])
#     return result


# def largest_two(arr):
#     return merge_sort_desc(arr)[:2]


# numbers = list(map(int,input("toonuud og: ").split()))

# print("Hamgiin ih 2:", largest_two(numbers))

#task 10
# def merge_sort(names):
#     if len(names) <= 1:
#         return names
#     mid = len(names) // 2
#     left = merge_sort(names[:mid])
#     right = merge_sort(names[mid:])

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


# names = input("nersee og: ").split()

# print("Omno:", names)
# print("Daraa:", merge_sort(names))


#task 11
# def sort_students(students):
#     if len(students) <= 1:
#         return students
#     mid = len(students) // 2
#     left = sort_students(students[:mid])
#     right = sort_students(students[mid:])

#     result = []
#     i = j = 0
#     while i < len(left) and j < len(right):
#         a = left[i]
#         b = right[j]
#         if a[1] > b[1] or (a[1] == b[1] and a[0] <= b[0]):
#             result.append(a)
#             i += 1
#         else:
#             result.append(b)
#             j += 1
#     result.extend(left[i:])
#     result.extend(right[j:])
#     return result


# n = int(input("suragchiin too: "))
# students = []
# for _ in range(n):
#     ner, onoo = input("ner onoo: ").split()
#     students.append((ner, int(onoo)))

# print("Omno:", students)
# print("Daraa:", sort_students(students))

#task 12
# def sort_words(words):
#     if len(words) <= 1:
#         return words
#     mid = len(words) // 2
#     left = sort_words(words[:mid])
#     right = sort_words(words[mid:])

#     result = []
#     i = j = 0
#     while i < len(left) and j < len(right):
#         a = left[i]
#         b = right[j]
#         if len(a) < len(b) or (len(a) == len(b) and a <= b):
#             result.append(a)
#             i += 1
#         else:
#             result.append(b)
#             j += 1
#     result.extend(left[i:])
#     result.extend(right[j:])
#     return result


# words = input("ugsee og: ").split()

# print("Omno:", words)
# print("Daraa:", sort_words(words))

#task 13
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


# def binary_search(arr, target):
#     arr = merge_sort(arr)
#     left = 0
#     right = len(arr) - 1

#     while left <= right:
#         mid = (left + right) // 2

#         if arr[mid] == target:
#             return mid
#         elif arr[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1

#     return -1


# numbers = list(map(int,input("toonuud og: ").split()))
# target = int(input("haih too og: "))

# print("Erembelsen:", merge_sort(numbers))
# print("Index:", binary_search(numbers, target))


#task 14
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


# def is_anagram(word1, word2):
#     return merge_sort(list(word1)) == merge_sort(list(word2))


# word1 = input("1-r ug og: ")
# word2 = input("2-r ug og: ")

# print(is_anagram(word1, word2))

#task 15
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


# def closest_pair(arr):
#     arr = merge_sort(arr)
#     pair = (arr[0], arr[1])
#     min_diff = arr[1] - arr[0]

#     for i in range(1, len(arr) - 1):
#         diff = arr[i + 1] - arr[i]
#         if diff < min_diff:
#             min_diff = diff
#             pair = (arr[i], arr[i + 1])

#     return pair, min_diff


# numbers = list(map(int,input("toonuud og: ").split()))

# pair, diff = closest_pair(numbers)
# print("Erembelsen:", merge_sort(numbers))
# print("Garalt:", pair, "zoruu =", diff)