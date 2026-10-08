import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Voice Changer Prototype)")
root.geometry("600x400")

frame = ttk.Frame(root, padding=20)
frame.pack(fill="both", expand=True)

title = ttk.Label(
  frame,
  text="Voice Changer Prototype",
  font=("Segoe UI", 20, "bold")
)
title.pack(pady=10)

root.mainloop()