from Country_data import Country, Subdivision
from Countries_info import countries


class Crud:
    def __init__(self):
        self.countries = []  # Start with an empty list to keep track of countries

    def create_country(self, name, population, capital, area):  # Create a new Country instance and add it to our list
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
        # Retrieves the country by name and return its details
        country = self.find_country(name)
        if country:
            return country.output_info()
        return f"Country '{name}' not found."

    def update_country(self, name, population=None, capital=None, area=None):
        # Finds the country and update its details
        country = self.find_country(name)
        if country:
            if population is not None:
                country.population = population
            if capital is not None:
                country.capital = capital
            if area is not None:
                country.area = area
            return f"Country '{name}' updated."
        return f"Country '{name}' not found."

    def delete_country(self, name):
        # Finds the country and remove it from the list
        country = self.find_country(name)
        if country:
            self.countries.remove(country)
            return f"Country '{name}' deleted."
        return f"Country '{name}' not found."

    def create_subdivision(self, country_name, name, population, area,
                           capital):  # Find the country where we want to add the subdivision
        country = self.find_country(country_name)
        if not country:
            return f"Country '{country_name}' not found."

        # Check if the subdivision already exists within the Country.
        for sub in country.subdivisions:
            if sub.name == name:
                return f"Subdivision '{name}' already exists in {country_name}."

        # Create a new Subdivision object and add it to the country's list
        subdivision = Subdivision(name, population, capital, area)
        country.add_subdivision(subdivision)
        return f"Subdivision '{name}' created in {country_name}."

    def read_subdivision(self, country_name, name):  # Shows the details of the subdivision
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

        # Find the subdivision within the country
        for sub in country.subdivisions:
            if sub.name == name:
                if population is not None:
                    sub.population = population
                if capital is not None:
                    sub.capital = capital
                if area is not None:
                    sub.area = area
                return f"Subdivision '{name}' updated in {country_name}."

        return f"Subdivision '{name}' not found in {country_name}."

    def delete_subdivision(self, country_name, name):
        # Removes the subdivision from the country
        country = self.find_country(country_name)
        if not country:
            return f"Country '{country_name}' not found."

        # Find and remove the subdivision
        for sub in country.subdivisions:
            if sub.name == name:
                country.subdivisions.remove(sub)
                return f"Subdivision '{name}' deleted from {country_name}."

        return f"Subdivision '{name}' not found in {country_name}."

    def load_data(self, data):
        # Load data to create countries and subdivisions
        for entry in data:
            try:
                self.create_country(entry["Country"], entry["Population"], entry["Capital"],
                                    entry["Area"])  # Creates the country
                for subdivision in entry["Subdivisions"]:  # Adds the subdivision to the created country
                    self.create_subdivision(entry["Country"], subdivision["Name"], subdivision["Population"],
                                            subdivision["Area"],
                                            subdivision["Capital"])
            except ValueError as e:
                print(f"Error loading data: {e}")


# Example usage
if __name__ == "__main__":
    crud = Crud()  # Create an instance of the Crud class

    # Load country data
    crud.load_data(countries)

    # This creates a new country will not add if the country already exists.
    crud.create_country("Germany", 83251296, "Berlin", 357580)

    # Read information about existing countries and subdivisions
    print(crud.read_country("Germany"))
    print(crud.read_subdivision("Germany", "Hamburg"))

    # Updates the population for Germany
    print(crud.update_country("Germany", population=85000000))

    # Updates the population for Hamburg
    print(crud.update_subdivision("Germany", "Hamburg", population=3600000))

    # Deletes the Hamburg Subdivision
    print(crud.delete_subdivision("Germany", "Hamburg"))

    # Deletes France if its exists
    print(crud.delete_country("France"))

    # Check if the country and subdivision were deleted successfully
    print(crud.read_country("France"))  # Should show that France is not found
    print(crud.read_subdivision("Germany", "Hamburg"))  # Should show that Hamburg is not found
