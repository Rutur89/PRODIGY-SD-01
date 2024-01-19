import tkinter as tk
from tkinter import messagebox

class TemperatureConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Temperature Converter")
        self.root.geometry("300x200")
        self.root.configure(bg="#3498db")  # Set background color

        self.temperature_label = tk.Label(root, text="Enter Temperature:", bg="#3498db", fg="white")  # Set text and background color
        self.temperature_label.pack()

        self.temperature_entry = tk.Entry(root)
        self.temperature_entry.pack(pady=5)

        self.unit_label = tk.Label(root, text="Select Unit:", bg="#3498db", fg="white")
        self.unit_label.pack()

        self.unit_var = tk.StringVar()
        self.unit_var.set("Celsius")

        self.unit_options = ["Celsius", "Fahrenheit", "Kelvin"]
        self.unit_menu = tk.OptionMenu(root, self.unit_var, *self.unit_options)
        self.unit_menu.pack(pady=5)

        self.convert_button = tk.Button(root, text="Convert", command=self.convert_temperature, bg="#2ecc71", fg="white")  # Set button color
        self.convert_button.pack(pady=10)

    def convert_temperature(self):
        try:
            temperature = float(self.temperature_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter a numerical value.")
            return

        original_unit = self.unit_var.get()

        if original_unit == "Celsius":
            fahrenheit = (temperature * 9/5) + 32
            kelvin = temperature + 273.15
        elif original_unit == "Fahrenheit":
            celsius = (temperature - 32) * 5/9
            kelvin = (temperature + 459.67) * 5/9
        elif original_unit == "Kelvin":
            celsius = temperature - 273.15
            fahrenheit = (temperature * 9/5) - 459.67

        result_message = f"{temperature} {original_unit} is equivalent to:\n"
        if original_unit != "Celsius":
            result_message += f"{celsius:.2f} Celsius\n"
        if original_unit != "Fahrenheit":
            result_message += f"{fahrenheit:.2f} Fahrenheit\n"
        if original_unit != "Kelvin":
            result_message += f"{kelvin:.2f} Kelvin"

        messagebox.showinfo("Result", result_message)

if __name__ == "__main__":
    root = tk.Tk()
    app = TemperatureConverterApp(root)
    root.mainloop()
