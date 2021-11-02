import csv 
import numpy as np
import plotly.express as px

def getDataSource(data_path):
    icecreamsales = []
    colddrinksales = []
    with open(data_path) as csv_file:
          csv_reader = csv.DictReader(csv_file)
          for row in csv_reader:
              icecreamsales.append(float(row["Ice-cream Sales( Rs. )"]))
              colddrinksales.append(float(row["Cold drink sales( Rs. )"]))
    return {"x" : icecreamsales, "y": colddrinksales}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("the value of corrrelations is ", correlation)


def setup():
    data_path  = "C106\Ice-Cream vs Cold-Drink vs Temperature - Ice Cream Sale vs Temperature data.csv"
    datasource = getDataSource(data_path)
    findCorrelation(datasource)

setup()

#           icecream colddrink
#icecream       1       0.99
#colddrink      0.99        1