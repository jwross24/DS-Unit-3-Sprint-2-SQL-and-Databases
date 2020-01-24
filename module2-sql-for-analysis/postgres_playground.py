import psycopg2
import sqlite3

dbname = "yynnield"
user = "yynnield"
# Don't commit or share this for security purposes!
password = "PASSWORD-GOES-HERE"
# Port should be included or default
host = "rajje.db.elephantsql.com"

pg_conn = psycopg2.connect(dbname=dbname, user=user,
                           password=password, host=host)

pg_curs = pg_conn.cursor()

create_table_statement = """
CREATE TABLE test_table (
  id        SERIAL PRIMARY KEY,
  name  varchar(40) NOT NULL,
  data    JSONB
);
"""

insert_table_statement = """
INSERT INTO test_table (name, data) VALUES
(
  'A row name',
  null
),
(
  'Another row, with JSON',
  '{ "a": 1, "b": ["dog", "cat", 42], "c": true }'::JSONB
);
"""

pg_curs.execute(create_table_statement)
pg_curs.execute(insert_table_statement)
pg_conn.commit()

query = "SELECT * FROM test_table;"
pg_curs.execute(query)
print(pg_curs.fetchall())

sl_conn = sqlite3.connect('rpg_db.sqlite3')
sl_curs = sl_conn.cursor()

# We care about charactercreator_character table
row_count = 'SELECT COUNT(*) FROM charactercreator_character'
print(sl_curs.execute(row_count).fetchall())

# Our goal - copy the characters table from SQLite to PostgreSQL using Python
# Step 1 - E = Extract: Get the Characters
get_characters = 'SELECT * FROM charactercreator_character'
characters = sl_curs.execute(get_characters).fetchall()
print(characters[:5])
print(len(characters))

# Step 2 - Transform
# In this case, we don't actually want/need to change much
# Because we want to keep all the data
# And we're going from SQL to SQL

# But what do we need to be able to load into PostgreSQL?
# We need to make a new table with the appropriate schema

# What was the old schema? We can get at this with SQLite internals
print(sl_curs.execute(
    'PRAGMA table_info(charactercreator_character);'
    ).fetchall())

# https://www.postgresql.org/docs/current/sql-createtable.html

create_character_table = """
CREATE TABLE charactercreator_character (
    character_id SERIAL PRIMARY KEY,
    name VARCHAR(30),
    level INT,
    exp INT,
    hp INT,
    strength INT,
    intelligence INT,
    dexterity INT,
    wisdom INT
);
"""

pg_curs.execute(create_character_table)
pg_conn.commit()

# We can query tables if we want to check
# This is a clever optional thing, showing postgresql internals
show_tables = """
SELECT
   *
FROM
   pg_catalog.pg_tables
WHERE
   schemaname != 'pg_catalog'
AND schemaname != 'information_schema';
"""
pg_curs.execute(show_tables)
print(pg_curs.fetchall())

print(characters[0])

example_insert = """
INSERT INTO charactercreator_character
(name, level, exp, hp, strength, intelligence, dexterity, wisdom)
VALUES """ + str(characters[0][1:]) + ";"

print(example_insert)

# How do we do this for all characters? Loops!
for character in characters:
    insert_character = """
        INSERT INTO charactercreator_character
        (name, level, exp, hp, strength, intelligence, dexterity, wisdom)
        VALUES """ + str(character[1:]) + ";"
    pg_curs.execute(insert_character)
pg_conn.commit()

pg_curs.execute('SELECT * FROM charactercreator_character')
pg_characters = pg_curs.fetchall()

for character, pg_character in zip(characters, pg_characters):
    assert character == pg_character

# No complaints, which means they're all the same!

# Based off lecture notebook:
# https://colab.research.google.com/drive/1bebaE0R_ZQxG7yVppV08gR461T0dxh47
