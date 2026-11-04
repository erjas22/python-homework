#task1

# a, b, c = map(int, input().split())

# p = a + b + c

# print(p)

#task2

# a, b = map(int, input().split())
# print(a + b)

#task3 

# a = int(input())

# V = a ** 3
# S = 6 * a ** 2

# print(V, S)

# #task4

# a, b = map(int, input().split())

# S = a * b
# P = 2 * (a + b)

# print(S, P)

# #task5

# x = int(input())
# y = 3 * x - 5
# print(y)

# #task6

# x = int(input())
# y = 4 * x**2 - 3 * x + 5
# print(y)

#task7 

n = int(input())
print(n % 10)

#task8 

n = int(input())
print(n // 10 % 10)

#task9

n = int(input())

a = n // 10
b = n % 10

print(a * b)

#task10

n = int(input())

a = n // 100
b = (n // 10) % 10
c = n % 10

print(a + b + c)

#task11

n = int(input())

minute = n // 60
second = n % 60

print(minute, second)

#task12

n = int(input())

hour = n // 3600
minute = (n % 3600) // 60
second = n % 60

print(hour, minute, second)

#task13

m, s = map(int, input().split())

total = m * 60 + s

print(total)

#task14

h, m, s = map(int, input().split())

total = h * 3600 + m * 60 + s

print(total)

#task15

n = int(input())

day = n // 24
hour = n % 24

print(day, hour)

#task16

day, hour = map(int, input().split())

total = day * 24 + hour

print(total)

#task17

n = int(input())

year = n // 12
month = n % 12

print(year, month)

#task18

year, month = map(int, input().split())

total = year * 12 + month

print(total)

#task19

a, b = map(int, input().split())
print(max(a, b))

#task20

a, b = map(int, input().split())
print(min(a, b))

#task21

a, b, c = map(int, input().split())
print(max(a, b, c))

#task22

a, b, c, d = map(int, input().split())
print(min(a, b, c, d))

#task23

a, b, c, d = map(int, input().split())
print(sum(x for x in [a, b, c, d] if x > 80))

#task24

a, b, c, d = map(int, input().split())
p = 1

for x in [a, b, c, d]:
    if x < 5:
        p *= x

print(p)

#task25

a, b, c = map(int, input().split())
print(sum(x for x in [a, b, c] if x % 2 == 0))

#task26

a, b, c = map(int, input().split())
p = 1

for x in [a, b, c]:
    if x % 2 != 0:
        p *= x

print(p)

#task27

a, b, c = map(int, input().split())
print([a, b, c].count(5))

#task28

a, b, c, d = map(int, input().split())
print(sum(x % 3 == 0 for x in [a, b, c, d]))

#task29

a, b, c, d = map(int, input().split())
print(sum(x for x in [a, b, c, d] if x % 11 != 0))

#task30

n = int(input())
print("YES" if n > 10 else "NO")

#task31

n = int(input())
print("YES" if n < 5 else "NO")

#task32

for i in range(3):
    n = int(input())
    print("YES" if n % 2 == 0 else "NO")

#task33

print("IOI")

#task34

for i in range(3):
    print("IOI")

#task34

n = int(input())

for i in range(n):
    print("IOI")

#task35

n = int(input())
s = 0

for i in range(1, n + 1):
    s += i

print(s)

#task36

n = int(input())
f = 1

for i in range(1, n + 1):
    f *= i

print(f)

#task37

n = int(input())
s = 0

for i in range(n):
    s += 100

print(s)

#task38

a, n = map(int, input().split())
s = 0

for i in range(n):
    s += a

print(s)

#task39

n = int(input())
print(2 ** n)

#task40

