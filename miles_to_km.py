from tkinter import *

def miles_to_km():
    try:
        miles = float(miles_input.get())
        km = round(miles * 1.60934, 3)
        kilometer_result_label.config(text=f"{km} km")
    except ValueError:
        kilometer_result_label.config(text="Invalid input")

# Set up window
window = Tk()
window.title("Miles to Kilometers Converter")
window.config(padx=40, pady=30, bg="#f0f8ff")

# Input field
miles_input = Entry(width=10, font=("Arial", 14))
miles_input.grid(column=1, row=0, padx=10, pady=10)

# Miles Label
miles_label = Label(text="Miles", font=("Arial", 14), bg="#f0f8ff")
miles_label.grid(column=2, row=0, padx=10)

# is equal to Label
is_equal_label = Label(text="is equal to", font=("Arial", 14), bg="#f0f8ff")
is_equal_label.grid(column=0, row=1, padx=10)

# Kilometer Result Label
kilometer_result_label = Label(text="0 km", font=("Arial", 14, "bold"), bg="#f0f8ff", fg="#007acc")
kilometer_result_label.grid(column=1, row=1, padx=10)

# Calculate Button
calculate_button = Button(text="Convert", font=("Arial", 12, "bold"), command=miles_to_km, bg="#007acc", fg="white", padx=10, pady=5)
calculate_button.grid(column=1, row=2, pady=20)

# Run the GUI
window.mainloop()
