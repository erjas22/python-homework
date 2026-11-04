#task 1
# class Phone:
#     def __init__(self, brand, battery):
#         self.brand = brand
#         self.battery = battery

#     def use_phone(self):
#         self.battery -= 10

#     def charge(self):
#         self.battery += 20

#     def show_battery(self):
#         print(f"Tseneg:{self.battery}%")

# phone1 = Phone("iPhone", 80)
# phone1.use_phone()
# phone1.show_battery()
# phone1.charge()
# phone1.show_battery()


# #task 2
# class Product:
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity

#     def sell(self, amount):
#         if amount > self.quantity:
#             print("Baraa hureltsehgui")
#         else:
#             self.quantity -= amount
#             print("Uldegdel:", self.quantity)

#     def show_total(self):
#         print("Niit une:", self.price * self.quantity)

# product1 = Product("Mouse", 30000, 10)
# product1.sell(3)
# product1.show_total()


# #task 3
# class Athlete:
#     def __init__(self, name, points):
#         self.name = name
#         self.points = points

#     def add_points(self, points):
#         self.points += points

#     def lose_points(self, points):
#         self.points -= points

#     def show_points(self):
#         print("Onoo:", self.points)

# athlete1 = Athlete("Bat", 20)
# athlete1.add_points(15)
# athlete1.lose_points(5)
# athlete1.show_points()


# #task 4
# class Movie:
#     def __init__(self, title, rating, views):
#         self.title = title
#         self.rating = rating
#         self.views = views

#     def add_view(self):
#         self.views += 1

#     def update_rating(self, new_rating):
#         self.rating = new_rating

#     def show_info(self):
#         print(f"Kino: {self.title}\nUnelgee: {self.rating}\nUzsen: {self.views}")

# movie1 = Movie("Inception", 8.8, 100)
# movie2 = Movie("Interstellar", 8.6, 250)
# movie1.add_view()
# movie2.update_rating(9.0)
# movie1.show_info()
# movie2.show_info()


# #task 5
# class GameCharacter:
#     def __init__(self, name, health, damage):
#         self.name = name
#         self.health = health
#         self.damage = damage

#     def attack(self, enemy):
#         enemy.health -= self.damage
#         if enemy.health < 0:
#             enemy.health = 0

#     def show_health(self):
#         print(f"{self.name}-iin ami: {self.health}")

# player1 = GameCharacter("Knight", 100, 20)
# player2 = GameCharacter("Goblin", 60, 10)
# player1.attack(player2)
# player2.show_health()


# #task 6
# class Wallet:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance

#     def add_money(self, amount):
#         self.balance += amount

#     def pay(self, amount):
#         if amount > self.balance:
#             print("Mungu hureltsehgui")
#         else:
#             self.balance -= amount

#     def show_balance(self):
#         print(f"{self.owner} - uldegdel: {self.balance}")

# wallet1 = Wallet("Bat", 50000)
# wallet1.add_money(20000)
# wallet1.pay(30000)
# wallet1.show_balance()
# wallet1.pay(100000)
# wallet1.show_balance()


# #task 7
# class LibraryBook:
#     def __init__(self, title, available):
#         self.title = title
#         self.available = available

#     def borrow(self):
#         if self.available:
#             self.available = False
#             print("Nomiig zeellee")
#         else:
#             print("Nom al hediin zeelegdsen baina")

#     def return_book(self):
#         self.available = True
#         print("Nomiig butsaalaa")

# book1 = LibraryBook("Python", True)
# book1.borrow()
# book1.borrow()
# book1.return_book()


# #task 8
# class Exam:
#     def __init__(self, student_name, score, max_score):
#         self.student_name = student_name
#         self.score = score
#         self.max_score = max_score

#     def get_percentage(self):
#         return self.score / self.max_score * 100

#     def check_result(self):
#         p = self.get_percentage()
#         if p >= 90:
#             print(self.student_name, ": Mash sain")
#         elif p >= 80:
#             print(self.student_name, ": Sain")
#         elif p >= 60:
#             print(self.student_name, ": Tentssen")
#         else:
#             print(self.student_name, ": Tentseegui")

# exam1 = Exam("Bat", 45, 50)
# exam2 = Exam("Saraa", 25, 50)
# exam1.check_result()
# exam2.check_result()


# #task 9
# class Employee:
#     def __init__(self, name, salary, bonus):
#         self.name = name
#         self.salary = salary
#         self.bonus = bonus

#     def add_bonus(self, amount):
#         self.bonus += amount

#     def get_total_salary(self):
#         print("Niit tsalin:", self.salary + self.bonus)

# employee1 = Employee("Bat", 2000000, 100000)
# employee1.add_bonus(50000)
# employee1.get_total_salary()


# #task 10
# class CartItem:
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity

#     def increase_quantity(self, amount):
#         self.quantity += amount

#     def decrease_quantity(self, amount):
#         if amount > self.quantity:
#             print("Tiim olon baraa sagsand alga")
#         else:
#             self.quantity -= amount

#     def get_total_price(self):
#         print(f"{self.name}: {self.price * self.quantity}")

# item1 = CartItem("Talh", 3000, 2)
# item2 = CartItem("Suu", 2500, 3)
# item3 = CartItem("Ondog", 500, 10)
# item1.increase_quantity(1)
# item3.decrease_quantity(4)

# items = [item1, item2, item3]
# for i in items:
#     i.get_total_price()


# #task 11
# class Computer:
#     def __init__(self, brand, ram, storage):
#         self.brand = brand
#         self.ram = ram
#         self.storage = storage

#     def upgrade_ram(self, amount):
#         self.ram += amount

#     def upgrade_storage(self, amount):
#         self.storage += amount

#     def show_info(self):
#         print(f"Uildverlegch: {self.brand}\nRAM: {self.ram} GB\nBagtaamj: {self.storage} GB")

# pc1 = Computer("Lenovo", 8, 256)
# pc1.upgrade_ram(8)
# pc1.upgrade_storage(256)
# pc1.show_info()


# #task 12
# class Account:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance += amount

# class SavingsAccount(Account):
#     def __init__(self, owner, balance, interest_rate):
#         super().__init__(owner, balance)
#         self.interest_rate = interest_rate

#     def add_interest(self):
#         self.balance += self.balance * self.interest_rate / 100
#         print("Huu nemsnii daraah uldegdel:", self.balance)

# account1 = SavingsAccount("Bat", 100000, 10)
# account1.add_interest()


# #task 13
# class Device:
#     def __init__(self, brand, price):
#         self.brand = brand
#         self.price = price

# class Laptop(Device):
#     def __init__(self, brand, price, ram):
#         super().__init__(brand, price)
#         self.ram = ram

#     def show_info(self):
#         print(f"Uildverlegch: {self.brand}\nUne: {self.price}\nRAM: {self.ram} GB")

# laptop1 = Laptop("Apple", 4500000, 16)
# laptop1.show_info()


# #task 14
# class User:
#     def __init__(self, username, email):
#         self.username = username
#         self.email = email

# class Admin(User):
#     def __init__(self, username, email, permission):
#         super().__init__(username, email)
#         self.permission = permission

#     def show_info(self):
#         print(f"Hereglegchiin ner: {self.username}\nImeil: {self.email}\nErh: {self.permission}")

# admin1 = Admin("saraa", "saraa@example.com", "Full Access")
# admin1.show_info()


# #task 15
# class Character:
#     def __init__(self, name, health):
#         self.name = name
#         self.health = health

# class Mage(Character):
#     def __init__(self, name, health, mana):
#         super().__init__(name, health)
#         self.mana = mana

#     def cast_spell(self):
#         if self.mana < 10:
#             print("Mana hureltsehgui")
#         else:
#             self.mana -= 10

#     def show_info(self):
#         print(f"Ner: {self.name}\nAmi: {self.health}\nMana: {self.mana}")

# mage1 = Mage("Gandalf", 100, 25)
# mage1.cast_spell()
# mage1.cast_spell()
# mage1.cast_spell()
# mage1.show_info()