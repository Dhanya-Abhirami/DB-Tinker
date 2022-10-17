# https://www.psycopg.org/docs/usage.html
import psycopg2
import time

# Connect to existing database
conn = psycopg2.connect(
    database="docker",
    user="docker",
    password="docker",
    host="db-postgres"
)

# Open cursor to perform database operation
cur = conn.cursor()

# Create table
cur.execute("""CREATE TABLE titanic_passengers (
PassengerId INTEGER,
Survived INTEGER,
Pclass INTEGER,
Name TEXT,
Sex TEXT,
Age FLOAT,
SibSp INTEGER,
Parch  INTEGER,
Ticket TEXT,
Fare FLOAT,
Cabin TEXT,
Embarked TEXT)
""")

# Insert CSV data to DB
cur = conn.cursor()
with open('data/train.csv', 'r') as f:
    next(f) # Skip the header row.
    cur.copy_from(f, 'titanic_passengers', sep='|',null='')
conn.commit()

# Query the database 
t0 = time.time()
cur.execute("SELECT * FROM titanic_passengers")
rows = cur.fetchall()
# for row in rows:
#     print(row)
t1 = time.time()
total = t1-t0
print(total)

# Close communications with database
cur.close()
conn.close()
