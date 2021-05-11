#!/usr/bin/env python3

import csv
# Usinf csv module to read a csv file and print it

filename = input("Enter the file name:")
f = open(filename)
csv_read = csv.reader(f)
for row in csv_read:
    name, phone, role = row
    print("Name: {}, Phone: {}, Role: {}".format(name, phone, role))
f.close()
