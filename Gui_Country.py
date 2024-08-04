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
        self.root.geometry("900x500")  # Window Size

        self.main_frame = ttk.Frame(self.root, padding=(15, 15, 15, 15))
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        self.main_frame.configure(style="MainFrame.TFrame")

        # Creates the Listbox to show the display info
        self.country_listbox = tk.Listbox(self.main_frame, font=("Arial", 12), justify="center", width=30,
                                          selectbackground="blue")
        self.country_listbox.grid(row=0, column=0, rowspan=6, padx=(0, 20), pady=(0, 10))

        self.scrollbar = tk.Scrollbar(self.main_frame, orient="vertical", command=self.country_listbox.yview)
        self.scrollbar.grid(row=0, column=1, rowspan=6, sticky="ns")
        self.country_listbox.config(yscrollcommand=self.scrollbar.set)  # Scrollbar for the Countries

        self.country_listbox.bind("<<ListboxSelect>>", self.show_country_info_data)

        # Creates a frame to display the detailed country information
        self.info_frame = tk.Frame(self.root, bg="#f9f9f9", bd=3, relief="sunken")
        self.info_frame.pack(padx=10, pady=10, side=tk.LEFT, fill=tk.NONE)

        # Creates the labels to display the country details
        self.country_label = ttk.Label(self.info_frame, text="Country: ", font=("Arial", 12))
        self.country_label.pack()
        self.population_label = ttk.Label(self.info_frame, text="Population: ", font=("Arial", 12))
        self.population_label.pack()
        self.capital_label = ttk.Label(self.info_frame, text="Capital: ", font=("Arial", 12))
        self.capital_label.pack()
        self.area_label = ttk.Label(self.info_frame, text="Area: ", font=("Arial", 12))
        self.area_label.pack()

        # Creates the Listbox to display subdivisions
        self.subdivision_listbox = tk.Listbox(self.root, width=60, height=10, selectbackground="blue")
        self.subdivision_listbox.pack(padx=10, pady=10, side=tk.LEFT)

        # Configures the style of the Button for the "Add Country" Button
        self.style.configure("Add.TButton", background="orange", foreground="white", font=("Arial", 14, "bold"),
                             padding=10)
        self.add_button = ttk.Button(self.root, text="Add New Country", style="Add.TButton",
                                     command=self.add_new_country_window)
        self.add_button.pack(padx=5, pady=5, side=tk.LEFT)

        # Configures the style of the Button for the "Quit" Button
        self.style.configure("Quit.TButton", background="orange", foreground="red", font=("Arial", 14, "bold"),
                             padding=10)
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
        tk.Label(self.add_add_new_country_window, text="Country Name", font=("Arial", 10, "bold")).pack()
        self.country_name_entry = tk.Entry(self.add_add_new_country_window, width=30)
        self.country_name_entry.pack()

        tk.Label(self.add_add_new_country_window, text="Population:", font=("Arial", 10, "bold")).pack()
        self.population_entry = tk.Entry(self.add_add_new_country_window, width=30)
        self.population_entry.pack()

        tk.Label(self.add_add_new_country_window, text="Capital:", font=("Arial", 10, "bold")).pack()
        self.capital_entry = tk.Entry(self.add_add_new_country_window, width=30)
        self.capital_entry.pack()

        tk.Label(self.add_add_new_country_window, text="Area in km²", font=("Arial", 10, "bold")).pack()
        self.area_entry = tk.Entry(self.add_add_new_country_window, width=30)
        self.area_entry.pack()

        self.subdivision_frame = tk.Frame(self.add_add_new_country_window)  # Creates a frame to show the info about the
        self.subdivision_frame.pack(padx=10, pady=10)  # subdivisions

        # Initializes the list to hold subdivision entries
        self.subdivision_entries = []
        self.add_add_subdivision_entry()

        # Creates a Button to add a subdivision and to add the Country
        (tk.Button(self.add_add_new_country_window, text="Add Subdivision", command=self.add_add_subdivision_entry)
         .pack(pady=5))

        tk.Button(self.add_add_new_country_window, text="Add Country", command=self.add_country).pack(pady=5)

    def add_add_subdivision_entry(self):
        entry_subdivision_frame = ttk.Frame(self.subdivision_frame)  # Creates a new entry frame for a subdivision
        entry_subdivision_frame.pack(pady=5, fill=tk.X)

        tk.Label(entry_subdivision_frame, text="Subdivision:", font=("Arial", 10, "bold")).pack(side=tk.LEFT)
        name_entry = tk.Entry(entry_subdivision_frame, width=30)
        name_entry.pack(side=tk.LEFT, padx=(10, 10))
        tk.Label(entry_subdivision_frame, text="Population:", font=("Arial", 10, "bold")).pack(side=tk.LEFT)
        population_entry = tk.Entry(entry_subdivision_frame, width=30)
        population_entry.pack(side=tk.LEFT, padx=(10, 10))
        tk.Label(entry_subdivision_frame, text="Area:", font=("Arial", 10, "bold")).pack(side=tk.LEFT)
        area_entry = tk.Entry(entry_subdivision_frame, width=30)
        area_entry.pack(side=tk.LEFT, padx=(10, 10))

        self.subdivision_entries.append(
            (name_entry, population_entry, area_entry))  # Adds the new subdivision to the list

    def add_country(self):  # Gets the information of the new country
        name = self.country_name_entry.get()
        population = self.population_entry.get()
        capital = self.capital_entry.get()
        area = self.area_entry.get()

        subdivisions = []  # Gets the information from the subdivisions
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

        add_new_country = { # Creates a entry for a new Country
            "Country": name,
            "Population": population,
            "Capital": capital,
            "Area": area,
            "Subdivisions": subdivisions

        }

        # Adds new country to the list and updates the list
        self.countries.append(add_new_country)
        self.update_country_listbox()
        self.add_add_new_country_window.destroy() # Closes the "Add Country Window"


root = tk.Tk()
window = GUI(root, countries)
root.mainloop()
