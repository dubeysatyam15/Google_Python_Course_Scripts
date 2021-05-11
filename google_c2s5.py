#!/usr/bin/env python3
import csv

''' We are going to make a new csv file from the script and
write into it using the writer() and writer.writerows() function
in csv module '''

admin_ip = [["localhost.local", "127.0.0.0"], ["mylinuxhost.local", "192.168.134.5"]]
with open("ipaddr.csv", "w") as file_write:
    csv_write = csv.writer(file_write)
    csv_write.writerows(admin_ip)
