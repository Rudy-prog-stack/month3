create_product_table ="""
CREATE TABLE IF NOT EXISTS products (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name_product VARCHAR(100) NOT NULL,
price INTEGER NOT NULL,
description TEXT NOT NULL,
photo TEXT
)
"""

add_product = 'INSERT INTO products(name_product, price, description, photo) VALUES (?, ?, ?, ?)'
get_product = 'SELECT name_product, price, description FROM products'
