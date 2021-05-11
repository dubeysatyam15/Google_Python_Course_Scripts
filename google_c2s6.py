#!/usr/bin/env python3
import csv

# Usinf DictReader() function to read a csv file using csv module
f = open('software.csv')
csv_dict_read = csv.DictReader(f)
for row in csv_dict_read:
    print(("{} software is used for {}").format(row["name"], row["use"]))
f.close()
