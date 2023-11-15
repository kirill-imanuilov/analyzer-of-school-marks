from cursor import cursor, connection
import datetime
from get_config_data import get_config_data


with open('./subjects.txt', 'r') as file:
    subjects = file.readlines()
    # Delete '\n'
    for i in range(len(subjects)):
        subjects[i] = subjects[i][:-1]

input_date_message:str = 'Date: '

quarter: str = get_config_data(key='quarter')

date:str = input(input_date_message)

if date == '':
    date = str(datetime.date.today())

with connection:
    for elem in subjects:
        cursor.execute(f"""
                       INSERT INTO data (subject, mark, date, quarter) VALUES (
                       '{elem}',
                       '{float(input(elem + ": "))}',
                       '{date}',
                       '{quarter}'
                       )
                       """)

