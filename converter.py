import tkinter as tk
import random
import time

rates = {
    "EUR": 1.0,
    "USD": 1.1,
    "JPY": 160.0,
    "SEK": 11.2
}

def spin_and_convert():
    try:
        amount = float(entry.get())
        
        # Check if Gamble-Mode is on
        if gamble_var.get():
            # "Glücksrad" Animation-Effekt (simuliert)
            for _ in range(10):
                fake_val = random.uniform(0.1, 500.0)
                result_label.config(text=f"🎲 Würfeln: {fake_val:.2f}", fg="orange")
                root.update()
                time.sleep(0.05)
            
            # Zufälliger Multiplikator zwischen 0.5 und 2.0
            multiplier = random.uniform(0.5, 2.0)
            result = amount * rates[var.get()] * multiplier
            result_label.config(text=f"🎰 Glücks-Resultat: {result:.2f}", fg="red")
        else:
            # Normaler Modus
            result = amount * rates[var.get()]
            result_label.config(text=f"Resultat: {result:.2f}", fg="black")
            
    except ValueError:
        result_label.config(text="Bitte Zahl eingeben", fg="black")

root = tk.Tk()
root.title("Casino Currency Converter 🎰")
root.geometry("500x650")
root.resizable(False, False)

# Fonts
title_font = ("Arial", 20, "bold")
label_font = ("Arial", 12)
button_font = ("Arial", 14, "bold")

# Title
tk.Label(root, text="Currency Converter", font=title_font).pack(pady=20)

# Entry
tk.Label(root, text="Betrag in Euro:", font=label_font).pack()
entry = tk.Entry(root, font=("Arial", 16), width=15, justify="center")
entry.pack(pady=10)

# Gamble Mode Checkbox
gamble_var = tk.BooleanVar()
tk.Checkbutton(root, text="🔥 GLÜCKSRAD-MODUS AKTIVIEREN 🔥", 
               variable=gamble_var, font=("Arial", 10, "bold"), fg="red").pack(pady=5)

# Currency selection
var = tk.StringVar(value="USD")
radio_frame = tk.LabelFrame(root, text=" Währung wählen ", padx=20, pady=10)
radio_frame.pack(pady=10)

for currency in rates:
    tk.Radiobutton(
        radio_frame,
        text=currency,
        variable=var,
        value=currency,
        font=label_font
    ).pack(anchor="w")

# Convert button
tk.Button(
    root,
    text="BERECHNEN / SPIN 🎲",
    command=spin_and_convert,
    font=button_font,
    bg="#4CAF50",
    fg="white",
    width=20,
    height=2
).pack(pady=25)

# Result
result_label = tk.Label(root, text="Resultat:", font=("Arial", 16, "bold"))
result_label.pack(pady=10)

root.mainloop()
