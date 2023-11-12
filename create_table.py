from cursor import cursor

cursor.execute("""
               CREATE TABLE IF NOT EXISTS data (
               subject STRING,
               mark INTEGER,
               date STRING,
               quarter STRING)
               """)

