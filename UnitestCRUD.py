import unittest
from CRUD_functions import Crud




class TestCountryCrud(unittest.TestCase):
    def setUp(self):
        self.crud = Crud() # Set up a new Crud instance before each test


    def test_create_country(self):
        # Test case for creating a new country
        self.crud.create_country("Germany", 83000000, "Berlin", 357022)
        country = next((c for c in self.crud.countries if c.name == "Germany"), None)
        self.assertIsNotNone(country, "Failed to create country.")
        self.assertEqual(country.name, "Germany")
        self.assertEqual(country.population, 83000000)
        self.assertEqual(country.capital, "Berlin")
        self.assertEqual(country.area, 357022)

    def test_create_subdivision(self):
        # Test case for creating a new subdivision
        self.crud.create_country("Germany", 83000000, "Berlin", 357022)
        result = self.crud.create_subdivision("Germany", "Hamburg", 1800000, 755, "Hamburg")
        self.assertEqual(result, "Subdivision 'Hamburg' created in Germany.")
        country = next((c for c in self.crud.countries if c.name == "Germany"), None)
        self.assertIsNotNone(country, "Country 'Germany' not found.")
        subdivision = next((s for s in country.subdivisions if s.name == "Hamburg"), None)
        self.assertIsNotNone(subdivision, "Subdivision 'Hamburg' not found.")




if __name__ == "__main__":
    unittest.main()
