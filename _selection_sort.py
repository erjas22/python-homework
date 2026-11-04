# #task 1
# arr = list(map(int,input("toonuud og: ").split()))

# for i in range(len(arr)):
#     min_index = i
#     for j in range(i + 1, len(arr)):
#         if arr[j] < arr[min_index]:
#             min_index = j
#     arr[i], arr[min_index] = arr[min_index], arr[i]

# print(arr)


# #task 2
# arr = list(map(int,input("toonuud og: ").split()))

# for i in range(3):
#     min_index = i
#     for j in range(i + 1, len(arr)):
#         if arr[j] < arr[min_index]:
#             min_index = j
#     arr[i], arr[min_index] = arr[min_index], arr[i]

# print(arr)


# #task 3
# arr = list(map(int,input("toonuud og: ").split()))

# for i in range(len(arr)):
#     max_index = i
#     for j in range(i + 1, len(arr)):
#         if arr[j] > arr[max_index]:
#             max_index = j
#     arr[i], arr[max_index] = arr[max_index], arr[i]

# print(arr)


# #task 4
# arr = list(map(int,input("toonuud og: ").split()))

# for i in range(len(arr)):
#     min_index = i
#     for j in range(i + 1, len(arr)):
#         if arr[j] < arr[min_index]:
#             min_index = j
#     arr[i], arr[min_index] = arr[min_index], arr[i]

# print(arr)


# #task 5
# arr = list(map(int,input("toonuud og: ").split()))
# unique = []

# for x in arr:
#     if x not in unique:
#         unique.append(x)

# for i in range(len(unique)):
#     min_index = i
#     for j in range(i + 1, len(unique)):
#         if unique[j] < unique[min_index]:
#             min_index = j
#     unique[i], unique[min_index] = unique[min_index], unique[i]

# print(unique)


# #task 6
# arr = list(map(int,input("toonuud og: ").split()))

# min_index = 0
# for j in range(1, len(arr)):
#     if arr[j] < arr[min_index]:
#         min_index = j
# arr[0], arr[min_index] = arr[min_index], arr[0]

# print(arr)


# #task 7
# arr = list(map(int,input("toonuud og: ").split()))

# min_index = 0
# for j in range(1, len(arr)):
#     if arr[j] < arr[min_index]:
#         min_index = j
# arr[0], arr[min_index] = arr[min_index], arr[0]

# print(arr)


# #task 8
# arr = list(map(int,input("toonuud og: ").split()))

# for i in range(2):
#     min_index = i
#     for j in range(i + 1, len(arr)):
#         if arr[j] < arr[min_index]:
#             min_index = j
#     arr[i], arr[min_index] = arr[min_index], arr[i]
#     print(f"{i + 1}-r alhmiin daraa: {arr}")


# #task 9
# arr = list(map(int,input("toonuud og: ").split()))
# count = 0

# for i in range(len(arr)):
#     min_index = i
#     for j in range(i + 1, len(arr)):
#         if arr[j] < arr[min_index]:
#             min_index = j
#     if min_index != i:
#         arr[i], arr[min_index] = arr[min_index], arr[i]
#         count += 1

# print(f"{count} udaa solison, {arr}")


#task 10
a = list(map(int,input("a toonuud og: ").split()))
b = list(map(int,input("b toonuud og: ").split()))
c = list(map(int,input("c toonuud og: ").split()))

# for name, lst in [("a", a), ("b", b), ("c", c)]:
#     sorted_ok = True
#     for i in range(len(lst) - 1):
#         if lst[i] > lst[i + 1]:
#             sorted_ok = False
#             break
#     if sorted_ok:
#         print(f"{name} erembelegdsen")

for name, lst in [("a", a), ("b", b), ("c", c)]:
    count = 0
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            count += 1 
            break
    if count == 0:
        print(f"eremblegdsen")
    else:
        print(f"eremblegdeegui")



# #task 11
# def selection_sort(arr):
#     for i in range(len(arr)):
#         min_index = i
#         for j in range(i + 1, len(arr)):
#             if arr[j] < arr[min_index]:
#                 min_index = j
#         arr[i], arr[min_index] = arr[min_index], arr[i]
#     return arr

# arr = list(map(int,input("toonuud og: ").split()))
# print(selection_sort(arr))


# #task 12
# def selection_sort_desc(arr):
#     for i in range(len(arr)):
#         max_index = i
#         for j in range(i + 1, len(arr)):
#             if arr[j] > arr[max_index]:
#                 max_index = j
#         arr[i], arr[max_index] = arr[max_index], arr[i]
#     return arr

# arr = list(map(int,input("toonuud og: ").split()))
# print(selection_sort_desc(arr))


# #task 13
# arr = list(map(int,input("toonuud og: ").split()))

# min_index = 0
# for j in range(1, len(arr)):
#     if arr[j] < arr[min_index]:
#         min_index = j

# print(f"hamgiin baga element {arr[min_index]}, index: {min_index}")


# #task 14
# arr = list(map(int,input("toonuud og: ").split()))

# for i in range(len(arr)):
#     min_index = i
#     for j in range(i + 1, len(arr)):
#         if arr[j] < arr[min_index]:
#             min_index = j
#     arr[i], arr[min_index] = arr[min_index], arr[i]
#     print(f"{i + 1}-r alham: {arr}")


# #task 15
# arr = list(map(int,input("toonuud og: ").split()))
# bubble = arr.copy()
# selection = arr.copy()

# for i in range(len(bubble)):
#     for j in range(len(bubble) - 1 - i):
#         if bubble[j] > bubble[j + 1]:
#             bubble[j], bubble[j + 1] = bubble[j + 1], bubble[j]

# for i in range(len(selection)):
#     min_index = i
#     for j in range(i + 1, len(selection)):
#         if selection[j] < selection[min_index]:
#             min_index = j
#     selection[i], selection[min_index] = selection[min_index], selection[i]

# print(f"bubble: {bubble}, selection: {selection}")
# if bubble == selection:
#     print("ijil")
# else:
#     print("ondoo")