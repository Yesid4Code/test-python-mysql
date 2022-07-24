"""
  5) ordenar los terceros que se tienen en el archivo data.py por nombre y 
  agregar dentro de cada tercero una propiedad que muestre la compañia a la que pertenece
"""
from data import Data


thirds = Data.get_thirds()


def myFunc(e):
    """Function that return 'tradename' as the value"""
    return e["tradename"]


def sortThirdsByName(thirds):
    for third in thirds:
        if third["tradename"] == "":
            third["tradename"] = third["firstname"] + " " + third["lastname"] + " " + third["maidenname"]
    return thirds.sort(key=myFunc)  # sorted by tradename


if __name__ == "__main__":
    sortThirdsByName(thirds)
    for third in thirds:
        third["companyInfo"] = Data.get_companies()[third["companyid"] - 1]
    print(thirds)
