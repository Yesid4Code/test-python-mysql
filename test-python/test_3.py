"""
  3) ordenar los terceros que se tienen en el archivo data.py
  por nombre, para obtener el nombre correcto se debe tener en
  cuenta la siguiente validación:

  si el tercero tiene un (tradename != '') entonces se muestra este valor,
  en caso contrario se debe obtener concatenando los siguientes
  campos: (firstname, lastname, maidenname) en el orden dado
"""
from data import Data

thirds = Data.get_thirds()

for third in thirds:
    if third["tradename"] == "":
        name = third["firstname"] + " " + \
            third["lastname"] + " " + third["maidenname"]
        third["tradename"] = name


def myFunc(e):
    """Function that return 'tradename' as the value"""
    return e["tradename"]


def print_trade(thirds):
    for third in thirds:
        print("tradename: ", third["tradename"])


print_trade(thirds)
thirds.sort(key=myFunc)  # sorted by tradename
print("--------------- Sorted ---------------")
print_trade(thirds)
