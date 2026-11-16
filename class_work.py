create_product_table ="""
CREATE TABLE IF NOT EXISTS products (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name_product VARCHAR(100) NOT NULL,
price INTEGER NOT NULL,
description TEXT NOT NULL,
photo TEXT
)
"""
create_product_detail_table ="""
CREATE TABLE IF NOT EXISTS products (
id INTEGER PRIMARY KEY AUTOINCREMENT,
category TEXT,
price INTEGER NOT NULL,
description TEXT NOT NULL,
photo TEXT
PRODUCT_ID INTEGER NOT NULL,
)
"""

Add_product = 'INSERT INTO products(product_id, price, description, photo) VALUES (?, ?, ?, ?)'