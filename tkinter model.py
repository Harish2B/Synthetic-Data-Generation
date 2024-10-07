import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import configparser
import subprocess

class MainApplication:
    def __init__(self, root):
        self.root = root
        self.config = configparser.ConfigParser()
        self.root.title("Synthetic Data Generator")
        self.root.geometry("1024x728")

        # Create menu
        self.menu = tk.Menu(self.root)
        self.root.config(menu=self.menu)

        self.file_menu = tk.Menu(self.menu)
        self.menu.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="Open File", command=self.open_file)
        self.file_menu.add_command(label="New File", command=self.new_file)
        self.file_menu.add_command(label="Save", command=self.save)
        self.file_menu.add_command(label="Save As", command=self.save_as)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.root.quit)

        # Create tabs
        self.tabs = ttk.Notebook(self.root)
        self.tabs.pack(fill="both", expand=True)

        self.attributes_tab = ttk.Frame(self.tabs)
        self.constraints_tab = ttk.Frame(self.tabs)
        self.time_series_tab = ttk.Frame(self.tabs)
        self.relationships_tab = ttk.Frame(self.tabs)
        self.noise_tab = ttk.Frame(self.tabs)

        self.tabs.add(self.attributes_tab, text="Attributes")
        self.tabs.add(self.constraints_tab, text="Constraints")
        self.tabs.add(self.time_series_tab, text="Time Series")
        self.tabs.add(self.relationships_tab, text="Relationships")
        self.tabs.add(self.noise_tab, text="Noise")

        # Create attributes frame
        self.attributes_frame = ttk.Frame(self.attributes_tab)
        self.attributes_frame.pack(fill="both", expand=True)

        self.attributes_label = ttk.Label(self.attributes_frame, text="Enter attributes:")
        self.attributes_label.pack()

        self.attributes_entry = ttk.Entry(self.attributes_frame)
        self.attributes_entry.pack()

        self.attributes_button = ttk.Button(self.attributes_frame, text="Add", command=self.add_attribute)
        self.attributes_button.pack()

        self.attributes_listbox = tk.Listbox(self.attributes_frame)
        self.attributes_listbox.pack()

        self.done_attributes_button = ttk.Button(self.attributes_frame, text="Done", command=self.done_attributes)
        self.done_attributes_button.pack()

        def done_attributes(self):
            self.tabs.select("Constraints")  # Move to the next tab (Constraints)

        # Create constraints frame
        self.constraints_frame = ttk.Frame(self.constraints_tab)
        self.constraints_frame.pack(fill="both", expand=True)

        self.attributes_var = tk.StringVar()
        self.attributes_label = ttk.Label(self.constraints_frame, text="Attributes:")
        self.attributes_label.pack()
        self.attributes_menu = ttk.OptionMenu(self.constraints_frame, self.attributes_var)
        self.attributes_menu.pack()

        # Create minimum entry
        self.min_label = ttk.Label(self.constraints_frame, text="Minimum:")
        self.min_label.pack()
        self.min_entry = ttk.Entry(self.constraints_frame)
        self.min_entry.pack()

        # Create maximum entry
        self.max_label = ttk.Label(self.constraints_frame, text="Maximum:")
        self.max_label.pack()
        self.max_entry = ttk.Entry(self.constraints_frame)
        self.max_entry.pack()
        # Create temporal pattern option menu
        self.seasonality_label = ttk.Label(self.constraints_frame, text="seasonality:")
        self.seasonality_label.pack()
        self.seasonality_var = tk.StringVar()
        self.seasonality_var.set("daily")
        self.seasonality_options = ["daily", "weekly", "monthly", "quarterly", "yearly"]
        self.seasonality_menu = ttk.OptionMenu(self.constraints_frame, self.seasonality_var,*self.seasonality_options)
        self.seasonality_menu.pack()

        # Create seasonality option menu
        # Create trend type option menu
        self.trend_type_label = ttk.Label(self.constraints_frame, text="trend:")
        self.trend_type_label.pack()
        self.trend_type_var = tk.StringVar()
        self.trend_type_var.set("increasing")
        self.trend_type_options = ["increasing", "decreasing", "no changes"]
        self.trend_type_menu = ttk.OptionMenu(self.constraints_frame, self.trend_type_var, *self.trend_type_options)
        self.trend_type_menu.pack()

        # Create trend value entry
        self.trend_value_label = ttk.Label(self.constraints_frame, text="Trend Value:")
        self.trend_value_label.pack()
        self.trend_value_entry = ttk.Entry(self.constraints_frame)
        self.trend_value_entry.pack()

        # Create add constraint button
        self.constraints_button = ttk.Button(self.constraints_frame, text="Add", command=self.add_constraint)
        self.constraints_button.pack()

        # Create listbox to display constraints
        self.constraints_listbox = tk.Listbox(self.constraints_frame)
        self.constraints_listbox.pack()

        # Create done button
        self.done_constraints_button = ttk.Button(self.constraints_frame, text="Done", command=self.done_constraints)
        self.done_constraints_button.pack()

        # Create time series frame
        self.time_series_frame = ttk.Frame(self.time_series_tab)
        self.time_series_frame.pack(fill="both", expand=True)

        self.time_picker_frame = ttk.Frame(self.time_series_frame)
        self.time_picker_frame.pack(fill="both", expand=True)

        self.start_time_label = ttk.Label(self.time_picker_frame, text="Enter start time (dd-mm-yyyy hh:mm:ss):")
        self.start_time_label.grid(row=0, column=0, padx=5, pady=5)
        self.start_time_entry = ttk.Entry(self.time_picker_frame, width=20)
        self.start_time_entry.grid(row=1, column=0, padx=5, pady=5)

        self.end_time_label = ttk.Label(self.time_picker_frame, text="Enter end time (dd-mm-yyyy hh:mm:ss):")
        self.end_time_label.grid(row=0, column=1, padx=5, pady=5)
        self.end_time_entry = ttk.Entry(self.time_picker_frame, width=20)
        self.end_time_entry.grid(row=1, column=1, padx=5, pady=5)

        self.time_interval_label = ttk.Label(self.time_picker_frame, text="Enter time interval:")
        self.time_interval_label.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        self.time_interval_var = tk.StringVar()
        self.time_interval_var.set("1 min")
        self.time_interval_options = ["1 min", "5 min", "10 min", "15 min", "30 min", "1 hour", "4 hours","8 hours", "12 hours","24 hours", "Custom"]
        self.time_interval_menu = ttk.OptionMenu(self.time_picker_frame, self.time_interval_var,*self.time_interval_options)
        self.time_interval_menu.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

        self.custom_time_interval_frame = ttk.Frame(self.time_picker_frame)
        self.custom_time_interval_frame.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

        self.custom_time_interval_label = ttk.Label(self.custom_time_interval_frame,text="Enter custom time interval:")
        self.custom_time_interval_label.pack_forget()  # Hide the label initially
        self.custom_time_interval_entry = ttk.Entry(self.custom_time_interval_frame)
        self.custom_time_interval_entry.pack_forget()  # Hide the entry initially

        def show_custom_time_interval_entry(*args):
            if self.time_interval_var.get() == "Custom":
                self.custom_time_interval_label.pack()
                self.custom_time_interval_entry.pack()
            else:
                self.custom_time_interval_label.pack_forget()
                self.custom_time_interval_entry.pack_forget()

        self.time_interval_var.trace('w', show_custom_time_interval_entry)

        self.done_time_series_button = ttk.Button(self.time_series_frame, text="Done",command=self.done_time_series)
        self.done_time_series_button.pack()

        def done_time_series(self):
            self.tabs.select(3)  # Move to the next tab (Relationships)

        # Create relationships frame
        self.relationships_frame = ttk.Frame(self.relationships_tab)
        self.relationships_frame.pack(fill="both", expand=True)

        self.dependent_label = ttk.Label(self.relationships_frame, text="Select dependent attribute:")
        self.dependent_label.pack()
        self.dependent_var = tk.StringVar()
        self.dependent_options = []
        self.dependent_menu = ttk.OptionMenu(self.relationships_frame, self.dependent_var, *self.dependent_options)
        self.dependent_menu.pack()

        self.independent_label = ttk.Label(self.relationships_frame, text="Select independent attribute:")
        self.independent_label.pack()
        self.independent_var = tk.StringVar()
        self.independent_options = []
        self.independent_menu = ttk.OptionMenu(self.relationships_frame, self.independent_var,*self.independent_options)
        self.independent_menu.pack()

        self.relationship_label = ttk.Label(self.relationships_frame, text="Select relationship:")
        self.relationship_label.pack()
        self.relationship_var = tk.StringVar()
        self.relationship_var.set("linear")
        self.relationship_options = ["linear", "parabolic", "exponential", "sinusoidal", "hyperbolic", "sigmoid"]
        self.relationship_menu = ttk.OptionMenu(self.relationships_frame, self.relationship_var,*self.relationship_options)
        self.relationship_menu.pack()

        self.relationship_button = ttk.Button(self.relationships_frame, text="Add", command=self.add_relationship)
        self.relationship_button.pack()

        self.relationship_listbox = tk.Listbox(self.relationships_frame)
        self.relationship_listbox.pack()

        self.done_relationship_button = ttk.Button(self.relationships_frame, text="Done",command=self.done_relationship)
        self.done_relationship_button.pack()

        def done_relationship(self):
            self.tabs.select(4)  # Move to the next tab (Noise)

        # Create noise frame
        self.noise_frame = ttk.Frame(self.noise_tab)
        self.noise_frame.pack(fill="both", expand=True)

        self.noise_level_label = ttk.Label(self.noise_frame, text="Enter noise level:")
        self.noise_level_label.pack()
        self.noise_level_entry = ttk.Entry(self.noise_frame)
        self.noise_level_entry.pack()

        self.outlier_proportion_label = ttk.Label(self.noise_frame, text="Enter outlier proportion:")
        self.outlier_proportion_label.pack()
        self.outlier_proportion_entry = ttk.Entry(self.noise_frame)
        self.outlier_proportion_entry.pack()

        self.outlier_magnitude_label = ttk.Label(self.noise_frame, text="Enter outlier magnitude:")
        self.outlier_magnitude_label.pack()
        self.outlier_magnitude_entry = ttk.Entry(self.noise_frame)
        self.outlier_magnitude_entry.pack()

        self.run_button = ttk.Button(self.noise_frame, text="Run", command=self.run_code)
        self.run_button.pack()

    def open_file(self):
        filename = filedialog.askopenfilename()
        if filename:
            self.config.read(filename)
            self.attributes_listbox.delete(0, tk.END)
            self.constraints_listbox.delete(0, tk.END)
            self.relationship_listbox.delete(0, tk.END)

            for key, value in self.config.items('Attributes'):
                self.attributes_listbox.insert(tk.END, value)

            for key, value in self.config.items('Constraints'):
                self.constraints_listbox.insert(tk.END, value)

            for key, value in self.config.items('Relationships'):
                self.relationship_listbox.insert(tk.END, value)

    def new_file(self):
        self.attributes_listbox.delete(0, tk.END)
        self.constraints_listbox.delete(0, tk.END)
        self.relationship_listbox.delete(0, tk.END)
        self.start_time_entry.delete(0, tk.END)
        self.end_time_entry.delete(0, tk.END)
        self.noise_level_entry.delete(0, tk.END)
        self.outlier_proportion_entry.delete(0, tk.END)
        self.outlier_magnitude_entry.delete(0, tk.END)

    def save(self):
        self.save_config()

    def save_as(self):
        filename = filedialog.asksaveasfilename(defaultextension=".ini")
        if filename:
            with open(filename, 'w') as configfile:
                self.config.write(configfile)

    def add_attribute(self):
        attribute = self.attributes_entry.get()
        if not attribute:
            tk.messagebox.showerror("Error", "Attribute cannot be empty")
        else:
            self.attributes_listbox.insert(tk.END, attribute)
            self.attributes_entry.delete(0, tk.END)
            self.dependent_options.append(attribute)
            self.independent_options.append(attribute)
            menu = self.dependent_menu["menu"]
            menu.add_command(label=attribute, command=lambda value=attribute: self.dependent_var.set(value))
            menu = self.independent_menu["menu"]
            menu.add_command(label=attribute, command=lambda value=attribute: self.independent_var.set(value))
            self.dependent_var.set(attribute)  # Set the default value
            self.independent_var.set(attribute)  # Set the default value

        # Update the OptionMenu with the new options
        self.attributes_menu.set_menu(*self.dependent_options)
        self.dependent_menu.set_menu(*self.dependent_options)
        self.independent_menu.set_menu(*self.independent_options)

    def add_constraint(self):
        try:
            attribute = self.attributes_var.get()
            min_val = self.min_entry.get()
            max_val = self.max_entry.get()
            temporal_pattern = self.trend_type_var.get()
            seasonality = self.seasonality_var.get()
            amplitude=self.trend_value_entry.get()
            if not attribute or not min_val or not max_val:
                raise ValueError("All fields are required")
            min_val = float(min_val)
            max_val = float(max_val)
            if min_val >= max_val:
                raise ValueError("Minimum value cannot be greater than or equal to maximum value")
            self.constraints_listbox.insert(tk.END, f"{attribute}:{min_val},{max_val},{seasonality},{temporal_pattern},{amplitude}")
            self.min_entry.delete(0, tk.END)
            self.max_entry.delete(0, tk.END)
        except ValueError as e:
            tk.messagebox.showerror("Error", str(e))

    def add_relationship(self):
        try:
            dependent = self.dependent_var.get()
            independent = self.independent_var.get()
            relationship = self.relationship_var.get()
            if not dependent or not independent or not relationship:
                raise ValueError("All fields are required")
            self.relationship_listbox.insert(tk.END, f"{relationship}:{dependent},{independent}")
        except ValueError as e:
            tk.messagebox.showerror("Error", str(e))

    def done_time_series(self):
        try:
            start_time = self.start_time_entry.get()
            end_time = self.end_time_entry.get()
            time_interval = self.time_interval_var.get()
            if not start_time or not end_time or not time_interval:
                raise ValueError("All fields are required")
            if end_time <= start_time:
                raise ValueError("End time must be after start time")
        except ValueError as e:
            tk.messagebox.showerror("Error", str(e))

    def done_attributes(self):
        pass

    def done_constraints(self):
        pass

    def done_relationship(self):
        pass

    def done_noise(self):
        try:
            noise_level = self.noise_level_entry.get()
            outlier_proportion = self.outlier_proportion_entry.get()
            outlier_magnitude = self.outlier_magnitude_entry.get()
            if not noise_level or not outlier_proportion or not outlier_magnitude:
                raise ValueError("All fields are required")
            noise_level = float(noise_level)
            outlier_proportion = float(outlier_proportion)
            outlier_magnitude = float(outlier_magnitude)
            if noise_level < 0 or outlier_proportion < 0 or outlier_magnitude < 0:
                raise ValueError("All values must be non-negative")
        except ValueError as e:
            tk.messagebox.showerror("Error", str(e))

    def save_config(self):
        self.config['Attributes'] = {}
        for i in range(self.attributes_listbox.size()):
            self.config['Attributes'][f'attribute_{i}'] = self.attributes_listbox.get(i)

        self.config['Constraints'] = {}
        for i in range(self.constraints_listbox.size()):
            self.config['Constraints'][f'constraint_{i}'] = self.constraints_listbox.get(i)

        self.config['Relationships'] = {}
        for i in range(self.relationship_listbox.size()):
            self.config['Relationships'][f'relationship_{i}'] = self.relationship_listbox.get(i)

        self.config['Time Series'] = {}
        self.config['Time Series']['start_time'] = self.start_time_entry.get()
        self.config['Time Series']['end_time'] = self.end_time_entry.get()
        self.config['Time Series']['time_interval'] = self.time_interval_var.get()

        self.config['Noise'] = {}
        self.config['Noise']['noise_level'] = self.noise_level_entry.get()
        self.config['Noise']['outlier_proportion'] = self.outlier_proportion_entry.get()
        self.config['Noise']['outlier_magnitude'] = self.outlier_magnitude_entry.get()

        with open('config.ini', 'w') as configfile:
            self.config.write(configfile)

    @staticmethod
    def run_code():
        subprocess.run(['python', 'main_function.py'])

if __name__ == "__main__":
    root = tk.Tk()
    app = MainApplication(root)
    root.mainloop()
