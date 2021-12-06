import csv

def getCSVData(filename):
    #create an empty list to store tows
    rows = []

    #open the csv file
    datafile = open(filename, "r")

    #create a csv reader from csv file
    reader = csv.reader(datafile)

    # skip the header
    next(reader)

    # add rows from reader to list
    for row in reader:
        rows.append(row)
    return rows

