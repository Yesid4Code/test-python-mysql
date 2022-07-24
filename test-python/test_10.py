"""
  10) realice una consulta al archivo data.py, muestre todos los terceros,
  reduzca la información y solo muestre el nombre y la identificación,
  ordenelos por identificación
"""
from data import Data

thirds = Data.get_thirds()

print("\n------------------------- Thirds -------------------------\n")
print(thirds)


def myFunc(e):
    """Function that return 'identificationNumber' as the value"""
    return e["identificationNumber"]


if __name__ == "__main__":
    liteThird = []
    for third in thirds:
        th = {}
        th["identificationNumber"] = third["identificationNumber"]
        th["tradename"] = third["tradename"]
        liteThird.append(th)

    liteThird.sort(key=myFunc)  # sorted by identificationNumber

    print("\n--------------------- Thirds filtered ---------------------\n")

    print(liteThird)
