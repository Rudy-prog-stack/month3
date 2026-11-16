import aiosqlite
from database import queries


path_db = 'database/sqlite3.db'

async def init_db():
    async with aiosqlite.connect(path_db) as conn:
        await conn.execute(queries.create_product_table)
        await conn.execute(queries.products_detail_table)
        await conn.commit()

async def add_product_db(name_product, price, photo):
    async with aiosqlite.connect(path_db) as conn:
        await conn.execute(queries.add_product, (name_product, price, photo))
        await conn.commit()

async def get_product_db():
    async with aiosqlite.connect(path_db) as conn:
        cursor = await conn.execute(queries.get_product)
        products = await cursor.fetchall()
    return products

async def get_product_by_id(id_product):
    async with aiosqlite.connect(path_db) as conn:
        cursor = await conn.execute(queries.get_product_by_id, (id_product,))
        product = await cursor.fetchone()
    return product

# --------------------------------------------------------------------------------------------

async def add_product_detail_db(category, color, product_id, description):
    async with aiosqlite.connect(path_db) as conn:
        await conn.execute(queries.insert_product_detail, (category, color, product_id, description))
        await conn.commit()

async def get_product_detail_db():
    async with aiosqlite.connect(path_db) as conn:
        cursor = await conn.execute(queries.select_product_id)
        products = await cursor.fetchone()
    return products

async def get_product_by_detail(name, photo, price, product_id, category, color, description):
    async with aiosqlite.connect(path_db) as conn:
        cursor = await conn.execute(queries.get_products, (name, photo, price, product_id, category, color, description))
        product = await cursor.fetchall()
    return product

async def get_products_db():
    async with aiosqlite.connect(path_db) as conn:
        cursor = await conn.execute(queries.get_products)
        products = await cursor.fetchall()
    return products

