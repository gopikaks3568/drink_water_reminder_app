import tkinter as tk
from plyer import notification
import threading
import time
import random

# some water facts
water_facts = [
    "Your body is about 60% water.",
    "Drinking water can improve brain function.",
    "Water helps regulate your body temperature.",
    "Dehydration can cause fatigue and headaches.",
    "Drinking water before meals can aid digestion."
]


reminder_interval = 60
glasses_drank = 0
running = True

def remind():
    global running
    while running:
        time.sleep(reminder_interval * 60)
        notification.notify(
            title="💧 Drink Water!",
            message=random.choice(water_facts),
            timeout=10
        )
        update_fact()

def update_fact():
    fact_label.config(text=random.choice(water_facts))

def set_interval():
    global reminder_interval
    try:
        mins = int(interval_entry.get())
        if mins > 0:
            reminder_interval = mins
            status_label.config(text=f"Reminder set for every {mins} minutes ✅")
        else:
            status_label.config(text="Please enter a valid number ❌")
    except ValueError:
        status_label.config(text="Please enter a number ❌")

def drank_water():
    global glasses_drank
    glasses_drank += 1
    counter_label.config(text=f"Glasses Drank: {glasses_drank}")


root = tk.Tk()
root.title("Water Reminder App")
root.geometry("400x300")

tk.Label(root, text="Set Reminder Interval (minutes):").pack(pady=5)
interval_entry = tk.Entry(root)
interval_entry.pack(pady=5)

set_btn = tk.Button(root, text="Set Timer", command=set_interval)
set_btn.pack(pady=5)

status_label = tk.Label(root, text="Default: 60 minutes", fg="blue")
status_label.pack(pady=5)

counter_label = tk.Label(root, text="Glasses Drank: 0", font=("Arial", 12))
counter_label.pack(pady=5)

drink_btn = tk.Button(root, text="I Drank Water 💧", command=drank_water)
drink_btn.pack(pady=5)

fact_label = tk.Label(root, text=random.choice(water_facts), wraplength=300, justify="center")
fact_label.pack(pady=10)

# Start a reminder thread in the background
threading.Thread(target=remind, daemon=True).start()

root.mainloop()
