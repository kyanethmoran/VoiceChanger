import tkinter as tk
from tkinter import ttk, messagebox
from pedalboard.io import AudioStream
import threading
import queue

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

output_dropdown.set("Select your output")

#start and stop buttons
audio_thread = None
stop_event = threading.Event()
audio_messages = queue.Queue()
closing = False

def run_audio(microphone, output):
  try:
      with AudioStream(microphone, output):
        audio_messages.put("Microphone is live!")
        stop_event.wait()
  except Exception as error:
     audio_messages.put(f"Audio error: {error}")

def start_audio():
   global audio_thread

   if audio_thread is not None and audio_thread.is_alive():
      return

   microphone = mic_dropdown.get()
   output = output_dropdown.get()

   if microphone not in microphones or output not in outputs:
      messagebox.showwarning(
         "Choose devices",
         "Slect a microphone and an audio output first."
      )
      return

   stop_event.clear()
   status_label.config(text="Starting microphone...")

   audio_thread = threading.Thread(
      target = run_audio,
      args=(microphone, output),
      daemon=True
   )
   audio_thread.start()

def stop_audio():
   stop_event.set()
   status_label.config(text="Microphone stopped.")

def check_audio_messages():
  while not audio_messages.empty():
    message = audio_messages.get_nowait()
    status_label.config(text=message)

  if closing:
     if audio_thread is None or not audio_thread.is_alive():
        root.destroy()
        return

  root.after(100, check_audio_messages)

def close_app():
   global closing
   closing= True
   stop_audio()   

# buttons
button_frame = ttk.Frame(frame)
button_frame.pack(pady=15)

start_button = ttk.Button(
   button_frame,
   text="Start",
   command = start_audio
)
start_button.pack(side="left",padx=5)

stop_button = ttk.Button(
   button_frame,
   text="Stop",
   command=stop_audio
)
stop_button.pack(side="left",padx=5)

status_label = ttk.Label(frame, text="Microphone stopped.")
status_label.pack()

root.protocol("WM_DELETE_WINDOW", close_app)
root.after(100, check_audio_messages)

root.mainloop()