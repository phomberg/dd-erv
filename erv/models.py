from django.db import models

import pyodbc
import sys
import time

server = '***'
database = '***'
username = '***'
password = '***'
driver= '{ODBC Driver 17 for SQL Server}'
conn_str = 'DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password
conn = pyodbc.connect(conn_str)
crs = conn.cursor()

def get_conn_str():
    return conn_str

def get_cursor():
    return crs

def get_article_rnd(nr_of_articles):
    sql = "SELECT TOP {0} ARTICLE FROM view_ERV_Articles ORDER BY NEWID()".format(nr_of_articles)
    
    crs.execute(sql)
    row = crs.fetchone()
    
    records = []

    while row: 
        rec = {
                "Article": row[0]
                }
        records.append(rec)
        
        row = crs.fetchone()

    return records

def get_article(product, pack_type, pack_size, units):
    sql = "SELECT BUNDLE_NAME "
    sql += "FROM view_Article "
    sql += "WHERE IS_SALES_DATA_UNIT = 1 "
    sql += "AND PRODUCT_NAME = '{0}' ".format(product)
    sql += "AND PACKAGE_TYPE_GROUP = '{0}' ".format(pack_type)
    sql += "AND CAST(UNIT_QUANTITY_LITRE * 1000 AS INT)	= {0} ".format(pack_size)
    sql += "AND SALES_UNITS = {0} ".format(units)

    
    crs.execute(sql)
    row = crs.fetchone()
    
    records = []

    while row: 
        rec = {
                "Article": row[0]
                }
        records.append(rec)
        
        row = crs.fetchone()

    return records

# Create your models here.

cust = [
            {
                "ID": 1
                ,"Name": "Restaurant XY"
                ,"Address": "Bahnhofstrasse 99"
                ,"PostalCode": 8000
                ,"City": "Zürich"
            },
            {
                "ID": 2
                ,"Name": "Pub ABC"
                ,"Address": "Hauptstrasse 1"
                ,"PostalCode": 3000
                ,"City": "Bern"
            },
            {
                "ID": 3
                ,"Name": "Take Away Q"
                ,"Address": "Seeweg 1"
                ,"PostalCode": 6000
                ,"City": "Luzern"
            },
            {
                "ID": 4
                ,"Name": "Z AG"
                ,"Address": "Marktgasse 1"
                ,"PostalCode": 8400
                ,"City": "Winterthur"
            }
        ]

sales = [
            {
                "CustomerID": 1
                ,"Article": "Artikel A"
                ,"Quantity": 96
            },
            {
                "CustomerID": 1
                ,"Article": "Artikel B"
                ,"Quantity": 72
            },
            {
                "CustomerID": 1
                ,"Article": "Artikel C"
                ,"Quantity": 24
            },
            {
                "CustomerID": 1
                ,"Article": "Artikel D"
                ,"Quantity": 6
            }

        ]

requests = [
            {
                "RequestID": 1
                ,"CustomerID": 1
                ,"RequestedBy": "Mineralquelle XY"
                ,"RequestedFor": "Mineralquelle XY"
            },
            {
                "RequestID": 2
                ,"CustomerID": 2
                ,"RequestedBy": None
                ,"RequestedFor": "Mineralquelle XY"
            },
            {
                "RequestID": 3
                ,"CustomerID": 3
                ,"RequestedBy": None
                ,"RequestedFor": "Mineralquelle XY"
            },
            {
                "RequestID": 4
                ,"CustomerID": 4
                ,"RequestedBy": None
                ,"RequestedFor": "Mineralquelle XY"
            },

        ]

def get_customers():
    return cust

def get_requests():

    recs = []

    for requ in requests:
        rec = {
                "RequestID": requ["RequestID"]
                ,"Customer": get_customer(requ["CustomerID"])
                ,"RequestedBy": requ["RequestedBy"] if requ["RequestedBy"] is not None else get_customer(requ["CustomerID"])["Name"]
                ,"RequestedFor": requ["RequestedFor"]
            }

        recs.append(rec)

    return recs

def get_customer(id):
    return next((c for c in cust if c["ID"] == id), None)

def get_sales(cust_id):
    return [s for s in sales if s["CustomerID"] == cust_id]
