from cursor import connection, cursor


cursor.execute("""
               CREATE TABLE IF NOT EXISTS config (
               key STRING,
               value STRING
               );
               """)

quarter: str = input('Input quarter: ')
chart_title: str = input('Input title of a chart: ')

config_keys = ['quarter', 'chart_title']
config_values = [quarter, chart_title]

with connection:
    cursor.execute("""DELETE FROM config;""")
    for i in range(len(config_keys)):
        cursor.execute(f"""
                       INSERT INTO config (key, value) VALUES ('{config_keys[i]}', '{config_values[i]}');
                       """)

