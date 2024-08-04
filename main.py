from Country_data import Country, Subdivision
from Countries_info import countries

def main():
    class Crud:
        def __init__(self):
            self.countries = []  # Start with an empty list to keep track of countries

        def create_country(self, name, population, capital, area):
            # Create a new Country instance and add it to our list
            new_country = Country(name, population, capital, area)
            self.countries.append(new_country)
            return new_country

        def find_country(self, name):
            # Finds a country by its name
            for country in self.countries:
                if country.name == name:
                    return country
            return None

        def read_country(self, name):
            # Retrieves the country by name and returns its details
            country = self.find_country(name)
            if country:
                return country.output_info()
            return f"Country '{name}' not found."

        def update_country(self, name, population=None, capital=None, area=None):
            # Finds the country and updates its details
            country = self.find_country(name)
            if country:
                if population is not None:
                    # Updates the population if a new value is provided
                    try:
                        country.population = int(population)
                    except ValueError:
                        return "Population must be a number"
                if capital is not None:
                    country.capital = capital
                if area is not None:
                    # Updates the area if a new value is provided
                    try:
                        country.area = int(area)
                    except ValueError:
                        return "Area must be a number"
                return f"Country '{name}' updated."
            return f"Country '{name}' not found."

        def delete_country(self, name):
            # Finds the country and removes it from the list
            country = self.find_country(name)
            if country:
                self.countries.remove(country)
                return f"Country '{name}' deleted."
            return f"Country '{name}' not found."

        def create_subdivision(self, country_name, name, population, area, capital):
            # Find the country where we want to add the subdivision
            country = self.find_country(country_name)
            if not country:
                return f"Country '{country_name}' not found."

            # Check if the subdivision already exists within the Country
            for sub in country.subdivisions:
                if sub.name == name:
                    return f"Subdivision '{name}' already exists in {country_name}."

            # Create a new Subdivision object and add it to the country's list
            subdivision = Subdivision(name, population, capital, area)
            country.add_subdivision(subdivision)
            return f"Subdivision '{name}' created in {country_name}."

        def read_subdivision(self, country_name, name):
            # Shows the details of the subdivision
            country = self.find_country(country_name)
            if not country:
                return f"Country '{country_name}' not found."

            # Find the subdivision within the country
            for sub in country.subdivisions:
                if sub.name == name:
                    info = sub.output_info_subdivisions()
                    population = sub.calculate_population()
                    return f"{info}\nTotal population with subdivisions: {population}"

            return f"Subdivision '{name}' not found in {country_name}."

        def update_subdivision(self, country_name, name, population=None, capital=None, area=None):
            # This updates the details of an existing subdivision
            country = self.find_country(country_name)
            if not country:
                return f"Country '{country_name}' not found."

            for sub in country.subdivisions:
                if sub.name == name:
                    if population is not None:
                        # Updates the population if a new value is provided
                        try:
                            sub.population = int(population)
                        except ValueError:
                            return "Population must be a number"
                    if capital is not None:
                        sub.capital = capital
                    if area is not None:
                        # Updates the area if a new value is provided
                        try:
                            sub.area = int(area)
                        except ValueError:
                            return "Area must be a number"
                    return f"Subdivision '{name}' updated in {country_name}."

            return f"Subdivision '{name}' not found in {country_name}."

        def delete_subdivision(self, country_name, name):
            # Removes the subdivision from the country
            country = self.find_country(country_name)
            if not country:
                return f"Country '{country_name}' not found."
            for sub in country.subdivisions:
                if sub.name == name:
                    country.subdivisions.remove(sub)
                    return f"Subdivision '{name}' deleted from {country_name}."

            return f"Subdivision '{name}' not found in {country_name}."

        def load_data(self, data):
            # Loads existing data to create the countries and subdivisions
            for entry in data:
                try:
                    self.create_country(entry["Country"], entry["Population"], entry["Capital"], entry["Area"])
                    for subdivision in entry["Subdivisions"]:
                        self.create_subdivision(entry["Country"], subdivision["Name"], subdivision["Population"], subdivision["Area"], subdivision["Capital"])
                except ValueError as e:
                    print(f"Error loading data: {e}")


    crud = Crud()

    # Load initial data
    crud.load_data(countries)

    # Try creating a new country (this will be ignored if it already exists)
    print(crud.create_country("Germany", 83251296, "Berlin", 357580))

    # Read information about existing countries and subdivisions
    print(crud.read_country("Germany"))
    print(crud.read_subdivision("Germany", "Hamburg"))

    # Update details for a country
    print(crud.update_country("Germany", population=85000000))

    # Update details for a subdivision
    print(crud.update_subdivision("Germany", "Hamburg", population=3600000))

    # Delete a subdivision
    print(crud.delete_subdivision("Germany", "Hamburg"))

    # Delete a country
    print(crud.delete_country("France"))

    # Check if the country and subdivision were deleted successfully
    print(crud.read_country("France"))  # Should indicate the country is not found
    print(crud.read_subdivision("Germany", "Hamburg"))  # Should indicate the subdivision is not found

    def print_menu():
        # Creates a Menu to choose from 9 Options
        print("\nMenu For Country and Subdivision:")
        print("1. Create Country")
        print("2. Read Country")
        print("3. Update Country")
        print("4. Delete Country")
        print("5. Create Subdivision")
        print("6. Read Subdivision")
        print("7. Update Subdivision")
        print("8. Delete Subdivision")
        print("9. Exit")
        print("----------------------------")

    while True:
        # Loop for the main menu
        print_menu()  # Prints the menu options for the user

        choice = input("Choose an option: ")  # Ask the User for a choice

        if choice == "1":  # Creates a New Country
            name = input("Country name: ")
            population = int(input("Population: "))
            capital = input("Capital: ")
            area = int(input("Area in sq km: "))
            print(crud.create_country(name, population, capital, area))

        elif choice == "2":  # Reads the Country details
            name = input("Country name: ")
            print(crud.read_country(name))

        elif choice == "3":  # Updates the information from the country
            name = input("Country name: ")
            population = int("New population: ")
            capital = input("New capital: ")
            area = input("New area: ")
            population = int(population) if population else None
            capital = capital if capital else None
            area = float(area) if area else None
            print(crud.update_country(name, population, capital, area))

        elif choice == "4":  # Deletes a Country
            name = input("Country name: ")
            print(crud.delete_country(name))

        elif choice == "5":  # Creates a new subdivision
            country_name = input("Country name: ")
            name = input("Subdivision name: ")
            population = int(input("Population: "))
            area = float(input("Area in sq km: "))
            capital = input("Capital: ")
            print(crud.create_subdivision(country_name, name, population, area, capital))

        elif choice == "6":  # Gives the option to read the subdivision details
            country_name = input("Country name: ")
            name = input("Subdivision name: ")
            print(crud.read_subdivision(country_name, name))

        elif choice == "7":  # Option to update the information from the subdivision
            country_name = input("Country name: ")
            name = input("Subdivision name: ")
            population = int("New population: ")
            capital = input("New capital: ")
            area = input("New area: ")
            population = int(population) if population else None
            capital = capital if capital else None
            area = float(area) if area else None
            print(crud.update_subdivision(country_name, name, population, capital, area))

        elif choice == "8":  # Deletes the subdivision
            country_name = int("Country name: ")
            name = input("Subdivision name: ")
            print(crud.delete_subdivision(country_name, name))

        elif choice == "9":  # Exits the program
            print("End Program.")
            break

        else:
            print("Try again.")

if __name__ == "__main__":
    main()
