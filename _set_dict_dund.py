# #task 1
# user1 = {"Bat", "Sara", "Bold", "Anu"}
# user2 = {"Bold", "Anu", "Temuulen", "Naraa"}
# both = user1 & user2
# print(both)

# #task 2
# players = {"Bat", "Sara", "Bold", "Anu", "Naraa", "Temuulen"}
# played = {"Bat", "Bold", "Naraa"}
# print(players - played)

# #task 3
# team_a = {"Bat", "Bold", "Anu", "Sara"}
# team_b = {"Anu", "Sara", "Naraa", "Temuulen"}
# only_one = (team_a - team_b) | (team_b - team_a)
# print(only_one)

# #task 4
# known = {"Python", "HTML", "CSS"}
# required = {"Python", "JavaScript", "SQL"}
# missing = required - known
# for lang in sorted(missing):
#     print(lang)

# #task 5
# subjects = [
#     "Python",
#     "Math",
#     "Python",
#     "English",
#     "Math",
#     "Physics"
# ]
# unique = set(subjects)
# print("heden oor hicheel:", len(unique))
# print(unique)

# #task 6
# password = "programming123"
# letters = set()
# digits = set()
# for ch in password:
#     if ch.isalpha():
#         letters.add(ch)
#     elif ch.isdigit():
#         digits.add(ch)
# print(f"Letters: {len(letters)}")
# print(f"Digits: {len(digits)}")

# #task 7
# a = "computer"
# b = "science"
# chars = set(a) | set(b)
# print(len(chars))

# #task 8
# students = {
#     "Bat": 75,
#     "Sara": 92,
#     "Bold": 61,
#     "Anu": 88,
#     "Naraa": 54
# }
# for name, score in students.items():
#     if score >= 90:
#         print(f"{name} - Excellent")
#     elif score >= 60:
#         print(f"{name} - Pass")
#     else:
#         print(f"{name} - Fail")

# #task 9
# products = {
#     "apple": 3000,
#     "banana": 2500,
#     "milk": 4500,
#     "bread": 3500
# }
# name = "apple"
# too = 3
# if name in products:
#     print(f"Total: {products[name] * too}")
# else:
#     print("iim baraa bhgu")

# #task 10
# sales = {
#     "keyboard": 15,
#     "mouse": 23,
#     "monitor": 8,
#     "headset": 17
# }
# max_n = 0
# max_name = ""
# for name, count in sales.items():
#     if count > max_n:
#         max_n = count
#         max_name = name
# print(max_name, max_n)

# #task 11
# employees = {
#     "Bat": 1500000,
#     "Sara": 1800000,
#     "Bold": 1300000,
#     "Anu": 2100000
# }
# new_employees = {}
# for name, salary in employees.items():
#     if salary < 1500000:
#         new_employees[name] = salary + salary // 10
#     else:
#         new_employees[name] = salary
# print(new_employees)

# #task 12
# people = {
#     "Bat": 17,
#     "Sara": 21,
#     "Bold": 19,
#     "Anu": 16,
#     "Naraa": 25
# }
# for name, age in people.items():
#     if age >= 18:
#         print(name)

# #task 13
# scores = {
#     "Bat": 70,
#     "Sara": 85,
#     "Bold": 60,
#     "Anu": 95
# }
# for name in scores:
#     scores[name] = scores[name] + 5
#     if scores[name] > 100:
#         scores[name] = 100
#     print(f"{name} → {scores[name]}")

# #task 14
# products = {
#     "keyboard": 120000,
#     "mouse": 50000,
#     "monitor": 450000,
#     "headset": 80000
# }
# une = 100000
# for name, price in products.items():
#     if price > une:
#         print(name)

# #task 15
# students = {
#     "Bat": "Ulaanbaatar",
#     "Sara": "Darkhan",
#     "Bold": "Ulaanbaatar",
#     "Anu": "Erdenet",
#     "Naraa": "Darkhan",
#     "Temuulen": "Ulaanbaatar"
# }
# city = "Ulaanbaatar"
# result = set()
# for name, hot in students.items():
#     if hot == city:
#         result.add(name)
# print(result)

# #task 16
# games = {
#     "Bat": {"CS2", "Dota2"},
#     "Sara": {"Valorant", "CS2"},
#     "Bold": {"Dota2", "WoW"},
#     "Anu": {"CS2", "WoW"}
# }
# cs2_players = set()
# for name, game in games.items():
#     if "CS2" in game:
#         cs2_players.add(name)
# print(cs2_players)

# #task 17
# all_games = set()
# for game in games.values():
#     all_games.update(game)
# print(all_games)

# #task 18
# for name, game in games.items():
#     if "CS2" in game and "WoW" in game:
#         print(name)

# #task 19
# skills = {
#     "Bat": {"Python", "HTML", "CSS"},
#     "Sara": {"Python", "JavaScript"},
#     "Bold": {"HTML", "CSS", "JavaScript"},
#     "Anu": {"Python", "SQL", "JavaScript"}
# }
# for name, skill in skills.items():
#     if "Python" in skill and "JavaScript" in skill:
#         print(name)

# #task 20
# employees = {
#     "Bat": {"English", "Mongolian"},
#     "Sara": {"English", "Korean"},
#     "Bold": {"Mongolian", "Japanese"},
#     "Anu": {"English", "Japanese"}
# }
# for name, lang in employees.items():
#     if "English" in lang and "Korean" not in lang:
#         print(name)

# #task 21
# web_users = {"Bat", "Sara", "Bold", "Anu"}
# mobile_users = {"Sara", "Anu", "Naraa"}
# both = web_users & mobile_users
# print(both)
# print(f"Niit: {len(both)}")

# #task 22
# status = {
#     "Bat": "online",
#     "Sara": "offline",
#     "Bold": "online",
#     "Anu": "offline",
#     "Naraa": "online"
# }
# online = set()
# for name, s in status.items():
#     if s == "online":
#         online.add(name)
# print(online)
# name = "Bat"
# if name in online:
#     print(f"{name} online bna")
# else:
#     print(f"{name} online bish")

# #task 23
# courses = {
#     "Python": {"Bat", "Sara", "Bold"},
#     "JavaScript": {"Sara", "Anu", "Bold"},
#     "SQL": {"Bat", "Anu"}
# }
# name = "Anu"
# found = set()
# for course, students in courses.items():
#     if name in students:
#         found.add(course)
# if found:
#     print(found)
# else:
#     print("ali ch course-d burtgelgui")

# #task 24
# all_students = set()
# for students in courses.values():
#     all_students.update(students)

# counts = {}
# for name in all_students:
#     count = 0
#     for students in courses.values():
#         if name in students:
#             count += 1
#     counts[name] = count

# max_count = max(counts.values())
# for name in sorted(counts):
#     if counts[name] == max_count:
#         print(name, counts[name])