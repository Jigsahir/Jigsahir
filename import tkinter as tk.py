import tkinter as tk
from tkinter import ttk

def validate_numeric_input(value, action):
    if action == '1':  # Insert action
        try:
            float(value)
            return True
        except ValueError:
            return False
    return True

def update_month_options(event):
    time_period = time_entry.get()
    try:
        total_months = int(float(time_period) * 12)
        month_options = ["All"] + [str(i) for i in range(1, total_months + 1)]
        month_combobox.config(values=month_options)
        month_combobox.set("All")
    except ValueError:
        # Handle non-numeric or invalid input
        month_combobox.config(values=["All"])
        month_combobox.set("All")

def calculate_monthly_interest(principle, rate, time):
    monthly_interest = []
    total_amount = principle
    total_interest = 0

    for month in range(1, int(time * 12) + 1):
        interest = total_amount * rate / 12 / 100
        total_interest += interest
        total_amount += interest
        monthly_interest.append((month, interest, total_interest, total_amount))

    return monthly_interest, total_interest

def calculate_button_click():
    principle_amount = float(principle_entry.get())
    interest_rate = float(rate_entry.get())
    time_period = float(time_entry.get())
    selected_month = month_combobox.get()

    monthly_data, total_interest = calculate_monthly_interest(principle_amount, interest_rate, time_period)

    # Clear the existing content in the Text widget
    result_text.config(state=tk.NORMAL)  # Enable the widget to modify the content
    result_text.delete(1.0, tk.END)

    # Displaying monthly interest, total interest, and total amount for the selected month
    for month, interest, total, total_amount in monthly_data:
        if selected_month == "All" or selected_month == str(month):
            result_text.insert(tk.END, f"Month {month}: Interest = ₹ {interest:.3f}, Total Interest = ₹ {total:.3f}, Total Amount = ₹ {total_amount:.3f}\n")
            result_text.insert(tk.END, "-" * 80 + "\n")  # Separator line

    # Displaying total interest
    result_text.insert(tk.END, f"\nTotal Interest: ₹ {total_interest:.3f}")
    
    result_text.config(state=tk.DISABLED)  # Disable the widget to make it uneditable

root = tk.Tk()
root.title(" Jignesh Compound Interest Calculation")

# Centering the window on the screen
window_width = 800
window_height = 600
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

# Centering all items
for i in range(6):  # Assuming there are 6 rows in your layout
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)

principle_label = tk.Label(root, text="Principle Amount")
principle_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")

principle_entry = tk.Entry(root, validate="key", validatecommand=(root.register(validate_numeric_input), '%P', '%d'))
principle_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")

interest_label = tk.Label(root, text="Interest Rate (%)")
interest_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")

rate_entry = tk.Entry(root, validate="key", validatecommand=(root.register(validate_numeric_input), '%P', '%d'))
rate_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")

time_label = tk.Label(root, text="Time (years)")
time_label.grid(row=2, column=0, padx=10, pady=10, sticky="e")

time_entry = tk.Entry(root, validate="key", validatecommand=(root.register(validate_numeric_input), '%P', '%d'))
time_entry.grid(row=2, column=1, padx=10, pady=10, sticky="w")
time_entry.bind("<FocusOut>", update_month_options)  # Bind event to update month options

month_label = tk.Label(root, text="Select Month")
month_label.grid(row=3, column=0, padx=10, pady=10, sticky="e")

month_options = ["All"]  # Initial options
month_combobox = ttk.Combobox(root, values=month_options)
month_combobox.grid(row=3, column=1, padx=10, pady=10, sticky="w")
month_combobox.set("All")  # Set default value

calculate_button = tk.Button(root, text="Calculate", command=calculate_button_click)
calculate_button.grid(row=4, column=1, padx=10, pady=10, sticky="w")

result_text = tk.Text(root, height=20, width=80, font=("arial", 12), state=tk.DISABLED)
result_text.grid(row=5, column=0, columnspan=2, pady=10, sticky="")

# Scrollbar for the Text widget
scrollbar = tk.Scrollbar(root, command=result_text.yview)
scrollbar.grid(row=5, column=2, sticky="ns")

# Attach the scrollbar to the Text widget
result_text.config(yscrollcommand=scrollbar.set)

root.mainloop()
