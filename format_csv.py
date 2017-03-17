#-*- coding:utf-8 -*-
import csv

with open("dump.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)