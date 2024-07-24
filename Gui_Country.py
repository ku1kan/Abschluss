import tkinter as tk
from tkinter import ttk
from Countries_info import countries


class GUI:
    def __init__(self, root, countries): #Creats GUI  with root Window and list of Countries
        self.root = root
        self.countries = countries

        self.style = ttk.Style()
        style.theme_use("clam") #Sets the theme for the Gui

        style.configure("TButton", font=("calibre", 12, "bold")) #Configures the style for the button
        style.map("TButton", foreground=[("pressed", "blue"), ("active", "yellow")]) #For Style configuration

        self.root.title("Country-Data") #Window Title
        self.root.geometry("1100x1000") #Window Size

        #Creates the Listbox to show the display info
        self.country_listbox = tk.Listbox(self.root, width=40, height=15)
        self.country_listbox.pack(padx=15, pady=15, side=tk.LEFT)
        self.country_listbox.bind("<<ListboxSelect>>", self.show_country_info)

        #Creats a frame to display the detailed country information
        self.info_frame = tk.Frame(self.root)
        self.info_frame.pack(padx=10, pady=10, side=tk.LEFT, fill=tk.NONE)

        #Creates the labels to diplay the country details
        self.country_label = tk.Label(self.info_frame, text="Country: ")
        self.country_label.pack()
        self.population_label = tk.Label(self.info_frame, text="Population: ")
        self.population_label.pack()
        self.capital_label = tk.Label(self.info_frame, text="Capital: ")
        self.capital_label.pack()
        self.area_label = tk.Label(self.info_frame, text="Area: ")
        self.area_label.pack()

        #Creates the Listbox to display subdivisions
        self.subdivision_listbox = tk.Listbox(self.root, width=65, height=10)
        self.subdivision_listbox.pack(padx=10, pady=10, side=tk.LEFT)

        #Configures the style of the Button for the "Add Country" Button
        self.style.configure("Add.TButton", foreground="orange", font=("Arial", 14, "bold"))
        self.add_button = ttk.Button(self.root, text="Add New Country", style="Add.TButton",
                                     command=self.add_country_window)
        self.add_button.pack(padx=6, pady=6, side=tk.LEFT)

        #Configures the style of the Button for the "Quit" Button
        self.style.configure("Quit.TButton", foreground="red", font=("Arial", 14, "bold"))

        self.add_button = ttk.Button(self.root, text="Quit", style="Add.TButton",
                                     command=self.root.destroy)
        self.add_button.pack(padx=5, pady=5, side=tk.LEFT)  # Creates the "Quit" button

        self.update_country_listbox() #Updates the country listbox with the initial list of countries

    def update_country_listbox(self): #Shows the Country information and deletes the old information form the listbox
        self.country_listbox.delete(0, tk.END)
        for country in self.countries:
            self.country_listbox.insert(tk.END, country["Country"])

    def shop_country_info(self): #Shows the information for the selected country
        selected_index = self.country_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            country = self.countries[index]
            self.country_label.config(text=f"Country: {country["Country"]}")
            self.population_label.config(text=f"Population: {country["Population"]}")
            self.capital_label.config(text=f"Capital: {country["Capital"]}")
            self.area_label.config(text=f"Area: {country['Area']}")

            self.subdivision_listbox.delete(0, tk.END) #Shows subdivision info and replace it with the old info
            for subdivision in country["Subdivisions"]:
                self.subdivision_listbox.insert(
                    tk.END,
                    f"{subdivision['Name']} - Population: {subdivision['Population']} "f" - Area: {subdivision['Area']}"
                )

    def add_new_country_window(self): #Opens a new window to add a country
        self.add_add_new_country_window = tk.Toplevel(self.root)
        self.add_add_new_country_window.title("Add New Country with Subdivisions")

        #Creates the entry fields for country detailes
        tk.Label(self.add_add_new_country_window, text="Country Name").pack()
        self.name_entry = tk.Entry(self.add_add_new_country_window)
        self.name_entry.pack()

        tk.Label(self.add_add_new_country_window, text="Population:").pack()
        self.name_entry = tk.Entry(self.add_add_new_country_window)
        self.name_entry.pack()

        tk.Label(self.add_add_new_country_window, text="Capital:").pack()
        self.name_entry = tk.Entry(self.add_add_new_country_window)
        self.name_entry.pack()

        tk.label(self.add_add_new_country_window, text="Area").pack()
        self.name_entry = tk.Entry(self.add_add_new_country_window)
        self.name_entry.pack()


        self.subdivision_frame = tk.Frame(self.add_add_new_country_window) #Creates a frame to show the info about the
        self.subdivision_frame.pack(padx=10, pady=10)                       #subdivisions

        # Initializes the list to hold subdivision entries
        self.subdivision_entries = []
        self.add_subdivision_entry()

        #Creates a Button to add a subdivision and to add the Country
        tk.Button(self.add_add_new_country_window,text="Add Subdivision",command=self.add_subdivision_entry).pack(pady=5)
        tk.Button(self.add_add_new_country_window, text="Add Country", command=self.add_country).pack(pady=5)


    def add_add_subdivision_entry(self):
        entry_subdivision_frame = tk.Frame(self.subdivision_frame) #Creates a new entry frame for a subdivision
        entry_subdivision_frame.pack(pady=5)

        tk.Label(entry_frame, text="Subdivision:").pack(side=tk.LEFT)
        name_entry = tk.Entry(entry_frame, width=20)
        name_entry.pack(side=tk.LEFT)
        tk.Label(entry_frame, text="Population:").pack(side=tk.LEFT)
        population_entry = tk.Entry(entry_frame, width=10)
        population_entry.pack(side=tk.LEFT)
        tk.Label(entry_frame, text="Area:").pack(side=tk.LEFT)
        area_entry = tk.Entry(entry_frame, width=10)
        area_entry.pack(side=tk.LEFT)

        self.subdivision_entries.append((name_entry, population_entry, area_entry)) #Adds the new subdivision to the list



        root = tk.TK
        window = GUI(root, countries)
        root.mainloop()
