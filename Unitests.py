import unittest
from Country_data import Country, Subdivision
from Countries_info import countries


class TestCountryAndSubdivision(unittest.TestCase):

    def setUp(self):
        # Initialize with the first country in the provided data
        data = countries[0]

        # Create a Country object with its attributes
        self.country = Country(
            name=data["Country"],
            population=data["Population"],
            capital=data["Capital"],
            area=data["Area"]
        )

        # Add subdivisions to the country
        for subdivision_data in data["Subdivisions"]:
            subdivision = Subdivision(
                name=subdivision_data["Name"],
                population=subdivision_data["Population"],
                capital=subdivision_data["Capital"],
                area=subdivision_data["Area"]
            )
            self.country.add_subdivision(subdivision)


if __name__ == '__main__':
    unittest.main()

