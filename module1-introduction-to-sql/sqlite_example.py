import sqlite3

conn = sqlite3.connect('toy_data.db')
curs = conn.cursor()
query = 'CREATE TABLE toy (name varchar(30), size int);'
curs.execute(query)
curs.close()
conn.commit()

curs2 = conn.cursor()
print(curs2.execute('SELECT * from toy;').fetchall())

insert_query = 'INSERT INTO toy (name, size) VALUES ("awesome", 27);'
curs2.execute(insert_query)
curs2.close()
conn.commit()

curs3 = conn.cursor()
print(curs3.execute('SELECT * from toy;').fetchall())
