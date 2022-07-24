"""
  8) realice una consulta al archivo data.py, muestre los items que si
  tienen colores, ordenelos por nombre y dentro de cada item agregue el
  color correspondiente
"""
from data import Data


def myFunc(e):
    """Function that return 'name' as the value"""
    return e["name"]


def sortItemsByName(colorItems):
    return colorItems.sort(key=myFunc)  # sorted by name


def getColorName(colorCode: str) -> str:
    colors = Data.get_colors()
    for color in colors:
        if color["colorCode"] == colorCode:
            return color["colorName"]


if __name__ == "__main__":
    items = Data.get_items()
    colorItems = []
    for item in items:
        if item["color"]:
            item["colorName"] = getColorName(item["color"])
            colorItems.append(item)

    sortItemsByName(colorItems)

    print(colorItems)
