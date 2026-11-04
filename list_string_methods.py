#task1
# a = input("nere hel: ")
# print("Sainu", a)

#task 2
# a, b = map(int,input("too og: ").split())
# print(a + b)

#task 3
# a = float(input("baraani une og: "))
# print(a * 2)

#task 4
# a = input()
# print(type(a))
# number = int(a)
# print(type(number))

#task 5 
# a = "sain uu"
# print(len(a))

#task 6
# a = input("text: ")
# print(a[0])
# print(a[-1])

#task 7
# n = int(input("too og: "))
# for i in range(0,n):
#     i+=1
#     print(i)

#task 8
# a = list(map(int,input("3 too og:").split()))
# print(sum(a))

#task 9 
# a = list(map(int,input("too og: ").split()))
# print(min(a),max(a))

#task 10 
# a = list(map(int,input("toonuud og: ").split()))
# b = sum(a)
# c = len(a)
# print(round(b / c))

#task 11
# a = list(map(str,input("amitad og: ").split()))
# b = input("nemeh amitan: ")
# a.append(b)
# print(a)

#task 12
# a = list(map(str, input('amitan. og: ').split()))
# b = input("nemeh amitan: ")
# a.insert(1,b)
# print(a)

#task 13
# a = list(map(str, input('amitan. og: ').split()))
# b = input("hasah amitan: ")
# a.remove(b)
# print(a)

#task 14
# a = list(map(str,input("amitan og: ").split()))
# d = int(input("too og: "))
# b = a.pop(d)
# c = ",".join(a)
# print(b)
# print(c)

#task 15
# a = list(map(int,input("too og:").split()))
# a.sort()
# print(a)
# a.sort(reverse=True)
# print(a)

#task 16
# a = list(map(int,input("too og: ").split()))
# a.reverse()
# print(a)

#task 17
# x = "   hello   "
# print(x.rstrip())
# print(x.lstrip())

#task 18
# a = list(map(str,input("oguulber og: ").split()))
# print(len(a))

#task 19
# a = input("text og: ")
# b = input("tooloh useg: ")
# m = a.lower()
# j = b.lower()
# print(m.count(j))

#task 20
# a = input("txt: ")
# b = input("txt: ")
# print(a.find(b))

#task 21
# a = map(str,input("txt: ").split())
# c = 0
# for b in a:
#     if b.startswith("report") and b.endswith(".pdf"):
#         print(b)
#         c += 1
# if c == 0:
#     print("oldsongu")

#task 22
# a = input("txt: ")
# d = input("txt: ")
# c = input("txt: ")
# b = a.replace(d,c)
# print(b)

#task 23
# a = list(map(str,input("nernuud og: ").split()))
# b = input("ner: ")
# if b in a:
#     print("Yes")
# else:
#     print("No")

#task 24
# a = input("text: ")
# print(a[0],a[1],a[2])
# print(a[-3],a[-2],a[-1])

#task 25
# a = input("txt: ")
# b = a.lower()
# if b == b[::-1]:
#     print("yes")
# else:
#     print("No")

#task 26
# a = list(map(str, input("text og: ").split()))
# urt = a[0]
# for ug in a:
#     if len(ug) > len(urt):
#         urt = ug
# print(urt)

#task 27
# a =input("ner og: ")
# b = int(input("nas og: "))
# c = input("hot og: ")
# print(a, "/ Ireh jil", b+1, "/",c)

# #task 28
# a = input().lower().split()
# b = []
# for i in a:
#     if i not in b:
#         b.append(i)
# b.sort()
# print(" ".join(b))

#task 29
# a = map(int,input("too og: ").split())
# b = []
# for i in a:
#     if i not in b:
#         b.append(i)
#         b.sort()
# print(b[1])

#task 30
# a = int(input("heden suragch: "))
# names = []
# dunguud = []
# for i in range(a):
#     m = input("ner, dun; ").split()
#     name = m [0].rstrip(",")
#     dun = int(m[1])
#     dunguud.append(dun)
#     names.append(name)
#     dundaj = sum(dunguud) / len(dunguud)
#     maxscore = max(dunguud)
#     index = dunguud.index(maxscore)
# print(f"dundaj dun: {round(dundaj,2)}")
# print(f"hamgiin ondor: {names(index)}{maxscore}")
# print(f"ners: {", ".join(names)}")

