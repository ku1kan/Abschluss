class Country:
    def __init__(self, name, population, capital, area):
        self.name = name
        self.population = population
        self.capital = capital
        self.area = area
        self.subdivisions = []  # A List that stores the subdivisions

    def add_subdivision(self, subdivision):
        if isinstance(subdivision, Country):
            self.subdivisions.append(subdivision)
        else:
            raise TypeError("Subdivision must be a Country instance")

    def calculate_population(self):  # Calculate the total population of the country and its subdivisions
        population = self.population
        for subdivision in self.subdivisions:
            population += subdivision.calculate_population()
        return population

    def output_info(self):
        print(f"Country: {self.name}")
        print(f"Population: {self.population}")
        print(f"Capital: {self.capital}")
        print(f"Area: {self.area}")

        if self.subdivisions: #prints subdivisons information if avaiable
            print("Subdivisions:")
            for subdivision in self.subdivisions:
                print(f"\t{subdivision.name}: Population - {subdivision.population}, Area - {subdivision.area}")

