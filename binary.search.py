# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# target = int(input("Too og: "))

# left = 0
# right = len(lst) - 1

# while left <= right:
#     mid = (left + right) // 2

#     if lst[mid] == target:
#         print("Oldloo. Index:", mid)
#         break
#     elif lst[mid] < target:
#         left = mid + 1
#     else:
#         right = mid - 1
# else:
#     print("Oldsongui")

#task 1
# def binary_search(lst, target):
#     left = 0
#     right = len(lst) - 1

#     while left <= right:
#         mid = (left + right) // 2

#         if lst[mid] == target:
#             return mid
#         elif lst[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1

#     return -1


# lst = list(map(int,input("toonuud og: ").split()))
# lst.sort()
# target = int(input("Too og: "))

# result = binary_search(lst, target)

# if result != -1:
#     print("Oldloo)
# else:
#     print("Oldsongui")
    

#task 2
# def binary_search(lst, target):
#     left = 0
#     right = len(lst) - 1

#     while left <= right:
#         mid = (left + right) // 2

#         if lst[mid] == target:
#             return mid
#         elif lst[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1

#     return -1


# lst = list(map(int,input("toonuud og: ").split()))
# lst.sort()
# target = int(input("Too og: "))

# result = binary_search(lst, target)

# if result != -1:
#     print("Oldloo. Index:", result)
# else:
#     print(binary_search(lst,target))


#task 3
# def binary_search(lst, target):
#     left = 0
#     right = len(lst) - 1

#     while left <= right:
#         mid = (left + right) // 2

#         if lst[mid] == target:
#             return mid
#         elif lst[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1

#     return -1


# lst = list(map(int,input("toonuud og: ").split()))
# lst.sort()
# target = int(input("Too og: "))

# result = binary_search(lst, target)

# if result != -1:
#     print("Oldloo. Index:", result)
# else:
#     print("oldsongue")

#task 4
# def binary_search(lst, target):
#     left = 0
#     right = len(lst) - 1

#     while left <= right:
#         mid = (left + right) // 2

#         if lst[mid] == target:
#             return mid
#         elif lst[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1

#     return -1
# lst = list(map(int,input("toonuud og: ").split()))
# lst.sort()
# target = int(input('too og: '))

# result = binary_search(lst,target)

# if result != -1:
#     print("oldloo. Index: ", result)
# else:
#     print("oldsongu")


#task 5
# def binary_search(lst,target):
#     left = 0
#     right = len(lst) - 1

#     while left <= right:

#         mid = (left + right) // 2

#         if lst[mid] == target:
#             return mid
#         elif lst[mid] < target:
#             left = mid + 1 
#         else:
#             right = mid - 1
#     return -1

# lst = list(map(int,input("toonuud og: ").split()))
# lst.sort()
# target = int(input("too og: "))

# result = binary_search(lst, target)

# if result != -1:
#     print("oldloo. index: ", result)
# else:
#     print("haij bui too bhgu")

#task 6
# def binary_search(lst, target):
#     left = 0
#     right = len(lst) - 1
#     count = 0
#     while left <= right:
#         mid = (left + right) // 2
#         count += 1

#         if lst[mid] == target:
#             return mid, count
#         elif lst[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return -1, count

# lst = list(map(int, input("Toonuudaa oruul: ").split()))
# lst.sort()

# target = int(input("too og: "))

# result, count = binary_search(lst, target)

# if result != -1:
#     print("oldloo. Index:", result)
#     print( count, "udaа shalgalaa.")
# else:
#     print("oldsongui.")
#     print("Niit", count, "udaа shalgalaa.")

#task 7
# def binary_search(lst,target):
#     left = 0
#     right = len(lst) - 1
#     while left <= right:
#         mid = (left + right) // 2

#         if lst[mid] == target:
#             return mid
#         elif lst[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return -1
# lst = list(map(int,input("toonuudaa oruul: ").split()))
# lst.sort()
# target = int(input("onoo og: "))
# result = binary_search(lst, target)
# if result != -1:
#     print( "oldloo. Index: ", result)
# else:
#     print("oldsongui")

# #task 8
# def binary_search(lst,target):
#     left = 0
#     right = len(lst) - 1
#     while left <= right:
#         mid = (left + right) // 2

#         if lst[mid] == target:
#             return mid
#         elif lst[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return -1
# lst = list(map(int,input("baraanii codenuud: ").split()))
# lst.sort()
# target = int(input("haih baraani code: "))
# result = binary_search(lst, target)
# if result != -1:
#     print( "burtgeltei")
# else:
#     print("burtgelgui")

# #task 9
# def binary_search(lst,target):
#     left = 0
#     right = len(lst) - 1
#     while left <= right:
#         mid = (left + right) // 2

#         if lst[mid] == target:
#             return mid
#         elif lst[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return -1
# lst = list(map(int,input("nomiin dugaaruud: ").split()))
# lst.sort()
# target = int(input("haih nomiin dugaar: "))
# result = binary_search(lst, target)
# if result != -1:
#     print( "oldloo. Index: ", result)
# else:
#     print(result)

# #task 10 
# def binary_search(lst,target):
#     left = 0
#     right = len(lst) - 1
#     while left <= right:
#         mid = (left + right) // 2

#         if lst[mid] == target:
#             return mid
#         elif lst[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return -1
# lst = list(map(int,input("toonuudaa oruul: ").split()))
# lst.sort()
# target = int(input("onoo og: "))
# result = binary_search(lst, target)
# if result != -1:
#     print( "oldloo. Index: ", result)
# else:
#     print("oldsongui")

# #task 11
# def first_index(lst,target):
#     left = 0
#     right = len(lst) - 1
#     result = -1
#     while left <= right:
#         mid = (left + right) // 2

#         if lst[mid] == target:
#             result = mid
#             right = mid - 1
#         elif lst[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return result
# lst = list(map(int,input("toonuudaa oruul: ").split()))
# lst.sort()
# target = int(input("too og: "))
# result = first_index(lst, target)
# if result != -1:
#     print("hamgiin ehnii index: ", result)
# else:
#     print("oldsongui")

# #task 12
# def last_index(lst,target):
#     left = 0
#     right = len(lst) - 1
#     result = -1
#     while left <= right:
#         mid = (left + right) // 2

#         if lst[mid] == target:
#             result = mid
#             left = mid + 1
#         elif lst[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return result
# lst = list(map(int,input("toonuudaa oruul: ").split()))
# lst.sort()
# target = int(input("too og: "))
# result = last_index(lst, target)
# if result != -1:
#     print("hamgiin suuliin index: ", result)
# else:
#     print("oldsongui")

# #task 13
# def insert_position(lst,target):
#     left = 0
#     right = len(lst) - 1
#     while left <= right:
#         mid = (left + right) // 2

#         if lst[mid] == target:
#             return mid
#         elif lst[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return left
# lst = list(map(int,input("toonuudaa oruul: ").split()))
# lst.sort()
# target = int(input("too og: "))
# result = insert_position(lst, target)
# if result < len(lst) and lst[result] == target:
#     print("jagsaaltad baina. Index: ", result)
# else:
#     print("oruulah index: ", result)

# #task 14
# def closest_smaller(lst,target):
#     left = 0
#     right = len(lst) - 1
#     result = -1
#     while left <= right:
#         mid = (left + right) // 2

#         if lst[mid] < target:
#             result = mid
#             left = mid + 1
#         else:
#             right = mid - 1
#     return result
# lst = list(map(int,input("toonuudaa oruul: ").split()))
# lst.sort()
# target = int(input("too og: "))
# result = closest_smaller(lst, target)
# if result != -1:
#     print("baga hamgiin oir too: ", lst[result])
# else:
#     print("baihgui")

# #task 15
# def closest_bigger(lst,target):
#     left = 0
#     right = len(lst) - 1
#     result = -1
#     while left <= right:
#         mid = (left + right) // 2

#         if lst[mid] > target:
#             result = mid
#             right = mid - 1
#         else:
#             left = mid + 1
#     return result
# lst = list(map(int,input("toonuudaa oruul: ").split()))
# lst.sort()
# target = int(input("too og: "))
# result = closest_bigger(lst, target)
# if result != -1:
#     print("ih hamgiin oir too: ", lst[result])
# else:
#     print("baihgui")

# #task 16
# def binary_search(lst,target):
#     left = 0
#     right = len(lst) - 1
#     while left <= right:
#         mid = (left + right) // 2

#         if lst[mid] == target:
#             return mid
#         elif lst[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return -1
# lst = list(map(int,input("toonuudaa oruul: ").split()))
# lst.sort()
# a = int(input("a og: "))
# b = int(input("b og: "))
# result_a = binary_search(lst, a)
# result_b = binary_search(lst, b)
# if result_a != -1:
#     print("a oldloo. Index: ", result_a)
# else:
#     print("a oldsongui")
# if result_b != -1:
#     print("b oldloo. Index: ", result_b)
# else:
#     print("b oldsongui")

# #task 17
# def binary_search_desc(lst,target):
#     left = 0
#     right = len(lst) - 1
#     while left <= right:
#         mid = (left + right) // 2

#         if lst[mid] == target:
#             return mid
#         elif lst[mid] > target:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return -1
# lst = list(map(int,input("toonuudaa oruul: ").split()))
# lst.sort(reverse=True)
# target = int(input("too og: "))
# result = binary_search_desc(lst, target)
# if result != -1:
#     print("oldloo. Index: ", result)
# else:
#     print("oldsongui")

# #task 18
# def binary_search(numbers,target):
#     left = 0
#     right = len(numbers) - 1
#     while left <= right:
#         mid = (left + right) // 2

#         if numbers[mid] == target:
#             return mid
#         elif numbers[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return -1
# numbers = list(map(int,input("toonuudaa oruul: ").split()))
# numbers.sort()
# target = int(input("too og: "))
# print(binary_search(numbers, target))

# #task 19
# def first_index(lst,target):
#     left = 0
#     right = len(lst) - 1
#     result = -1
#     while left <= right:
#         mid = (left + right) // 2

#         if lst[mid] == target:
#             result = mid
#             right = mid - 1
#         elif lst[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return result
# def last_index(lst,target):
#     left = 0
#     right = len(lst) - 1
#     result = -1
#     while left <= right:
#         mid = (left + right) // 2

#         if lst[mid] == target:
#             result = mid
#             left = mid + 1
#         elif lst[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return result
# lst = list(map(int,input("toonuudaa oruul: ").split()))
# lst.sort()
# target = int(input("too og: "))
# first = first_index(lst, target)
# last = last_index(lst, target)
# if first != -1:
#     print(target, "too", last - first + 1, "udaa baina")
# else:
#     print(target, "too baihgui")

# #task 20
# def linear_search(lst,target):
#     count = 0
#     for i in range(len(lst)):
#         count += 1
#         if lst[i] == target:
#             return i, count
#     return -1, count
# def binary_search(lst,target):
#     left = 0
#     right = len(lst) - 1
#     count = 0
#     while left <= right:
#         mid = (left + right) // 2
#         count += 1

#         if lst[mid] == target:
#             return mid, count
#         elif lst[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return -1, count
# lst = list(map(int,input("toonuudaa oruul: ").split()))
# lst.sort()
# target = int(input("too og: "))
# linear_index, linear_count = linear_search(lst, target)
# binary_index, binary_count = binary_search(lst, target)
# print("linear search: ", linear_count, "udaa shalgalaa")
# print("binary search: ", binary_count, "udaa shalgalaa")
# if binary_count < linear_count:
#     print("binary search tsoon shalgalt hiisen")
# elif linear_count < binary_count:
#     print("linear search tsoon shalgalt hiisen")
# else:
#     print("hoyulaa adilhan too shalgalt hiisen")