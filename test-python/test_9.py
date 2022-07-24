"""
9) realice una consulta al archivo data.py, muestre todos los items, 
  ordenelos por nombre y dentro de cada item agregue el color correspondiente,
  en caso de que esté lo tenga. 
  
  El resultado del ordenando debe ser así, en la parte inicial los items 
  que no tienen color y en la parte final los que si tienen color, todo dentro de
  un mismo objeto
"""
from data import Data
from test_8 import sortItemsByName, getColorName


if __name__ == "__main__":
    items = Data.get_items()

    colorlessItems = []
    colorItems = []
    for item in items:
        if item["color"] == None:
            colorlessItems.append(item)
        else:
            item["colorName"] = getColorName(item["color"])
            colorItems.append(item)

    sortItems = []
    sortItemsByName(colorlessItems)
    sortItemsByName(colorItems)
    sortItems.append(colorlessItems)
    sortItems.append(colorItems)

    print(sortItems)
