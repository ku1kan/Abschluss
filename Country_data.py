from Countries_info import countries


class Country:
    def __init__(self, name, population, capital, area):
        if population < 0 or area < 0:
            raise ValueError("Population and area must be non-negative")
        self.name = name
        self.population = population
        self.capital = capital
        self.area = area
        self.subdivisions = []  # A list to store subdivisions

    def add_subdivision(self, subdivision):
        # Ensure the subdivision is of the correct type.
        if not isinstance(subdivision, Subdivision):
            raise TypeError("Subdivision must be a Subdivision instance")
        # Add the subdivision to the list.
        self.subdivisions.append(subdivision)
        print(f"Added subdivision: {subdivision.name}")  # Just a check to ensure it's added correctly.

    def calculate_population(self):  # Calculate the total population of the country and its subdivisions
        # Start with the country's population.
        total_population = self.population
        for subdivision in self.subdivisions:
            total_population += subdivision.calculate_population() # Iterate over the subdivisions and add their
            # populations to the total
        return total_population # Return the total population.

    def output_info(self):  # Prints the country information
        print(f"Country: {self.name}")
        print(f"Population: {self.population}")
        print(f"Capital: {self.capital}")
        print(f"Area: {self.area}")

        if self.subdivisions:  # Prints subdivisions information if available
            print("Subdivisions:")
            for subdivision in self.subdivisions:
                subdivision.output_info_subdivisions()


class Subdivision:
    def __init__(self, name, population, capital, area):
        if population < 0 or area < 0:
            raise ValueError("Population and area must be non-negative")
        self.name = name
        self.population = population
        self.capital = capital
        self.area = area
        self.subdivisions = []  # This stores the smaller subdivisions

    def add_subdivision(self, subdivision):
        # Ensure the subdivision is of the correct type.
        if not isinstance(subdivision, Subdivision):
            raise TypeError("Subdivision must be a Subdivision instance")
        # Add the subdivision to the list.
        self.subdivisions.append(subdivision)
        print(f"Added subdivision: {subdivision.name}")  # Just a check to ensure it's added correctly.

    def calculate_population(self):  # Calculate the total population of the subdivision and its smaller subdivisions
        population = self.population
        for subdivision in self.subdivisions:
            population += subdivision.calculate_population()
        return population

    def output_info_subdivisions(self):  # Displays the Information for the Subdivisions
        print(f"Subdivision: {self.name}")
        print(f"Population: {self.population}")
        print(f"Capital: {self.capital}")
        print(f"Area: {self.area}")

        if self.subdivisions:
            print("Smaller-Subdivisions:")
            for subdivision in self.subdivisions:
                print(f"\t{subdivision.name}: Population - {subdivision.population}, Area - {subdivision.area}")


# Create a Country object from the provided data
def calculate_whole_population(info):
    # Initialize/ Create a new Country with main attributes
    country = Country(
        info["Country"],
        info["Population"],
        info["Capital"],
        info["Area"]
    )
    # Add subdivisions to the country.
    for subdivision_data in info["Subdivisions"]:
        country.add_subdivision(
            Subdivision(
                subdivision_data["Name"],
                subdivision_data["Population"],
                subdivision_data["Capital"],
                subdivision_data["Area"]
            )
        )
    # Return the populated country object.
    return country


# Generate a list of Country objects from the data
countries_info = [calculate_whole_population(info) for info in countries]

# Print information and total population for each country
for country in countries_info:
    country.output_info()
    print(f"Total population with the subdivisions: {country.calculate_population()}\n")
