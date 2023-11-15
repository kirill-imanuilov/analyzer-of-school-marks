from cursor import connection, cursor
import matplotlib.pyplot as plt


quarter = 'II'
chart_title = 'title'

with open('./subjects.txt', 'r') as file:
    subjects = file.readlines()
    # Delete '\n'
    for i in range(len(subjects)):
        subjects[i] = subjects[i][:-1]

with connection:
    for subject in subjects:
        data = cursor.execute(f"""
                       SELECT * FROM data WHERE subject = '{subject}' AND quarter = '{quarter}'
                       """).fetchall()
        keys = []
        values = []
        for elem in data:
            keys.append(elem[2])
            values.append(elem[1])
        plt.plot(keys, values, label=data[0][0])


    values = [4.50] * len(keys)
    plt.plot(keys, values, 'k-.')
    values = [3.50] * len(keys)
    plt.plot(keys, values, 'k-.')

    plt.xticks(rotation=20)
    plt.legend()
    plt.title(chart_title)
    plt.savefig(chart_title + '.png')
    

