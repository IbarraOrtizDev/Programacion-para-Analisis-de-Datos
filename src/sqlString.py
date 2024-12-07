createDatabaseString = """CREATE DATABASE IF NOT EXISTS dataQuery"""

createTableString = """CREATE TABLE IF NOT EXISTS data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(255),
    price VARCHAR(255),
    marca VARCHAR(255),
    imagenProducto VARCHAR(255),
    rating VARCHAR(255),
    linkProduct VARCHAR(255),
    store VARCHAR(255),
    ean VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)"""

insertDataString = """INSERT INTO data (title, price, marca, imagenProducto, rating, linkProduct, store, ean) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"""


# Query data by ean
selectDataString = """SELECT * FROM data WHERE ean = ? AND created_at >= datetime('now', '-1 day')"""

selectDataLastOneDayByStore = """SELECT * FROM data WHERE ean = ? AND store = ? AND created_at >= datetime('now', '-1 day')"""