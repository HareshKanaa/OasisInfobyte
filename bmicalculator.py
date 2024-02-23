import tkinter as tk
from tkinter import messagebox

class BMIcalculator:
    def __init__(self):
        self.weight_kg = 0
        self.height_m = 0
        self.bmi = 0

    def calculate_bmi(self):
        self.bmi = self.weight_kg / (self.height_m ** 2)

    def interpret_bmi(self):
        if self.bmi < 18.5:
            return "Underweight"
        elif 18.5 <= self.bmi < 25:
            return "Normal weight"
        elif 25 <= self.bmi < 30:
            return "Overweight"
        else:
            return "Obese"

    def get_user_input(self):
        root = tk.Tk()
        root.title("BMI Calculator")
        root.geometry("400x300")
        root.configure(bg="#f0f0f0")

        weight_label = tk.Label(root, text="Enter weight in kilograms:", bg="#f0f0f0", fg="#333333", font=("Arial", 14))
        weight_label.pack(pady=10)
        weight_entry = tk.Entry(root, font=("Arial", 14))
        weight_entry.pack(pady=10)

        height_label = tk.Label(root, text="Enter height in meters:", bg="#f0f0f0", fg="#333333", font=("Arial", 14))
        height_label.pack(pady=10)
        height_entry = tk.Entry(root, font=("Arial", 14))
        height_entry.pack(pady=10)

        def calculate_bmi_gui():
            try:
                self.weight_kg = float(weight_entry.get())
                self.height_m = float(height_entry.get())
                self.calculate_bmi()
                result = f"Your BMI is: {self.bmi:.2f}\nBMI Category: {self.interpret_bmi()}"
                messagebox.showinfo("BMI Result", result)
            except ValueError:
                messagebox.showerror("Error", "Please enter valid numeric input for weight and height.")

        calculate_button = tk.Button(root, text="Calculate BMI", command=calculate_bmi_gui, bg="#4CAF50", fg="white", font=("Arial", 14))
        calculate_button.pack(pady=20)

        root.mainloop()

def main():
    calculator = BMIcalculator()
    calculator.get_user_input()

if __name__ == "__main__":
    main()
