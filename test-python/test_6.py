"""
  6) ordernar las compañias por nombre y dentro de cada compañia, crear un objecto 
  llamado thirds el cual va a terner todos los terceros que pertenezcan a esa compañia
"""
from data import Data
#from test_5 import thirds, sortThirdsByName


def myFunc(e):
    """Function that return 'tradename' as the value"""
    return e["name"]


def sortCompaniesByName(thirds):
    return thirds.sort(key=myFunc)  # sorted by tradename


def appendCompaniesThirds(companies):
    for companie in companies:
        thirds = []
        for third in Data.get_thirds():
            if companie["id"] == third["companyid"]:
                thirds.append(third)

        companie["thirds"] = thirds


if __name__ == "__main__":
    companies = Data.get_companies()
    sortCompaniesByName(companies)
    appendCompaniesThirds(companies)
    print(companies)
