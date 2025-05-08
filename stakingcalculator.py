import tkinter as tk
from tkinter import messagebox

def calculate_staking():
    try:
        bankroll = float(entry_bankroll.get())
        total_buyins = float(entry_total_buyins.get())
        roi_percent = float(entry_roi.get())
        max_exposure_percent = float(entry_max_exposure.get())
        field_size = int(entry_field_size.get())

        base_markup = 1 + (roi_percent / 100)
        exposure = total_buyins / bankroll
        max_allowed_buyins = bankroll * (max_exposure_percent / 100)

        if total_buyins <= max_allowed_buyins:
            sell_percent = 0
        else:
            sell_percent = 1 - (max_allowed_buyins / total_buyins)

        if field_size > 1000:
            adjustment = ((field_size - 1000) / 1000) * 0.02
            adjusted_markup = base_markup - adjustment
        else:
            adjusted_markup = base_markup

        adjusted_markup = max(adjusted_markup, 1.0)

        result_text.set(f"Base Markup: {round(base_markup, 3)}\n"
                        f"Adjusted Markup: {round(adjusted_markup, 3)}\n"
                        f"Sell Percent: {round(sell_percent * 100, 1)}%\n"
                        f"Your Risk if No Sale: {round(exposure * 100, 1)}%\n"
                        f"Max Safe Risk Allowed: {max_exposure_percent}%")
    except ValueError:
        messagebox.showerror("Input error", "Please enter valid numbers in all fields.")

# GUI setup
root = tk.Tk()
root.title("Poker Staking Calculator")

# Input fields
labels = ["Bankroll ($)", "Total Buy-ins ($)", "Estimated ROI (%)", "Max Exposure (%)", "Average Field Size"]
entries = []

for label_text in labels:
    label = tk.Label(root, text=label_text)
    label.pack()
    entry = tk.Entry(root)
    entry.pack()
    entries.append(entry)

entry_bankroll, entry_total_buyins, entry_roi, entry_max_exposure, entry_field_size = entries

# Calculate button
calculate_button = tk.Button(root, text="Calculate", command=calculate_staking)
calculate_button.pack()

# Output area
result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, justify=tk.LEFT, padx=10, pady=10)
result_label.pack()

# Run the app
root.mainloop()

