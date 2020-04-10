import csv
import numpy

with open('/Users/rodsim/downloads/b7d2591790c7eee6abf3842983a46d92_Download_COVID19_20200404.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

#with open ('/Users/rodsim/downloads/b7d2591790c7eee6abf3842983a46d92_Download_COVID19_20200404.csv')