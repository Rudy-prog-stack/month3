create_product_table ="""
CREATE TABLE IF NOT EXISTS products (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name_product VARCHAR(100) NOT NULL,
price INTEGER NOT NULL,
photo TEXT
)
"""

add_product = 'INSERT INTO products(name_product, price, photo) VALUES (?, ?, ?)'
get_product = 'SELECT name_product, price FROM products'

products_detail_table = """
    CREATE TABLE IF NOT EXISTS products_detail (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        category TEXT,
        color TEXT,
        product_id INTEGER NOT NULL UNIQUE,
        description TEXT
    )
"""

insert_product_detail = "INSERT INTO products_detail (category, color, product_id, description) VALUES (?, ?, ?, ?)" 

select_product_id = "SELECT 1 FROM products WHERE product_id = ?"

get_products = """ SELECT p.id AS product_id, p.name_product, p.photo, p.price, pd.category, pd.color, pd.description FROM products AS p LEFT JOIN products_detail AS pd ON p.id = pd.product_id ORDER BY p.id DESC """

update_product = 'UPDATE {table} SET {field} = ? WHERE product_id = ?'