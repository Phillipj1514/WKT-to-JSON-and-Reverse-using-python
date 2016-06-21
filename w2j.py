#!/usr/bin/python

import csv
import sys
import shapely
import shapely.wkt
import geojson
import os
# change the file name 
inputFileName = "in.csv"
outputFileName = os.path.splitext(inputFileName)[0] + "_out.csv"

with open(inputFileName, 'rb') as inFile, open(outputFileName, 'wb') as outfile:
    r = csv.reader(inFile)
    w = csv.writer(outfile)

    next(r, None)  
    w.writerow(['JSON','AREA','PERIMETER','COMMNAME','COMMNO','COMM_CODE','OID_','ParCode','ParName','Quintile','Decile1','Decile2','Decile3','Decile4','Decile5','Decile6','Decile7','Decile8','Decile9','Decile10','Decile1to3','Decile8to1','Decile9to1','QuinL','QuinU','QuinDec9to']) 
    for row in r:
        w.writerow(row)
    	
# continue on with changing it to json

csv.field_size_limit(sys.maxsize)

csvfile = open('in_out.csv', 'rb')
reader = csv.DictReader(csvfile)
c = csv.DictWriter(open("out(json).csv", "wb"), fieldnames=reader.fieldnames)
c.writeheader()

for row in reader:
    for col in row:
        if col == 'JSON':
            d_wkt = row['JSON']
            js1 = shapely.wkt.loads(d_wkt)
            js2 = geojson.Feature(geometry=js1, properties={})
            row['JSON'] = js2.geometry
    c.writerow(row)
# delete unwanted file
help= "in_out.csv"
if os.path.exists(help):
    os.remove(help)
    
