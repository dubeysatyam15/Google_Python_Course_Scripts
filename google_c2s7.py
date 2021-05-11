#!/usr/bin/env python3
import csv

# Importing DictWriter() to write into a new csv file from a list of dictionaries
users = [{"name": "Satyam Dubey", "username": "sam", "department": "IT infrastructure"},
        {"name": "Rupesh Sharma", "username": "Rup", "department": "User Experience Research"},
        {"name": "Santosh Pandey", "username": "Sant", "department": "Development"},
        {"name": "Sonali Kumari", "username": "sona", "department": "Marketing"}]

keys = ["name", "username", "department"]

with open("employee.csv", "w") as employee:
    emp_read = csv.DictWriter(employee, fieldnames=keys)
    emp_read.writeheader()
    emp_read.writerows(users)
