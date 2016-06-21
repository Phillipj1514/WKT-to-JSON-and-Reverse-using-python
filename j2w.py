#!/usr/bin/python

import csv
import sys
import shapely
import shapely.wkt
import geojson
import json
from shapely.geometry import shape
import os

# change the file name 
inputFileName = "out(json).csv"
outputFileName = os.path.splitext(inputFileName)[0] + "_in.csv"

with open(inputFileName, 'rb') as inFile, open(outputFileName, 'wb') as outfile:
    r = csv.reader(inFile)
    w = csv.writer(outfile)

    next(r, None)  
    w.writerow(['WKT','AREA','PERIMETER','COMMNAME','COMMNO','COMM_CODE','OID_','ParCode','ParName','Quintile','Decile1','Decile2','Decile3','Decile4','Decile5','Decile6','Decile7','Decile8','Decile9','Decile10','Decile1to3','Decile8to1','Decile9to1','QuinL','QuinU','QuinDec9to']) 
    for row in r:
        w.writerow(row)
    	
# continue on with changing it to json

csv.field_size_limit(sys.maxsize)

csvfile = open('out(json)_in.csv', 'rb')
reader = csv.DictReader(csvfile)
c = csv.DictWriter(open("out(wkt).csv", "wb"), fieldnames=reader.fieldnames)
c.writeheader()

for row in reader:
    for col in row:
        if col == 'WKT':
            d_js = row['WKT']
            c1 = geojson.loads(d_js)
            c2 = shape(c1)
            row['WKT'] = c2.wkt  
    c.writerow(row)
# delete unwanted file
help= "out(json)_in.csv"
if os.path.exists(help):
    os.remove(help)
    
   