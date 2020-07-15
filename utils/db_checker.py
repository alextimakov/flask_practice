import sqlite3

conn = sqlite3.connect('instance/sample_app.sqlite')

c = conn.cursor()
for row in c.execute("SELECT * from user"):
    print(row)

conn.commit()
conn.close()
