from cursor import connection, cursor


def get_config_data(key: str):
    with connection:
        return cursor.execute(f"""
                               SELECT * FROM config WHERE key = '{key}'
                               """).fetchone()[1]

