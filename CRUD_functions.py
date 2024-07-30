from Country_data import Country, Subdivision
from Countries_info import countries


class Crud:
    def __init__(self):
        self.countries = []  # Start with an empty list to keep track of countries

    def create_country(self, name, population, capital, area):
        # Create a new Country instance and add it to our list
        new_country = Country(name, population, capital, area)
        self.countries.append(new_country)
        return new_country

    def find_country(self, name):
        # Find a country by its name
        return next((c for c in self.countries if c.name == name), None)

    def read_country(self, name):
        # Retrieve the country by name and print its details
        country = self.find_country(name)
        if country:
            return country.output_info()
        else:
            print(f"Country '{name}' not found.")

    def update_country(self, name, **kwargs):
        # Find the country and update its details
        country = self.find_country(name)
        if country:
            for key, value in kwargs.items():
                if key == "population":
                    try:
                        country.population = int(value)
                    except ValueError as e:
                        print(f"Error updating population for '{name}': {e}")
                        return
                elif key == "capital":
                    country.capital = value
                elif key == "area":
                    try:
                        country.area = int(value)
                    except ValueError as e:
                        print(f"Error updating area for '{name}': {e}")
                        return
            print(f"Country '{name}' updated.")
        else:
            print(f"Country '{name}' not found.")

    def delete_country(self, name):
        # Find the country and remove it from the list
        country = self.find_country(name)
        if country:
            self.countries.remove(country)
            print(f"Country '{name}' deleted.")
        else:
            print(f"Country '{name}' not found.")

    def create_subdivision(self, country_name, name, population, area, capital):
        # Find the country where we want to add the subdivision
        country = self.find_country(country_name)
        if not country:
            print(f"Country '{country_name}' not found.")
            return

        # Check if the subdivision already exists
        if any(sub.name == name for sub in country.subdivisions):
            print(f"Subdivision '{name}' already exists in {country_name}.")
            return

        try:
            # Create a new Subdivision object and add it to the country's list
            subdivision = Subdivision(name, int(population), capital, int(area))
            country.add_subdivision(subdivision)
            print(f"Subdivision '{name}' created in {country_name}.")
        except ValueError as e:
            print(f"Error creating subdivision '{name}' in {country_name}: {e}")

    def read_subdivision(self, country_name, name):
        # Find the country first
        country = self.find_country(country_name)
        if not country:
            print(f"Country '{country_name}' not found.")
            return

        # Find the subdivision within the country
        subdivision = next((sub for sub in country.subdivisions if sub.name == name), None)
        if subdivision:
            subdivision.output_info_subdivisions()
            print(f"Total population with subdivisions: {subdivision.calculate_population()}\n")
        else:
            print(f"Subdivision '{name}' not found in {country_name}.")

    def update_subdivision(self, country_name, name, **kwargs):
        # Find the country first
        country = self.find_country(country_name)
        if not country:
            print(f"Country '{country_name}' not found.")
            return

        # Find the subdivision within the country
        subdivision = next((sub for sub in country.subdivisions if sub.name == name), None)
        if subdivision:
            # Update subdivision details if provided
            for key, value in kwargs.items():
                if key == "population":
                    try:
                        subdivision.population = int(value)
                    except ValueError as e:
                        print(f"Error updating population for '{name}' in {country_name}: {e}")
                        return
                elif key == "capital":
                    subdivision.capital = value
                elif key == "area":
                    try:
                        subdivision.area = int(value)
                    except ValueError as e:
                        print(f"Error updating area for '{name}' in {country_name}: {e}")
                        return
            print(f"Subdivision '{name}' updated in {country_name}.")
        else:
            print(f"Subdivision '{name}' not found in {country_name}.")

    def delete_subdivision(self, country_name, name):
        # Find the country first
        country = self.find_country(country_name)
        if not country:
            print(f"Country '{country_name}' not found.")
            return

        # Find and remove the subdivision
        subdivision = next((sub for sub in country.subdivisions if sub.name == name), None)
        if subdivision:
            country.subdivisions.remove(subdivision)
            print(f"Subdivision '{name}' deleted from {country_name}.")
        else:
            print(f"Subdivision '{name}' not found in {country_name}.")


