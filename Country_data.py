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
        if not isinstance(subdivision, Subdivision):
            raise TypeError("Subdivision must be a Subdivision instance")
        self.subdivisions.append(subdivision)

    def calculate_population(self):  # Calculate the total population of the country and its subdivisions
        total_population = self.population
        for subdivision in self.subdivisions:  # Iterate over the subdivisions and add their populations to the total
            total_population += subdivision.calculate_population()
        return total_population

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
        if not isinstance(subdivision, Subdivision):
            raise TypeError("Subdivision must be a Subdivision instance")
        self.subdivisions.append(subdivision)

    def calculate_population(self):  # Calculate the total population of the subdivision and its smaller subdivisions
        population = self.population
        for subdivision in self.subdivisions:
            population += subdivision.calculate_population()
        return population

    def output_info_subdivisions(self):
        print(f"Subdivision: {self.name}")
        print(f"Population: {self.population}")
        print(f"Capital: {self.capital}")
        print(f"Area: {self.area}")

        if self.subdivisions:
            print("Smaller-Subdivisions:")
            for subdivision in self.subdivisions:
                print(f"\t{subdivision.name}: Population - {subdivision.population}, Area - {subdivision.area}")

