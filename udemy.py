# Import library
import csv
import os

# Sorce variables
#udemyCsv = "./resources/web_starter.csv"
udemyCsv = os.path.join(".","resources","web_starter.csv")
resultCsv = "./resources/result.csv"

# List data
title = []
subscribers = []
reviews = []
reviewsPercent = []
length = []
newRow = []

# Open file
with open(udemyCsv, "r", encoding="UTF-8") as csvFile:
    csvReader = csv.reader(csvFile, delimiter=",")

    # Read all the data and store it in the variable arrays
    for row in csvReader:
        title.append(row[1])
        subscribers.append(row[4])
        reviews.append(row[6])
        percent = round(int(row[6])/int(row[5]),2)
        reviewsPercent.append(percent)
        newLength = row[9].split(" ")
        length.append(float(newLength[0]))

roster = zip(title, subscribers, reviews, reviewsPercent, length)

# Open new file
with open(resultCsv, "w", newline="\n", encoding="UTF-8") as dataFile:
    writer = csv.writer(dataFile)
    writer.writerow(["Title","Subscribers","Reviews","RevPercent","Length"])
    writer.writerows(roster)

