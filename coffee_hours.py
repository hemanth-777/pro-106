import csv
import numpy as np


def getDataSource(data_path):
    coffee_in_percentage = []
    hours_of_sleep = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            coffee_in_percentage.append(float(row["Coffee In Percentage"]))
            hours_of_sleep.append(float(row["Hours Of Sleep"]))

    return {"x" : marks_in_percentage, "y": days_present}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between cups of coffee and hours of sleep :-  \n--->",correlation[0,1])

def setup():
    data_path  = "./cups of coffee vs hours of sleep.csv"

    datasource = getDataSource(data_path)
    findCorrelation(datasource)

setup()
