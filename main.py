from CRUD_functions import Crud
from Countries_info import countries



def main():
    crud = Crud()
    crud.load_data(countries)

    # Creating a new country for test
    crud.create_country("Germany", 83251296, "Berlin", 357580)

    # Creating and testing a new Country and subdivions for test
    crud.read_country("Germany")
    crud.read_subdivision("Germany", "Hamburg")

    # Updating a country for test
    crud.update_country("Germany", population=85000000)

    # Updating a subdivision for test
    crud.update_subdivision("Germany", "Hamburg", population=3600000)

    # Deleting a subdivison for test
    crud.delete_subdivision("Germany", "Hamburg")

    # Deleting a country for test
    crud.delete_country("France")

    # Reading a country after deleting it for test
    crud.read_country("France")  # Should not find the country
    crud.read_subdivision("Germany", "Hamburg")  # Should not find the subdivision

if __name__ == "__main__":
    main()
