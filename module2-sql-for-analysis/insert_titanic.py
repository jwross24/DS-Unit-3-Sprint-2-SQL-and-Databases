from os import getcwd
import psycopg2

# Initialize connection information
dbname = "yynnield"
user = "yynnield"
# Don't commit or share this for security purposes!
password = "PASSWORD-GOES-HERE"
# Port should be included or default
host = "rajje.db.elephantsql.com"

# Create the connection and a new cursor
pg_conn = psycopg2.connect(dbname=dbname, user=user,
                           password=password, host=host)
pg_curs = pg_conn.cursor()

# Drop the `psex` type and `passengers` table if they exist
drop_type_statement = "DROP TYPE IF EXISTS psex CASCADE;"
drop_table_statement = "DROP TABLE IF EXISTS Passengers;"

pg_curs.execute(drop_type_statement)
pg_curs.execute(drop_table_statement)
pg_conn.commit()

# Create the `psex` type and `passengers` table
create_type_statement = "CREATE TYPE psex AS ENUM ('male', 'female');"
create_table_statement = """
CREATE TABLE Passengers (
    Survived    BOOLEAN,
    Pclass      INTEGER,
    Name        TEXT PRIMARY KEY,
    Sex         psex,
    Age         NUMERIC(3, 1),
    SibSp       INTEGER,
    ParCh       INTEGER,
    Fare        NUMERIC(7, 4)
);
"""

pg_curs.execute(create_type_statement)
pg_curs.execute(create_table_statement)
pg_conn.commit()

# Copy the Titanic dataset into the `passengers` table
file_path = getcwd()
with open(file_path + '/titanic.csv', 'r') as f:
    next(f)
    pg_curs.copy_from(f, 'Passengers', sep=',')
    pg_conn.commit()

# Example query to see if the data was copied successfully
pg_curs = pg_conn.cursor()
pg_curs.execute('SELECT * FROM passengers LIMIT 5;')
[print(row) for row in pg_curs.fetchall()]
pg_conn.commit()

# Close the connection
pg_conn.close()
