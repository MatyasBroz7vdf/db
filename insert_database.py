import database_connect as dc
import functions as fc
import config as cf
import os
import random
import time

def _create_vendors(min_lenght_vendor: int, max_lenght_vendor: int, _database, vendors):
    x = 0
    while x < vendors:
        o = "INSERT INTO `vendor` (name) VALUES "
        l = fc._get_random_string(min_lenght_vendor, max_lenght_vendor)
        o = o + "(\"" + l + "\");"
        x += 1
        d = dc.execute(o, _database)

def _create_products(min_lenght_products: int, max_lenght_products: int, _database, vendors, products):
    x = 0
    while x < products:
        o = "INSERT INTO `product` (name, price, vendor_id) VALUES "
        l = fc._get_random_string(min_lenght_products, max_lenght_products)
        l1 = str(random.randint(1, 2000))
        l2 = str(random.randint(1, vendors))
        print("L2", l2)
        o = o + "(\'" + l + "\', " + l1 + ", " + l2 + ");"
        x += 1
        print(o)
        d = dc.execute(o, _database)


def main():
    i = 0
    if True:
        products = 100
        min_lenght_products = 5
        max_lenght_products = 7

        vendors = 10
        min_lenght_vendor = 3
        max_lenght_vendor = 8

    _database = dc.connect(cf.location, cf.port, cf.user, cf.pw, cf.db)
    dc.clear(_database) #CLEARING DATABASE
    start_time = time.time() #START TIMER HERE

    _create_vendors(min_lenght_vendor, max_lenght_vendor, _database, vendors) #CREATING VENDORS
    _create_products(min_lenght_products, max_lenght_products, _database, vendors, products) #CREATING PRODUCTS

    end_time = time.time() #STOP TIMER HERE

    a = dc.execute("SELECT v.id, v.name, COUNT(p.id) AS product_count FROM vendor v LEFT JOIN product p ON v.id = p.vendor_id GROUP BY v.id ORDER BY product_count DESC;", _database)
    for z in a:
        print(z)
    
    dc.close(_database)

    print("It took ", end_time - start_time, " seconds.")



main()