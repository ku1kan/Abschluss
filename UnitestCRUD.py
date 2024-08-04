import unittest
from CRUD_functions import Crud


class TestCountryCrud(unittest.TestCase):
    def setUp(self):
        self.crud = Crud()  # Fresh instance of CRUD for each test, to avoid the possibility of cross-test pollution

    def test_create_country(self):
        self.crud.create_country("Germany", 83000000, "Berlin", 357022.)  # Creates Germany

        country = next((c for c in self.crud.countries if c.name == "Germany"),
                       None)  # Checks for the Country in the List

        self.assertIsNotNone(country, "Failed to create country.")
        self.assertEqual(country.name, "Germany")
        self.assertEqual(country.population, 83000000)
        self.assertEqual(country.capital, "Berlin")
        self.assertEqual(country.area, 357022)

    def test_create_subdivision(self):
        # Test case for creating a new subdivision
        self.crud.create_country("Germany", 83000000, "Berlin", 357022)  # Make sure that Germany exists

        result = self.crud.create_subdivision("Germany", "Hamburg", 1800000, 755, "Hamburg")
        self.assertEqual(result,
                         "Subdivision 'Hamburg' created in Germany.")  # Looks if the subdivision has been created

        country = next((c for c in self.crud.countries if c.name == "Germany"),
                       None)  # Gets the Country and checks/verifies if the subdivision is included
        self.assertIsNotNone(country, "Country 'Germany' not found.")

        # Checks if the subdivisions has been added to the country's subdivision
        subdivision = next((s for s in country.subdivisions if s.name == "Hamburg"), None)
        self.assertIsNotNone(subdivision, "Subdivision 'Hamburg' not found.")

    def test_delete_country(self):
        # Test case/country for deleting a country
        self.crud.create_country("France", 65000000, "Paris", 551695)
        result = self.crud.delete_country("France")
        self.assertEqual(result, "Country 'France' deleted.")

        # Verify that the country has been removed
        country = next((c for c in self.crud.countries if c.name == "France"), None)
        self.assertIsNone(country, "Country 'France' was not deleted.")

    def test_delete_subdivision(self):
        # Creates Country/Subdivision
        self.crud.create_country("Germany", 83000000, "Berlin", 357022)
        self.crud.create_subdivision("Germany", "Hamburg", 1800000, 755, "Hamburg")

        # Checks if the Subdivisions has been deleted
        result = self.crud.delete_subdivision("Germany", "Hamburg")
        self.assertEqual(result, "Subdivision 'Hamburg' deleted from Germany.")

        # Gets the Country and makes sure that the subdivision has been deleted
        country = next((c for c in self.crud.countries if c.name == "Germany"), None)
        self.assertIsNotNone(country, "Country 'Germany' not found.")
        subdivision = next((s for s in country.subdivisions if s.name == "Hamburg"), None)
        self.assertIsNone(subdivision, "Subdivision 'Hamburg' was not deleted.")

    def test_read_after_deletion(self):
        # Test case for reading a country after it has been deleted
        self.crud.create_country("France", 65000000, "Paris", 551695)
        self.crud.create_subdivision("France", "Paris", 2148000, 105, "Paris")
        self.crud.delete_country("France")

        # Tries to read the deleted country
        country = self.crud.read_country("France")  # Tries to read the deleted country
        self.assertEqual(country, "Country 'France' not found.")
        # Tries to read the subdivision from the list
        subdivision = self.crud.read_subdivision("France", "Paris")
        self.assertEqual(subdivision, "Country 'France' not found.")

    def test_update_country(self):
        # Test case/country for updating a country
        self.crud.create_country("Germany", 83000000, "Berlin", 357022)  # Creates Germany with its information

        # Population gets updated and makes sure that everything is unchanged
        result = self.crud.update_country("Germany", population=84000000, capital="Berlin", area=357022)

        self.assertEqual(result, "Country 'Germany' updated.")

        # Makes Sure that everything have been updated
        country = next((c for c in self.crud.countries if c.name == "Germany"), None)
        self.assertIsNotNone(country, "Country 'Germany' not found.")
        self.assertEqual(country.population, 84000000)
        self.assertEqual(country.capital, "Berlin")
        self.assertEqual(country.area, 357022)

    def test_update_subdivision(self):
        # Creates Country and Subdivision
        self.crud.create_country("Germany", 83000000, "Berlin", 357022)
        self.crud.create_subdivision("Germany", "Hamburg", 1800000, 755, "Hamburg")

        # Updates population of the subdivision
        result = self.crud.update_subdivision("Germany", "Hamburg", population=1900000, area=760)

        self.assertEqual(result, "Subdivision 'Hamburg' updated in Germany.")

        # Gets the information and makes sure that the information of the subdivisions have been updated
        country = next((c for c in self.crud.countries if c.name == "Germany"), None)
        self.assertIsNotNone(country, "Country 'Germany' not found.")
        subdivision = next((s for s in country.subdivisions if s.name == "Hamburg"), None)
        self.assertIsNotNone(subdivision, "Subdivision 'Hamburg' not found.")
        self.assertEqual(subdivision.population, 1900000)  # Population should be updated
        self.assertEqual(subdivision.area, 760)  # Should update the area


if __name__ == "__main__":
    unittest.main()  # Runs all the test cases for the CRUD functions
