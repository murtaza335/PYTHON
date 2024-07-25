import sqlite3 as sql
from items import *

connection = sql.Connection("items.db")
cursor = connection.cursor()
# Table 1 Pizza 
cursor.execute("""CREATE TABLE IF NOT EXISTS pizza( 
               pizza_id INTEGER PRIMARY KEY, 
               pizza_names TEXT NOT NULL,
               price_s INTEGER NOT NULL,
               price_m INTEGER NOT NULL,
               price_l INTEGER NOT NULL,
               price_xl INTEGER NOT NULL)""")
# Table 2 Burger 
cursor.execute("""CREATE TABLE IF NOT EXISTS burger(
               burger_id INTEGER PRIMARY KEY,
               burger_names text NOT NULL,
               burger_price INTEGER NOT NULL ) """)
# Table 3 shawarma
cursor.execute("""CREATE TABLE IF NOT EXISTS shawarma( 
               shawarma_id INTEGER PRIMARY KEY, 
               shawarma_names TEXT NOT NULL,
               price_s INTEGER NOT NULL,
               price_m INTEGER NOT NULL,
               price_l INTEGER NOT NULL)""")
# Table 4 fries 
cursor.execute("""CREATE TABLE IF NOT EXISTS fries( 
               fries_id INTEGER PRIMARY KEY, 
               fries_names TEXT NOT NULL,
               price_s INTEGER NOT NULL,
               price_m INTEGER NOT NULL,
               price_l INTEGER NOT NULL)""")
# Table 5 drinks 
cursor.execute("""CREATE TABLE IF NOT EXISTS drinks( 
               drinks_id INTEGER PRIMARY KEY, 
               drinks_names TEXT NOT NULL,
               price_s INTEGER NOT NULL,
               price_m INTEGER NOT NULL,
               price_l INTEGER NOT NULL)""")
# Table 6 Pizza_top 
cursor.execute("""CREATE TABLE IF NOT EXISTS pizza_top(
               top_id INTEGER PRIMARY KEY,
               top_name text NOT NULL,
               top_price INTEGER NOT NULL ) """)
# Table 7 sauces 
cursor.execute("""CREATE TABLE IF NOT EXISTS sauces(
               sauce_id INTEGER PRIMARY KEY,
               sauce_names text NOT NULL,
               sauce_price INTEGER NOT NULL ) """)





# id = [11238000, 11238001, 11238002]

# for i in range(len(id)):
#     cursor.execute("INSERT INTO drinks VALUES(?,?,?,?,?,?)",(id[i],drinks[i],100,150,190,250))




connection.commit()
connection.close()