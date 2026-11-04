#task1 
# nums = {1 , 2, 2, 3, 4, 4, 5}
# print(nums)

#task 2,3
# fruits ={"apple", "banana"}
# fruits.add("orange")
# print(fruits)
# fruits.remove("banana")
# print(fruits)

#task 4
# nums = {10, 20, 30, 40,}
# i = int(input("too og: "))
# if i in nums:
#     print("YES")
# else:
#     print("No")

#task 5
# nums = set(map(int,input("too og: ").split()))
# print(len(nums))

#task 6
# names = {"bat", "sara", "bat", "bold", "sara", "anu"}
# print(len(names))

#task 7
# a = {1, 2, 3}
# b = {3, 4, 5}
# all_nums = a | b
# print(all_nums)

#task 8
# a = {1, 2, 3, 4}
# b = {3, 4, 5 ,6}
# both = a & b
# print(both)

#task 9
# a = {1, 2, 3, 4}
# b = {3, 4, 5 ,6}
# print(a - b)
# print(b - a)

#task 10
# python_students = {"bat", "sara", "bold", "anu"}
# java_student = {"sara", "bold", "temuulen"}
# both = python_students & java_student
# print(both)

#task 11
# python = {"bat", "sara", "bold", "anu"}
# java = {"sara", "bold", "temuulen"}
# result = tuple(python - java, java - python)
# print(result)

#task 12
# a = str(input("ug og: "))
# b = set(a)
# print(len(b))

#task 13
# student = {
#     "name" : "Bat",
#     "age" : 18,
#     "score" : 95
# }
# print(student)

#task 14
# student = {
#     "name" : "Bat",
#     "age" : 18,
#     "score" : 95
# }
# print(student["name"])

#task 15
# student = {
#     "name" : "Bat",
#     "age" : 18,
#     "score" : 95
# }
# student["score"] = 95
# print(student["score"])

#task 16
# student = {
#     "name" : "Bat",
#     "age" : 18,
#     "score" : 95
# }
# student["city"] = "Ulaanbaatar"
# student["score"] = 95
# print(student)

#task 17
# student = {
#     "name" : "Bold",
#     "age" : 20,
#     "year" : 88
# }
# del student["age"]
# print(student)

#task 18
# car = {
#     "brand" : "toyata",
#     "model" : "pruis",
#     "year" :2015
# }
# for key in car:
#     print(key)

#task 19
# car = {
#     "brand" : "toyata",
#     "model" : "pruis",
#     "year" : 2015
# }
# print(car.values())

#task 20
# student = {
#     "name":"bat",
#     "age":18,
#     "score":95
# }
# for key in student.keys():
#     value = student[key]
#     print(key, value)

#task 21
# student = {
#     "name":"bat",
#     "age":18,
#     "score":95
# }
# if student.get("score"):
#     print("yes")
# else:
#     print("no")

#task 22
# product = {
#     "name" : "Keyboard",
#     "price" : 1200000,
#     "stock" : 5
# }
# if product["stock"] > 0:
#     print("avaible")
# else:
#     print("Out of stock")

#task 23
# scores = {
#     "bat": 80,
#     "sara": 95,
#     "bold": 70,
#     "anu": 88
# }
# for name, score in scores.items():
#     if score >= 80:
#         print(name,score)

#task 24
# scores = {
#     "bat": 80,
#     "sara": 95,
#     "bold": 70,
#     "anu": 88
# }
# max_n = 0
# max_name = ""
# for name, score in scores.items():
#     if score > max_n:
#         max_n = score
#         max_name = name
#         print(max_name, max_n)

# print(max(scores.items()))

# best = max(scores, key = scores.get)
# score = scores[best]
# print(best, score)

#task 25
# sales = {
#     "monday": 10,
#     "tuesday": 15,
#     "wednesday": 20
# }
# print(sum(sales.values()))

#task 26
animal = input("Өгүүлбэр оруулна уу: ").split()
counts = {}
for word in animal:
    counts[word] = counts.get(word, 0) + 1
for word, count in counts.items():
    print(word, count)

#task 27
# students = {
#     "Bat": ["Python", "Java"],
#     "Sara": ["Python", "C++"],
#     "Bold": ["Java", "Python"]
# }
# subjects = set()
# for lessons in students.values():
#     subjects.update(lessons)
# for subject in sorted(subjects, reverse=True):
#     print(subject)

#task 28 
# students = {
#     "Bat": "Ulaanbaatar",
#     "Sara": "Darkhan",
#     "Bold": "Ulaanbaatar",
#     "Anu": "Erdenet",
#     "Temuulen": "Darkhan"
# }
# cities = set(students.values())
# print(len(cities))

#task 29
# students = {
#     "bat" : "Ulaanbaatar",
#     "sara" : "Darkhan",
#     "bold" : "Ulaanbaatar",
#     "Anu" : "Erdenet"
# }
# for name, city in students.items():
#     if city == "Ulaanbaatar":
#         print(name)

#task 30 
# data = {
#     "a": 10,
#     "b": 20,
#     "c": 10,
#     "d": 30,
#     "e": 20
# }
# values_set = set(data.values())
# print(values_set)