import sqlite3

conn = sqlite3.connect('rpg_db.sqlite3')
curs = conn.cursor()
query = '''SELECT *
FROM charactercreator_character
INNER JOIN charactercreator_mage
ON character_id = character_ptr_id;'''

curs.execute(query)
print(curs.fetchone())
print(curs.fetchone())
print(curs.fetchone())

remaining_results = curs.fetchall()
print(remaining_results[:5])
