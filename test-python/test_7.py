"""
  7) realice una consulta al archivo data.py, muestre los items que no tienen colores 
  y ordenelos por nombre
"""
from data import Data


def myFunc(e):
    """Function that return 'tradename' as the value"""
    return e["name"]


def sortItemsByName(colorlessItems):
    return colorlessItems.sort(key=myFunc)  # sorted by tradename

if __name__ == "__main__":
    items = Data.get_items()
    colorlessItems = []
    for item in items:
        if item["color"] == None:
            colorlessItems.append(item)

    sortItemsByName(colorlessItems)
    print(colorlessItems)
