"""
  1) consulte la información del archivo data.py
  cree un objeto que contenga las empresas y dentro
  las sucursales que corresponden para cada empresa
"""
from data import Data


companies = Data.get_companies()


for companie in companies:
    branches_name = []
    for branch in companie["branches"]:  # Get branches of each companie
        get_branch_name = Data().get_branches()[branch - 1]
        branches_name.append(get_branch_name)

    companie["branches_name"] = branches_name

print(companies)
