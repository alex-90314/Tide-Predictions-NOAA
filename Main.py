#old method - reliant on the csv module

# import csv

# with open('Tide_Info.csv', newline='') as csvfile:
#     spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
#     for row in spamreader:
#         print(', '.join(row))

# new method - not reliant on the csv module
with open('Tide_Info.csv') as csv:
    for line in csv:
        Predict = line
        Print(f"On {Date} @ {Time} the tide will be {Predict}")