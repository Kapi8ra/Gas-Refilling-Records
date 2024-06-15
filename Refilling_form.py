import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pandas as pd
from datetime import datetime

class GasRefillingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gas Refilling System")
        
        # Configure style
        style = ttk.Style()
        style.theme_use('clam')  # Use 'clam' theme for a modern look
        style.configure("TLabel", font=("Arial", 14))
        style.configure("TButton", font=("Arial", 14))
        style.configure("TEntry", font=("Arial", 14))
        style.configure("Title.TLabel", font=("Arial", 18, "bold"))  # Title style
        
        self.create_widgets()

    def validate_entry(self, text):
        return text.isdigit() or text == ""

    def create_widgets(self):
        # Main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        vcmd = (self.root.register(self.validate_entry), '%P')
        
        # Title for Cylinder section
        ttk.Label(main_frame, text="Cylinder", style="Title.TLabel").grid(row=0, column=0, columnspan=2, pady=(0, 10))

        ttk.Label(main_frame, text="Enter Total of the cylinder type (10.7m3):").grid(row=1, column=0, sticky=tk.W)
        self.cylinder_10_7m3 = tk.Spinbox(main_frame, from_=0, to=1000, font=("Arial", 14), validate='key', validatecommand=vcmd)
        self.cylinder_10_7m3.grid(row=1, column=1, sticky=tk.E)

        ttk.Label(main_frame, text="Enter Total of the cylinder type (7.2m3):").grid(row=2, column=0, sticky=tk.W)
        self.cylinder_7_2m3 = tk.Spinbox(main_frame, from_=0, to=1000, font=("Arial", 14), validate='key', validatecommand=vcmd)
        self.cylinder_7_2m3.grid(row=2, column=1, sticky=tk.E)

        ttk.Label(main_frame, text="Enter Total of the cylinder type (1.4m3):").grid(row=3, column=0, sticky=tk.W)
        self.cylinder_1_4m3 = tk.Spinbox(main_frame, from_=0, to=1000, font=("Arial", 14), validate='key', validatecommand=vcmd)
        self.cylinder_1_4m3.grid(row=3, column=1, sticky=tk.E)

        # Title for Bundle section
        ttk.Label(main_frame, text="Bundle", style="Title.TLabel").grid(row=4, column=0, columnspan=2, pady=(10, 10))

        ttk.Label(main_frame, text="Enter Total of the cylinder type B(15)_10.7m3:").grid(row=5, column=0, sticky=tk.W)
        self.cylinder_B15_10_7m3 = tk.Spinbox(main_frame, from_=0, to=1000, font=("Arial", 14), validate='key', validatecommand=vcmd)
        self.cylinder_B15_10_7m3.grid(row=5, column=1, sticky=tk.E)

        ttk.Label(main_frame, text="Enter Total of the cylinder type B(16)_10.7m3:").grid(row=6, column=0, sticky=tk.W)
        self.cylinder_B16_10_7m3 = tk.Spinbox(main_frame, from_=0, to=1000, font=("Arial", 14), validate='key', validatecommand=vcmd)
        self.cylinder_B16_10_7m3.grid(row=6, column=1, sticky=tk.E)

        ttk.Label(main_frame, text="Enter Total of the cylinder type B(15)_7.2m3_SIG:").grid(row=7, column=0, sticky=tk.W)
        self.cylinder_B15_7_2m3_SIG = tk.Spinbox(main_frame, from_=0, to=1000, font=("Arial", 14), validate='key', validatecommand=vcmd)
        self.cylinder_B15_7_2m3_SIG.grid(row=7, column=1, sticky=tk.E)

        # Title for Rejected Cylinders section
        ttk.Label(main_frame, text="Rejected Cylinders", style="Title.TLabel").grid(row=8, column=0, columnspan=2, pady=(10, 10))

        ttk.Label(main_frame, text="Enter Number of Rejected Cylinders:").grid(row=9, column=0, sticky=tk.W)
        self.rejected_cylinders = tk.Spinbox(main_frame, from_=0, to=1000, font=("Arial", 14), validate='key', validatecommand=vcmd)
        self.rejected_cylinders.grid(row=9, column=1, sticky=tk.E)

        ttk.Label(main_frame, text="Enter Remarks for Rejected Cylinders:").grid(row=10, column=0, sticky=tk.W)
        self.remarks = ttk.Entry(main_frame)
        self.remarks.grid(row=10, column=1, sticky=tk.E)

        # Title for Liquid Tank section
        ttk.Label(main_frame, text="Liquid Tank", style="Title.TLabel").grid(row=11, column=0, columnspan=2, pady=(10, 10))

        ttk.Label(main_frame, text="Enter Before Liquid Tank Level in m3:").grid(row=12, column=0, sticky=tk.W)
        self.before_level_m3 = ttk.Entry(main_frame)
        self.before_level_m3.grid(row=12, column=1, sticky=tk.E)

        ttk.Label(main_frame, text="Enter After Liquid Tank Level in m3:").grid(row=13, column=0, sticky=tk.W)
        self.after_level_m3 = ttk.Entry(main_frame)
        self.after_level_m3.grid(row=13, column=1, sticky=tk.E)

        ttk.Button(main_frame, text="Save Data", command=self.save_data).grid(row=14, column=0, columnspan=2, pady=10)

    def save_data(self):
        try:
            data = {
                'Date': datetime.now().strftime("%Y-%m-%d"),
                '10.7m3': int(self.cylinder_10_7m3.get()),
                '7.2m3': int(self.cylinder_7_2m3.get()),
                '1.4m3': int(self.cylinder_1_4m3.get()),
                'B(15)_10.7m3': int(self.cylinder_B15_10_7m3.get()),
                'B(16)_10.7m3': int(self.cylinder_B16_10_7m3.get()),
                'B(15)_7.2m3_SIG': int(self.cylinder_B15_7_2m3_SIG.get()),
                'Rejected': int(self.rejected_cylinders.get()),
                'Remarks': self.remarks.get(),
                'Before_Level_m3': float(self.before_level_m3.get()),
                'After_Level_m3': float(self.after_level_m3.get()),
                'Gas_Used_m3': float(self.before_level_m3.get()) - float(self.after_level_m3.get()),
            }
            data['Gas_Used_kg'] = data['Gas_Used_m3'] * 1.429  # Oxygen Density kg/m3
            
            new_entry = pd.DataFrame([data])
            
            try:
                df = pd.read_excel('refilling_records.xlsx')
                df = pd.concat([df, new_entry], ignore_index=True)
            except FileNotFoundError:
                df = new_entry
            
            df.to_excel('refilling_records.xlsx', index=False)
            messagebox.showinfo("Success", "Data saved successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Error saving data: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = GasRefillingApp(root)
    root.mainloop()
