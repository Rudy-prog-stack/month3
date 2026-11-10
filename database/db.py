import aiosqlite
from database import queries


path_db = 'database/sqlite3.db'

async def init_db():
    async with aiosqlite.connect(path_db) as conn:
        await conn.execute(queries.create_product_table)
        await conn.commit()

async def add_product_db(name_product, price, description, photo):
    async with aiosqlite.connect(path_db) as conn:
        await conn.execute(queries.add_product, (name_product, price, description, photo))
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
        



