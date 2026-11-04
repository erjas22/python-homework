#task 1
# colors = tuple(map(str,input("ongo og: ").split()))
# print(colors)

#task 2
# amitan = tuple(map(str,input("amitan og: ").split()))
# print(f"{amitan[0]}\n{amitan[2]}\n{amitan[-1]}")

#task 3
# a = tuple(input("too og:"))
# print(type(a))

#task 4
# subjects = ("Математик", "Монгол хэл", "Англи хэл", "Python")
# print(f"{subjects[0]}\n{subjects[1]}\n{subjects[2]}\n{subjects[3]}")

#task 5
# numbers = tuple(input("too og: ").split())
# for i in numbers[0:3]:
#     print(i)

#task 6
# numbers = tuple(input("too og: ").split())
# print(numbers[-1], numbers[-2], numbers[-3])

# for i in range(len(numbers)):
#     print(numbers[i],end=" ")

#task 7
# fruits = tuple(input("fruit og: ").split())
# print(len(fruits))

#task 8 
# number = tuple(map(int,input("too og: ").split()))
# print(max(number))
# print(min(number))

#task 9
# score = tuple(map(int,input("score og: ").split()))
# print("niilber",sum(score))
# print("dundaj",sum(score)//len(score))

#task 10
# number = tuple(map(int, input("too og: ").split()))
# print(sorted(number))

#task 11
# number = tuple(map(int,input("too og: ").split()))
# print(number.count(10))

#task 12 
# fruit = tuple(map(str,input("fruit og: ").split()))
# print(fruit.index("jurj"))

#task  13
# animal = tuple(map(str,input("amitan og: ").split()))
# a = input()
# if a in animal:
#     print("bna")
# else:
#     print("bhgu")


#task 14
# student = tuple(map(str,input("ner nas angi og: ").split()))
# name, age, student_class = student
# print("Name: ",name, "\n","Age: ",age,"\n", "Class: ",student_class)

#task 15
# cordinate = tuple(map(int,input("x, y og: ").split()))
# x, y = cordinate
# print("x =",x,"\n","y =",y)

#task 16
# book = tuple(map(str,input("nom zohiolch huudas og: ").split()))
# nom, zohiolch,pages = book
# print("nom: ",nom,"\n","zohiolch: ",zohiolch,"\n","huudas: ",pages)

#task 17
# c = map(int,input("a b toog og:").split())
# a,b = c

# print("a =",b,"\n","b =",a)

#task 18
# number = tuple(map(int,input("toonud og: ").split()))
# a,*b = number
# print(f"ehni utga: {a}\n busad utga: {b}")
# print(f"Ehnii utga {number[0]}, {number[1:]}")

#task 19
# number = tuple(map(int,input("too og: ").split()))
# first, *middle, last = number
# print(f"Ehnii; {first} \n dundah: {middle}\n last; {last}")

#task 20
# student = tuple(map(str,input("nernii araas hicheeluud bich: ").split()))
# name, *subject = student
# print(f"Name: {name}\nHicheeluud: {subject}")

#task 21
# product = tuple(map(str,input("ner price quantity og: ").split()))
# name, price, quantity = product
# price = int(price)
# quantity = int(quantity)
# print(f"Baraa: {name}\nNegj une: {price}\nToo shirheg: {quantity}\nNiit une: {price * quantity}")

#task 22
# n = int(input("heden suragch bgan: "))
#student = []
# for i in range(n):
#     name, score = input("name score og: ").split()
#     score = int(score)
#     students.append((name, score))
# for name, score in students:
#     print(f"{name}: {score}")

#task 23
# n = int(input("heden suragch bgan: "))
# students = []
# for i in range(n):
#     name, score = input("name score og: ").split()
#     score = int(score)
#     students.append((name, score))
# for name, score in students:
#     if score > 80:
#         print(f"{name}: {score}")

#task 24
# colors = tuple(map(str,input("ongo og: ").split()))
# colors = list(colors)
# colors .append("shar")
# colors = tuple(colors)
# print(colors)