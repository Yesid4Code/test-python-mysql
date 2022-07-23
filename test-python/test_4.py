"""
  4) ordenar los terceros que se tienen en el archivo data.py por identificationNumber
"""
from data import Data


thirds = Data.get_thirds()


def myFunc(e):
    """Function that return 'tradename' as the value"""
    return e["identificationNumber"]


def print_identificationNumber(thirds):
    for third in thirds:
        print("tradename: ", third["identificationNumber"])


print_identificationNumber(thirds)

thirds.sort(key=myFunc)  # sorted by identificationNumber

print("--------------- Sorted ---------------")
print_identificationNumber(thirds)
