# import tkinter as tk
# from tkinter import messagebox

# # Login шалгах функц
# def login():
#     username = username_entry.get()
#     password = password_entry.get()

#     if username == "admin" and password == "1234":
#         messagebox.showinfo("Login", "Амжилттай нэвтэрлээ! 🎉")
#     else:
#         messagebox.showerror("Login", "Username эсвэл password буруу!")

# # Үндсэн цонх
# app = tk.Tk()
# app.title("Login App")
# app.geometry("1000x800")
# app.resizable(False, False)

# # Гарчиг
# title = tk.Label(
#     app,
#     text="Login",
#     font=("Arial", 24, "bold")
# )
# title.pack(pady=30)

# # Username
# username_label = tk.Label(app, text="Username")
# username_label.pack()

# username_entry = tk.Entry(app, width=30)
# username_entry.pack(pady=5)

# # Password
# password_label = tk.Label(app, text="Password")
# password_label.pack()

# password_entry = tk.Entry(app, width=30, show="*")
# password_entry.pack(pady=5)

# # Login button
# login_button = tk.Button(
#     app,
#     text="Login",
#     width=15,
#     command=login
# )
# login_button.pack(pady=20)

# app.mainloop()

















# import tkinter as tk
# from tkinter import messagebox
# import sqlite3
# import hashlib

# # =========================
# # DATABASE
# # =========================

# db = sqlite3.connect("users.db")
# cursor = db.cursor()

# cursor.execute("""
# CREATE TABLE IF NOT EXISTS users (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     username TEXT UNIQUE NOT NULL,
#     password TEXT NOT NULL
# )
# """)

# db.commit()


# def hash_password(password):
#     return hashlib.sha256(password.encode()).hexdigest()


# # =========================
# # MAIN WINDOW
# # =========================

# app = tk.Tk()
# app.title("My Login App")
# app.geometry("450x400")
# app.resizable(False, False)


# # =========================
# # CLEAR SCREEN
# # =========================

# def clear_screen():
#     for widget in app.winfo_children():
#         widget.destroy()


# # =========================
# # HOME PAGE
# # =========================

# def home_page(username):
#     clear_screen()

#     tk.Label(
#         app,
#         text="Welcome! 🎉",
#         font=("Arial", 26, "bold")
#     ).pack(pady=60)

#     tk.Label(
#         app,
#         text=f"Hello, {username}!",
#         font=("Arial", 18)
#     ).pack(pady=10)

#     tk.Button(
#         app,
#         text="Logout",
#         width=15,
#         command=login_page
#     ).pack(pady=40)


# # =========================
# # LOGIN
# # =========================

# def login():
#     username = username_entry.get()
#     password = password_entry.get()

#     if username == "" or password == "":
#         messagebox.showwarning(
#             "Warning",
#             "Бүх хэсгийг бөглөнө үү!"
#         )
#         return

#     hashed = hash_password(password)

#     cursor.execute(
#         "SELECT * FROM users WHERE username=? AND password=?",
#         (username, hashed)
#     )

#     user = cursor.fetchone()

#     if user:
#         home_page(username)
#     else:
#         messagebox.showerror(
#             "Error",
#             "Username эсвэл password буруу!"
#         )


# def login_page():
#     clear_screen()

#     tk.Label(
#         app,
#         text="LOGIN",
#         font=("Arial", 28, "bold")
#     ).pack(pady=30)

#     tk.Label(
#         app,
#         text="Username"
#     ).pack()

#     global username_entry
#     username_entry = tk.Entry(app, width=30)
#     username_entry.pack(pady=5)

#     tk.Label(
#         app,
#         text="Password"
#     ).pack()

#     global password_entry
#     password_entry = tk.Entry(
#         app,
#         width=30,
#         show="*"
#     )
#     password_entry.pack(pady=5)

#     tk.Button(
#         app,
#         text="Login",
#         width=20,
#         command=login
#     ).pack(pady=20)

#     tk.Button(
#         app,
#         text="Create Account",
#         command=register_page
#     ).pack()


# # =========================
# # REGISTER
# # =========================

# def register():
#     username = reg_username.get()
#     password = reg_password.get()
#     confirm = reg_confirm.get()

#     if username == "" or password == "":
#         messagebox.showwarning(
#             "Warning",
#             "Бүх хэсгийг бөглөнө үү!"
#         )
#         return

#     if password != confirm:
#         messagebox.showerror(
#             "Error",
#             "Password таарахгүй байна!"
#         )
#         return

#     try:
#         hashed = hash_password(password)

#         cursor.execute(
#             "INSERT INTO users (username, password) VALUES (?, ?)",
#             (username, hashed)
#         )

#         db.commit()

#         messagebox.showinfo(
#             "Success",
#             "Account амжилттай үүслээ!"
#         )

#         login_page()

#     except sqlite3.IntegrityError:
#         messagebox.showerror(
#             "Error",
#             "Энэ username аль хэдийн байна!"
#         )


# def register_page():
#     clear_screen()

#     tk.Label(
#         app,
#         text="REGISTER",
#         font=("Arial", 28, "bold")
#     ).pack(pady=25)

#     tk.Label(
#         app,
#         text="Username"
#     ).pack()

#     global reg_username
#     reg_username = tk.Entry(app, width=30)
#     reg_username.pack(pady=5)

#     tk.Label(
#         app,
#         text="Password"
#     ).pack()

#     global reg_password
#     reg_password = tk.Entry(
#         app,
#         width=30,
#         show="*"
#     )
#     reg_password.pack(pady=5)

#     tk.Label(
#         app,
#         text="Confirm Password"
#     ).pack()

#     global reg_confirm
#     reg_confirm = tk.Entry(
#         app,
#         width=30,
#         show="*"
#     )
#     reg_confirm.pack(pady=5)

#     tk.Button(
#         app,
#         text="Register",
#         width=20,
#         command=register
#     ).pack(pady=20)

#     tk.Button(
#         app,
#         text="Back to Login",
#         command=login_page
#     ).pack()


# # =========================
# # START APP
# # =========================

# login_page()

# app.mainloop()
# Илгээлээ




























# import tkinter as tk
# import random

# # Window
# WIDTH = 600
# HEIGHT = 400
# SIZE = 20

# score = 0
# direction = "Right"
# game_over = False

# snake = [(100, 100), (80, 100), (60, 100)]

# food = (
#     random.randrange(0, WIDTH, SIZE),
#     random.randrange(0, HEIGHT, SIZE)
# )

# # Create window
# root = tk.Tk()
# root.title("🐍 Snake Game")
# root.resizable(False, False)

# score_label = tk.Label(
#     root,
#     text="Score: 0",
#     font=("Arial", 16)
# )
# score_label.pack()

# canvas = tk.Canvas(
#     root,
#     width=WIDTH,
#     height=HEIGHT,
#     bg="black"
# )
# canvas.pack()


# def change_direction(event):
#     global direction

#     if event.keysym == "Up" and direction != "Down":
#         direction = "Up"

#     elif event.keysym == "Down" and direction != "Up":
#         direction = "Down"

#     elif event.keysym == "Left" and direction != "Right":
#         direction = "Left"

#     elif event.keysym == "Right" and direction != "Left":
#         direction = "Right"


# def create_food():
#     global food

#     while True:
#         new_food = (
#             random.randrange(0, WIDTH, SIZE),
#             random.randrange(0, HEIGHT, SIZE)
#         )

#         if new_food not in snake:
#             food = new_food
#             break


# def draw():
#     canvas.delete("all")

#     # Food
#     x, y = food
#     canvas.create_oval(
#         x, y,
#         x + SIZE,
#         y + SIZE,
#         fill="red"
#     )

#     # Snake
#     for i, (x, y) in enumerate(snake):
#         canvas.create_rectangle(
#             x, y,
#             x + SIZE,
#             y + SIZE,
#             fill="lime"
#         )


# def game_loop():
#     global score, game_over

#     if game_over:
#         return

#     head_x, head_y = snake[0]

#     if direction == "Up":
#         head_y -= SIZE
#     elif direction == "Down":
#         head_y += SIZE
#     elif direction == "Left":
#         head_x -= SIZE
#     elif direction == "Right":
#         head_x += SIZE

#     new_head = (head_x, head_y)

#     # Wall collision
#     if (
#         head_x < 0 or
#         head_x >= WIDTH or
#         head_y < 0 or
#         head_y >= HEIGHT
#     ):
#         end_game()
#         return

#     # Body collision
#     if new_head in snake:
#         end_game()
#         return

#     snake.insert(0, new_head)

#     # Eat food
#     if new_head == food:
#         score += 1
#         score_label.config(text=f"Score: {score}")
#         create_food()
#     else:
#         snake.pop()

#     draw()

#     root.after(100, game_loop)


# def end_game():
#     global game_over

#     game_over = True

#     canvas.create_text(
#         WIDTH // 2,
#         HEIGHT // 2,
#         text=f"GAME OVER\nScore: {score}",
#         fill="white",
#         font=("Arial", 30, "bold")
#     )


# root.bind("<KeyPress>", change_direction)

# draw()
# game_loop()

# root.mainloop()



















import cv2
import face_recognition
import os
import numpy as np

KNOWN_DIR = "known_faces"

known_encodings = []
known_names = []

# Бүртгэлтэй хүмүүсийн нүүрийг унших
for filename in os.listdir(KNOWN_DIR):
    if filename.lower().endswith((".jpg", ".jpeg", ".png")):
        path = os.path.join(KNOWN_DIR, filename)

        image = face_recognition.load_image_file(path)
        encodings = face_recognition.face_encodings(image)

        if len(encodings) == 0:
            print(f"Нүүр олдсонгүй: {filename}")
            continue

        known_encodings.append(encodings[0])

        # Файлын нэрийг хүний нэр болгоно
        name = os.path.splitext(filename)[0]
        known_names.append(name)

print("Бүртгэлтэй хүмүүс:", known_names)

# Webcam нээх
camera = cv2.VideoCapture(0)

while True:
    ret, frame = camera.read()

    if not ret:
        print("Камер нээгдсэнгүй.")
        break

    # OpenCV BGR -> RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Нүүрнүүдийг олох
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(
        rgb_frame,
        face_locations
    )

    for face_encoding, face_location in zip(
        face_encodings,
        face_locations
    ):
        name = "Unknown"
        access = False

        # Бүртгэлтэй нүүрнүүдтэй харьцуулах
        if known_encodings:
            matches = face_recognition.compare_faces(
                known_encodings,
                face_encoding,
                tolerance=0.5
            )

            distances = face_recognition.face_distance(
                known_encodings,
                face_encoding
            )

            best_match = np.argmin(distances)

            if matches[best_match]:
                name = known_names[best_match]
                access = True

        # Дүрсэн дээр дөрвөлжин зурах
        top, right, bottom, left = face_location

        color = (0, 255, 0) if access else (0, 0, 255)

        cv2.rectangle(
            frame,
            (left, top),
            (right, bottom),
            color,
            2
        )

        # Нэр / эрхийн мэдээлэл
        text = f"{name} - " + (
            "ACCESS GRANTED" if access else "ACCESS DENIED"
        )

        cv2.putText(
            frame,
            text,
            (left, bottom + 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            color,
            2
        )

    cv2.imshow("Face Login System", frame)

    # Q дарвал гарах
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()

