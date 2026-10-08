import tkinter as tk
from tkinter import ttk
from pedalboard.io import AudioStream

#title and appbox
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

# input
mic_label = ttk.Label(frame, text="Choose your microphone:")
mic_label.pack(anchor="w", pady=(15,5))

microphones = AudioStream.input_device_names

mic_dropdown = ttk.Combobox(
  frame,
  values=microphones,
  state="readonly",
  width=65
)
mic_dropdown.pack(fill="x")

# if microphones:
#   mic_dropdown.current(0)
mic_dropdown.set("Select your input")

#output
output_label = ttk.Label(frame, text="Choose your audio output:")
output_label.pack(anchor="w", pady=(15,5))

outputs = AudioStream.output_device_names

output_dropdown = ttk.Combobox(
  frame,
  values=outputs,
  state="readonly",
  width=65
)

output_dropdown.pack(fill="x")

# if outputs:
#   output_dropdown.current(0)
output_dropdown.set("Select your output")

root.mainloop()