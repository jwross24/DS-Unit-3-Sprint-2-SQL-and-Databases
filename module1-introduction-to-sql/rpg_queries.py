import sqlite3

queries = []

# How many total Characters are there?
query1 = '''SELECT COUNT(*)
FROM charactercreator_character;'''
queries.append(query1)

# How many of each specific subclass?
# Clerics
query2 = '''SELECT COUNT(*)
FROM charactercreator_cleric;'''
queries.append(query2)

# Fighters
query3 = '''SELECT COUNT(*)
FROM charactercreator_fighter;'''
queries.append(query3)

# Mages
query4 = '''SELECT COUNT(*)
FROM charactercreator_mage;'''
queries.append(query4)

# Necromancers
query5 = '''SELECT COUNT(*)
FROM charactercreator_necromancer;'''
queries.append(query5)

# Thieves
query6 = '''SELECT COUNT(*)
FROM charactercreator_thief;'''
queries.append(query6)

# How many total Items?
query7 = '''SELECT COUNT(*)
FROM armory_item;'''
queries.append(query7)

# How many of the Items are weapons? How many are not?
query8 = '''SELECT COUNT(*)
FROM armory_weapon;'''
queries.append(query8)

query9 = '''SELECT COUNT(*)
FROM armory_item
WHERE item_id NOT IN
(
    SELECT item_ptr_id
    FROM armory_weapon
);'''
queries.append(query9)

# How many Items does each character have? (Return first 20 rows)
query10 = '''SELECT character_id, COUNT(item_id) AS item_count
FROM charactercreator_character_inventory
GROUP BY character_id
LIMIT 20;'''
queries.append(query10)

# How many Weapons does each character have? (Return first 20 rows)
query11 = '''SELECT character_id, COUNT(item_id) AS weapon_count
FROM charactercreator_character_inventory
WHERE item_id IN
(
    SELECT item_ptr_id
    FROM armory_weapon
)
GROUP BY character_id
LIMIT 20;'''
queries.append(query11)

# On average, how many Items does each Character have?
query12 = '''SELECT AVG(item_count) AS avg_items
FROM
(
    SELECT COUNT(item_id) AS item_count
    FROM charactercreator_character_inventory
    GROUP BY character_id
);'''
queries.append(query12)

# On average, how many Weapons does each character have?
query13 = '''SELECT AVG(weapon_count) AS avg_weapons
FROM
(
    SELECT COUNT(*) AS weapon_count
    FROM charactercreator_character_inventory
    WHERE item_id IN (SELECT item_ptr_id FROM armory_weapon)
    GROUP BY character_id
);'''
queries.append(query13)

# Run all the queries
conn = sqlite3.connect('rpg_db.sqlite3')
curs = conn.cursor()
for index, query in enumerate(queries):
    print(f'Result of query {index+1}:')
    if index in [9, 10]:
        print(curs.execute(query).fetchall(), '\n')
    else:
        print(curs.execute(query).fetchone()[0], '\n')
    conn.commit()
curs.close()
