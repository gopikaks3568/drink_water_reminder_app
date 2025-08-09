import tkinter as tk
from plyer import notification
import threading
import time


def remind():
    while True:
        time.sleep(60*60)
        notification.notify(
            title="💧 Drink Water!",
            message="Time to hydrate yourself 🌊",
            timeout=10
        )


root = tk.Tk()
root.title("Water Reminder App")
root.geometry("300x200")

label = tk.Label(root, text="Water Reminder is Running!", font=("Arial", 12))
label.pack(pady=50)


threading.Thread(target=remind, daemon=True).start()

# Run the app
root.mainloop()
