import sqlite3

queries = []

# Count how many rows you have - it should be 249!
query1 = '''SELECT COUNT("User Id")
FROM review;'''
queries.append(query1)

# How many users who reviewed at least 100 Nature in the category also
# reviewed at least 100 in the Shopping category?
query2 = '''SELECT COUNT("User Id")
FROM review
WHERE Nature >= 100 AND Shopping >= 100;'''
queries.append(query2)

# What are the average number of reviews for each category?
query3 = '''SELECT AVG(ALL Sports),
AVG(ALL Religious),
AVG(ALL Nature),
AVG(ALL Theatre),
AVG(ALL Shopping),
AVG(ALL Picnic)
FROM review'''
queries.append(query3)

# Run all the queries
conn = sqlite3.connect('buddymove_holidayiq.sqlite3')
curs = conn.cursor()
for index, query in enumerate(queries):
    print(f'Result of query {index+1}:')
    if index == 2:
        print(curs.execute(query).fetchall(), '\n')
    else:
        print(curs.execute(query).fetchone()[0], '\n')
    conn.commit()
curs.close()
