from Country_data import Country, Subdivision


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
        for country in self.countries:
            if country.name == name:
                return country
        return None

    def read_country(self, name):
        # Retrieve the country by name and return its details
        country = self.find_country(name)
        if country:
            return country.output_info()
        return f"Country '{name}' not found."

    def update_country(self, name, population=None, capital=None, area=None):
        # Find the country and update its details
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
        # Find the country and remove it from the list
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

        # Check if the subdivision already exists
        for sub in country.subdivisions:
            if sub.name == name:
                return f"Subdivision '{name}' already exists in {country_name}."

        # Create a new Subdivision object and add it to the country's list
        subdivision = Subdivision(name, population, capital, area)
        country.add_subdivision(subdivision)
        return f"Subdivision '{name}' created in {country_name}."

    def read_subdivision(self, country_name, name):
        # Find the country first
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
        # Find the country first
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
        # Find the country first
        country = self.find_country(country_name)
        if not country:
            return f"Country '{country_name}' not found."

        # Find and remove the subdivision
        for sub in country.subdivisions:
            if sub.name == name:
                country.subdivisions.remove(sub)
                return f"Subdivision '{name}' deleted from {country_name}."

        return f"Subdivision '{name}' not found in {country_name}."
