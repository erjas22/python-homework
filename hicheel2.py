import tkinter as tk

app = tk.Tk()
app.title("My Weather App")
app.geometry("400x300")
app.configure(bg="lightblue")

title = tk.Label(
    app,
    text="WEATHER APP 🌤️",
    font=("Arial", 25, "bold"),
    bg="lightblue"
)
title.pack(pady=80)

app.mainloop()











