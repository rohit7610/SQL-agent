from pathlib import Path
import sqlite3

folder_path = Path(__file__).parent / "Database" 
db_path = folder_path / "shop.db"
conn = sqlite3.connect(db_path)

cursor = conn.cursor()

conn.execute("PRAGMA foreign_keys = ON;") # used to fecth the structure of the entire databse


#create table
conn.execute("""
CREATE TABLE IF NOT EXISTS customers(
customer_id INT PRIMARY KEY,
name TEXT NOT NULL,
email TEXT
)
""")

conn.execute("""
CREATE TABLE IF NOT EXISTS products(
product_id INT PRIMARY KEY,
pro_name TEXT,
price INT,
stock INT
)
""")

conn.execute("""
CREATE TABLE IF NOT EXISTS orders(
order_id INT PRIMARY KEY,
c_id INT,
p_id INT,
order_date TEXT,
total_amt INT,
FOREIGN KEY (c_id) REFERENCES customers(customer_id),
FOREIGN KEY (p_id) REFERENCES products(product_id)
)
""")

# Insert data
customer_data = [
    (101,'Rohit','rohit@gmail.com'),
    (102,'Krish','krish@gmail.com'),
    (103,'Ritik','ritik@gmail.com'),
    (104,'Mohit','mohit@gmail.com')
]


product_data = [
    (10,'ATV Bike',8500,10),
    (11,'Offroad Vehicle',15500,20),
    (12,'Continetal Gt',9500,24),
    (13,'Cruiser',10000,43)
]

order_data = [
    (1,101,10,'2026-10-12',17000),
    (2,102,11,'2026-09-10',15500),
    (3,103,12,'2026-08-23',9500),
    (4,104,13,'2026-08-15',10000)
]

conn.executemany("INSERT OR IGNORE INTO customers(customer_id, name, email) VALUES(?,?,?);", customer_data)
conn.executemany("INSERT OR IGNORE INTO products(product_id, pro_name, price, stock) VALUES(?,?,?,?);", product_data)
conn.executemany("INSERT OR IGNORE INTO orders(order_id,c_id,p_id,order_date,total_amt) VALUES(?,?,?,?,?);", order_data)

conn.commit()
conn.close()

print("shop.db initialized succesfully")