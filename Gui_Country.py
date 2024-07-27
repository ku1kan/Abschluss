import tkinter as tk
from tkinter import ttk
from Countries_info import countries


class GUI:
    def __init__(self, root, countries):  # Creates GUI  with root Window and list of Countries
        self.add_add_new_country_window = None
        self.root = root
        self.countries = countries

        self.style = ttk.Style()
        self.style.theme_use("clam")  # Sets the theme for the Gui

        self.style.configure("TButton", font=("calibre", 12, "bold"))  # Configures the style for the button
        self.style.map("TButton", foreground=[("pressed", "blue"), ("active", "yellow")])  # For Style configuration

        self.root.title("Country-Data")  # Window Title
        self.root.geometry("1100x1000")  # Window Size

        # Creates the Listbox to show the display info
        self.country_listbox = tk.Listbox(self.root, width=40, height=15)
        self.country_listbox.pack(padx=15, pady=15, side=tk.LEFT)
        self.country_listbox.bind("<<ListboxSelect>>", self.show_country_info_data)

        # Creates a frame to display the detailed country information
        self.info_frame = tk.Frame(self.root)
        self.info_frame.pack(padx=10, pady=10, side=tk.LEFT, fill=tk.NONE)

        # Creates the labels to display the country details
        self.country_label = tk.Label(self.info_frame, text="Country: ")
        self.country_label.pack()
        self.population_label = tk.Label(self.info_frame, text="Population: ")
        self.population_label.pack()
        self.capital_label = tk.Label(self.info_frame, text="Capital: ")
        self.capital_label.pack()
        self.area_label = tk.Label(self.info_frame, text="Area: ")
        self.area_label.pack()

        # Creates the Listbox to display subdivisions
        self.subdivision_listbox = tk.Listbox(self.root, width=65, height=10)
        self.subdivision_listbox.pack(padx=10, pady=10, side=tk.LEFT)

        # Configures the style of the Button for the "Add Country" Button
        # Configures the style of the Button for the "Add Country" Button
        self.style.configure("Add.TButton", foreground="orange", font=("Arial", 14, "bold"))
        self.add_button = ttk.Button(self.root, text="Add New Country", style="Add.TButton",
                                     command=self.add_new_country_window)
        self.add_button.pack(padx=6, pady=6, side=tk.LEFT)

        # Configures the style of the Button for the "Quit" Button
        self.style.configure("Quit.TButton", foreground="red", font=("Arial", 14, "bold"))
        self.quit_button = ttk.Button(self.root, text="Quit", style="Quit.TButton",
                                      command=self.root.destroy)
        self.quit_button.pack(padx=5, pady=5, side=tk.LEFT)  # Creates the "Quit" button

        self.update_country_listbox()  # Updates the country listbox with the initial list of countries

    def update_country_listbox(self):  # Shows the Country information and deletes the old information form the listbox
        self.country_listbox.delete(0, tk.END)
        for country in self.countries:
            self.country_listbox.insert(tk.END, country["Country"])

    def show_country_info_data(self, event):  # Shows the information for the selected country
        selected_index = self.country_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            country = self.countries[index]
            self.country_label.config(text=f"Country: {country['Country']}")
            self.population_label.config(text=f"Population: {country['Population']}")
            self.capital_label.config(text=f"Capital: {country['Capital']}")
            self.area_label.config(text=f"Area: {country['Area']}")

            self.subdivision_listbox.delete(0, tk.END)  # Shows subdivision info and replace it with the old info
            for subdivision in country["Subdivisions"]:
                self.subdivision_listbox.insert(
                    tk.END,
                    f"{subdivision['Name']} - Population: {subdivision['Population']} "f" - Area: {subdivision['Area']}"
                )

    def add_new_country_window(self):  # Opens a new window to add a country
        self.add_add_new_country_window = tk.Toplevel(self.root)
        self.add_add_new_country_window.title("Add New Country with Subdivisions")

        # Creates the entry fields for country details
        tk.Label(self.add_add_new_country_window, text="Country Name").pack()
        self.country_name_entry = tk.Entry(self.add_add_new_country_window)
        self.country_name_entry.pack()

        tk.Label(self.add_add_new_country_window, text="Population:").pack()
        self.population_entry = tk.Entry(self.add_add_new_country_window)
        self.population_entry.pack()

        tk.Label(self.add_add_new_country_window, text="Capital:").pack()
        self.capital_entry = tk.Entry(self.add_add_new_country_window)
        self.capital_entry.pack()

        tk.Label(self.add_add_new_country_window, text="Area").pack()
        self.area_entry = tk.Entry(self.add_add_new_country_window)
        self.area_entry.pack()

        self.subdivision_frame = tk.Frame(self.add_add_new_country_window)  # Creates a frame to show the info about the
        self.subdivision_frame.pack(padx=10, pady=10)  # subdivisions

        # Initializes the list to hold subdivision entries
        self.subdivision_entries = []
        self.add_add_subdivision_entry()

        # Creates a Button to add a subdivision and to add the Country
        tk.Button(self.add_add_new_country_window, text="Add Subdivision", command=self.add_add_subdivision_entry).pack(
            pady=5)
        tk.Button(self.add_add_new_country_window, text="Add Country", command=self.add_country).pack(pady=5)

    def add_add_subdivision_entry(self):
        entry_subdivision_frame = tk.Frame(self.subdivision_frame)  # Creates a new entry frame for a subdivision
        entry_subdivision_frame.pack(pady=5)

        tk.Label(entry_subdivision_frame, text="Subdivision:").pack(side=tk.LEFT)
        name_entry = tk.Entry(entry_subdivision_frame, width=20)
        name_entry.pack(side=tk.LEFT)
        tk.Label(entry_subdivision_frame, text="Population:").pack(side=tk.LEFT)
        population_entry = tk.Entry(entry_subdivision_frame, width=10)
        population_entry.pack(side=tk.LEFT)
        tk.Label(entry_subdivision_frame, text="Area:").pack(side=tk.LEFT)
        area_entry = tk.Entry(entry_subdivision_frame, width=10)
        area_entry.pack(side=tk.LEFT)

        self.subdivision_entries.append(
            (name_entry, population_entry, area_entry))  # Adds the new subdivision to the list

    def add_country(self):  # Gets the information of the new country
        name = self.country_name_entry.get()
        population = self.population_entry.get()
        capital = self.capital_entry.get()
        area = self.area_entry.get()

        subdivisions = []  # Gets the subdivision det
        for name_entry, population_entry, area_entry in self.subdivision_entries:
            subdivision_name = name_entry.get()
            subdivision_population = population_entry.get()
            subdivision_area = area_entry.get()
            if subdivision_name and subdivision_population and subdivision_area:
                subdivisions.append({
                    "Name": subdivision_name,
                    "Population": subdivision_population,
                    "Area": subdivision_area
                })

        add_new_country = {
            "Country": name,
            "Population": population,
            "Capital": capital,
            "Area": area,
            "Subdivisions": subdivisions

        }

        # Adds new country to the list
        self.countries.append(add_new_country)
        self.update_country_listbox()
        self.add_add_new_country_window.destroy()

root = tk.Tk()
window = GUI(root, countries)
root.mainloop()
