from consts import DB_NAME
import sqlite3

connection = sqlite3.connect(DB_NAME)
cursor = connection.cursor()

