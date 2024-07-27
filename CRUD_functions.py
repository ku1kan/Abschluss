class Crud:
    def __init__(self):
        self.countries = []  #AN empty list that stores the countries

    def create_country(self, name, population, capital, area): #Creates a new country instance and adds it to the list
        new_country = Country(name, population, capital, area)
        self.countries.append(new_country)
        return new_country

    def read_country(self, country):
        if isinstance(country, Country):
            return country.output_info()
        else:
            raise TypeError("Expected a Country instance")

    def update_country(self, country, name=None, population=None, capital=None, area=None):
        if isinstance(country, Country): #Check if the provided object is an instance of Country
            if name is not None:
                country.name = name
            if population is not None:
                country.population = population
            if capital is not None:
                country.capital = capital
            if area is not None:
                country.area = area
        else:
            raise TypeError("Expected a Country instance") #Raises an error if the object is not a country instance

    def delete_country(self, country):CRUD
        if isinstance(country, Country):
            self.countries.remove(country)