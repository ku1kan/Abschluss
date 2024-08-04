import unittest
import io
import sys
from Country_data import Country, Subdivision
from Countries_info import countries


class TestCountryAndSubdivision(unittest.TestCase):

    def setUp(self):
        data = countries[0]  # Uses the information from the first country

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

    def test_country(self):
        data = countries[0]

        # Checks the expected Value of the given Attributes (country,population,Capital,Area,subdivision)
        self.assertEqual(self.country.name, data["Country"])
        self.assertEqual(self.country.population, data["Population"])
        self.assertEqual(self.country.capital, data["Capital"])
        self.assertEqual(self.country.area, data["Area"])
        self.assertEqual(len(self.country.subdivisions), len(data["Subdivisions"]))

    def test_subdivision(self):
        data = countries[0]
        # Checks if the Subdivision attributes match the expected values
        for i, subdivision_data in enumerate(data["Subdivisions"]):
            subdivision = self.country.subdivisions[i]
            self.assertEqual(subdivision.name, subdivision_data["Name"])
            self.assertEqual(subdivision.population, subdivision_data["Population"])
            self.assertEqual(subdivision.capital, subdivision_data["Capital"])
            self.assertEqual(subdivision.area, subdivision_data["Area"])

    def test_add_subdivision(self):  # Verifies that adding a new subdivision updates the list correct
        new_subdivision = Subdivision(
            name="New Region",
            population=500000,
            capital="New City",
            area=576
        )
        # Should increase the total number of subdivision by 1
        self.country.add_subdivision(new_subdivision)
        self.assertEqual(len(self.country.subdivisions), len(countries[0]["Subdivisions"]) + 1)

    def test_calculate_population(self):
        # Checks if the total calculation is correct
        data = countries[0]
        total_population = data["Population"] + sum(
            sub["Population"] for sub in data["Subdivisions"])
        self.assertEqual(self.country.calculate_population(), total_population)

    def test_output_info(self):
        captured_output = io.StringIO()  # Gets the output of the country and prints it as a stdout
        sys.stdout = captured_output  # Goes from stdout to StringIO to capture the correct statement

        self.country.output_info()  # Prints the country information

        sys.stdout = sys.__stdout__  # Resets the stdout to its Original state
        output = captured_output.getvalue()  # Shows the output

        # Checks if the output has the correct information
        self.assertIn(f"Country: {self.country.name}", output)
        self.assertIn(f"Population: {self.country.population}", output)
        self.assertIn(f"Capital: {self.country.capital}", output)
        self.assertIn(f"Area: {self.country.area}", output)
        self.assertIn("Subdivisions:", output)

        # Makes sure that each subdivision detail is included in the output
        for subdivision in self.country.subdivisions:
            self.assertIn(f"Subdivision: {subdivision.name}", output)
            self.assertIn(f"Population: {subdivision.population}", output)
            self.assertIn(f"Capital: {subdivision.capital}", output)
            self.assertIn(f"Area: {subdivision.area}", output)

    def test_invalid_population_and_area(self):
        # Raises ValueError for invalid negative  population and area
        with self.assertRaises(ValueError):
            Country("Test-Land", -1, "Test City", 500000.0)
        with self.assertRaises(ValueError):
            Subdivision("Test-Region", 200000, "Test-City", -1)

    def test_add_invalid_subdivision(self):
        # Ensure adding a non-Subdivision object raises TypeError
        with self.assertRaises(TypeError):
            self.country.add_subdivision("Not a Subdivision")

    def test_multiple_countries(self):
        # Check if the calculation for multiple countries is correct
        for country_data in countries:
            country = Country(
                name=country_data["Country"],
                population=country_data["Population"],
                capital=country_data["Capital"],
                area=country_data["Area"]
            )
            for subdivision_data in country_data["Subdivisions"]:
                subdivision = Subdivision(
                    name=subdivision_data["Name"],
                    population=subdivision_data["Population"],
                    capital=subdivision_data["Capital"],
                    area=subdivision_data["Area"]
                )
                country.add_subdivision(subdivision)
            self.assertEqual(country.calculate_population(), country_data["Population"] +
                             sum(sub["Population"] for sub in country_data["Subdivisions"]))


if __name__ == '__main__':
    unittest.main()
