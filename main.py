
import tkinter as tk
from datetime import datetime

app = tk.Tk()
app.title("My Chat App")
app.geometry("1000x650")
app.configure(bg="#eef2ff")
app.minsize(750, 500)

# Colors
NAVY = "#14264b"
BLUE = "#2563eb"
LIGHT = "#f1f5ff"
WHITE = "#ffffff"
TEXT = "#172554"

# Sidebar
sidebar = tk.Frame(app, bg=NAVY, width=260)
sidebar.pack(side="left", fill="y")
sidebar.pack_propagate(False)

logo = tk.Label(
    sidebar, text="💬  My Chat",
    font=("Arial", 23, "bold"),
    bg=NAVY, fg=WHITE
)
logo.pack(pady=30)

profile = tk.Label(
    sidebar, text="👤  ChatUser\n🟢 Online",
    font=("Arial", 15, "bold"),
    bg=NAVY, fg=WHITE,
    justify="left"
)
profile.pack(pady=20)

tk.Label(
    sidebar, text="CHATS",
    font=("Arial", 11, "bold"),
    bg=NAVY, fg="#93c5fd"
).pack(anchor="w", padx=20, pady=15)

def choose_chat(name):
    chat_title.config(text="💬  " + name)
    chat_box.config(state="normal")
    chat_box.delete("1.0", tk.END)
    chat_box.config(state="disabled")

for name in ["Friend", "Python Team", "Family"]:
    tk.Button(
        sidebar,
        text="👤  " + name,
        font=("Arial", 14),
        bg="#203b70",
        fg=WHITE,
        activebackground=BLUE,
        activeforeground=WHITE,
        relief="flat",
        anchor="w",
        padx=15,
        pady=14,
        command=lambda n=name: choose_chat(n)
    ).pack(fill="x", padx=10, pady=5)

# Main chat area
main = tk.Frame(app, bg=LIGHT)
main.pack(side="right", fill="both", expand=True)

header = tk.Frame(main, bg=WHITE, height=75)
header.pack(fill="x")
header.pack_propagate(False)

chat_title = tk.Label(
    header,
    text="💬  Friend",
    font=("Arial", 20, "bold"),
    bg=WHITE,
    fg=TEXT
)
chat_title.pack(side="left", padx=25, pady=20)

chat_box = tk.Text(
    main,
    font=("Arial", 13),
    bg=LIGHT,
    fg=TEXT,
    relief="flat",
    wrap="word",
    padx=20,
    pady=20,
    state="disabled"
)
chat_box.pack(fill="both", expand=True, padx=10, pady=10)

chat_box.tag_configure(
    "mine",
    foreground=BLUE,
    justify="right",
    spacing1=8,
    spacing3=12
)

chat_box.tag_configure(
    "other",
    foreground=TEXT,
    justify="left",
    spacing1=8,
    spacing3=12
)

# Send message
def send_message(event=None):
    message = entry.get().strip()

    if message:
        time = datetime.now().strftime("%H:%M")

        chat_box.config(state="normal")
        chat_box.insert(
            tk.END,
            f"You  •  {time}\n{message}\n\n",
            "mine"
        )
        chat_box.config(state="disabled")
        chat_box.see(tk.END)

        entry.delete(0, tk.END)

def clear_chat():
    chat_box.config(state="normal")
    chat_box.delete("1.0", tk.END)
    chat_box.config(state="disabled")

# Bottom input area
bottom = tk.Frame(main, bg=WHITE, padx=15, pady=15)
bottom.pack(fill="x")

entry = tk.Entry(
    bottom,
    font=("Arial", 14),
    bg=LIGHT,
    fg=TEXT,
    relief="flat"
)
entry.pack(side="left", fill="x", expand=True, ipady=13, padx=10)

entry.insert(0, "Message...")

entry.bind("<Return>", send_message)

send_btn = tk.Button(
    bottom,
    text="➤ SEND",
    font=("Arial", 12, "bold"),
    bg=BLUE,
    fg=WHITE,
    relief="flat",
    padx=20,
    pady=10,
    command=send_message
)
send_btn.pack(side="left", padx=5)

clear_btn = tk.Button(
    bottom,
    text="Clear",
    bg="#fee2e2",
    fg="#dc2626",
    relief="flat",
    padx=12,
    pady=10,
    command=clear_chat
)
clear_btn.pack(side="left")

app.mainloop()
