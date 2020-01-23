# Based on Colab lecture notebook:
# https://colab.research.google.com/drive/1gdcNkWXF7njja7XiWT7ZiInna0RsWdQR

import pymongo

# Don't commit this! Reset this if it is committed
mongo_password = 'password'

# Make sure that dnspython module is installed
client = pymongo.MongoClient("mongodb+srv://dbUser:<password>@cluster0-cmo65.mongodb.net/test?retryWrites=true&w=majority")
db = client.test

print(db)

# print(db.test.count_documents({'x': 1}))
# db.test.insert_one({'x': 1})
# print(db.test.count_documents({'x': 1}))
# db.test.insert_one({'x': 1})
# print(db.test.count_documents({'x': 1}))

curs = db.test.find({'x': 1})
print(list(curs))

# Let's add some more interesting documents!
# Note - keys can be variable, which makes things easy to get started
# But interesting and potentially complicated to query

loris_doc = {
    'favorite_animal': 'peacock',
    'favorite_color': 'blue',
    'favorite_number': 7
}

jons_doc = {
    'favorite_animal': 'narwhal',
    'favorite_color': 'blue',
    'favorite_number': 24
}

emmas_doc = {
    'favorite_animal': 'panther',
    'favorite_color': 'purple',
    'favorite_number': 2
}

rays_doc = {
    'favorite_animal': 'wolf',
    'favorite_color': 'blue',
    'favorite_number': 16
}

baisali_doc = {
    'favorite_animal': 'elephant',
    'favorite_color': 'red',
    'favorite_number': 2
}

juds_doc = {
    'favorite_animal': 'liger',
    'favorite_color': 'blellow',
    'favorite_number': 42,
    'favorite_direction': 'Weast'
}

jans_doc = {
    'favorite_city': 'rotterdam',
    'favorite_color': 'green',
    'favorite_sport': 'football'
}

faraazs_doc = {
    'favorite_animal': 'ring-tailed lemur',
    'favorite_color': 'forest green',
    'favorite_restaurant': 'in-n-out'
}

all_docs = [loris_doc, jons_doc, emmas_doc, rays_doc, baisali_doc, juds_doc,
            jans_doc, faraazs_doc]

db.test.insert_many(all_docs)
print(list(db.test.find()))

more_docs = []
for i in range(10):
    doc = {'even': i % 2 == 0}
    doc['value'] = i
    more_docs.append(doc)

print(more_docs)

db.test.insert_many(more_docs)

print(list(db.test.find({'even': True, 'value': 0})))
print(list(db.test.find({'even': True})))
print(list(db.test.find({'favorite_color': 'blue'})))

# What is CRUD?
# Create Read Update Delete - aka most apps!
# Check out help(db.test.update_one)

db.test.delete_many({'even': False})
print(list(db.test.find()))

rpg_character = (1, "King Bob", 10, 3, 0, 0, 0)

# db.test.insert_one(rpg_character) gives an error
# We need a dictionary
# Lazy (probably not good long-term) solution!
db.test.insert_one({'rpg_character': rpg_character})

print(db.test.find_one({'rpg_character': rpg_character}))

# We can do better - even though we're not required to make a schema
# We should make useful/informative key names in our docs

rpg_doc = {
    'sql_key': rpg_character[0],
    'name': rpg_character[1],
    'hp': rpg_character[2],
    'level': rpg_character[3]
}

db.test.insert_one(rpg_doc)
print(list(db.test.find(rpg_doc)))

# Assignment - get the actual rpg_db data (from SQLite/PostgreSQL)
# Write code to turn it into docs (dictionaries) and insert

# Answer these questions:
# How was working with MongoDB different from working with PostgreSQL?
# What was easier, and what was harder?
