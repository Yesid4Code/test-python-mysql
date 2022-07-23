"""
  2) teniendo en cuenta el punto 1, cree una función que permita
  consultar las sucursales por su id, debe hacerse el mismo procedimiento
  que se realizó en el punto 1, pero, utilizando la función creada
"""
from data import Data


def get_branche(id: int) -> dict:
  """Function that gets the information of a branch"""
  return (Data().get_branches()[id])


companies = Data.get_companies()


for companie in companies:
    branches_name = []
    for branch in companie["branches"]:  # Get branches of each companie
        branches_name.append(get_branche(branch - 1))

    companie["branches_name"] = branches_name

print(companies)
