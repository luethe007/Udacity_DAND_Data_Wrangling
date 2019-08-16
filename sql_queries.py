import sqlite3
import pandas as pd

# Create connection object to "osm.db" database and create cursor object.
db = sqlite3.connect("osm.db")
c = db.cursor()

# Calculate amount of entries per table.
tables = ['nodes', 'node_tags', 'ways', 'way_nodes', 'way_tags']

for table in tables:
    QUERY = "SELECT count(*) FROM {}".format(table)
    c.execute(QUERY)
    print table
    print c.fetchone()

# Counts the occurrence of the top ten key values in the 'node_tags' and 'way_tags' tables.
QUERY = "SELECT tags.key, count(*) as num " \
        "FROM (SELECT * FROM node_tags UNION ALL SELECT * FROM way_tags) as tags " \
        "GROUP BY tags.key " \
        "ORDER BY num DESC " \
        "LIMIT 50;"
c.execute(QUERY)
df = pd.DataFrame(c.fetchall())
print df

# Further investigate highways
QUERY = "SELECT tags.value, count(*) as num " \
        "FROM (SELECT * FROM node_tags UNION ALL SELECT * FROM way_tags) as tags " \
        "WHERE tags.key='highway' " \
        "GROUP BY tags.value " \
        "ORDER BY num DESC " \
        "LIMIT 10;"
c.execute(QUERY)
df = pd.DataFrame(c.fetchall())
print df

# Further investigate buildings
QUERY = "SELECT tags.value, count(*) as num " \
        "FROM (SELECT * FROM node_tags UNION ALL SELECT * FROM way_tags) as tags " \
        "WHERE tags.key='building' " \
        "GROUP BY tags.value " \
        "ORDER BY num DESC " \
        "LIMIT 10;"
c.execute(QUERY)
df = pd.DataFrame(c.fetchall())
print df

# Further investigate amenities
QUERY = "SELECT tags.value, count(*) as num " \
        "FROM (SELECT * FROM node_tags UNION ALL SELECT * FROM way_tags) as tags " \
        "WHERE tags.key='amenity' " \
        "GROUP BY tags.value " \
        "ORDER BY num DESC " \
        "LIMIT 10;"
c.execute(QUERY)
df = pd.DataFrame(c.fetchall())
print df

# Further investigate cuisine
QUERY = "SELECT tags.value, count(*) as num " \
        "FROM (SELECT * FROM node_tags UNION ALL SELECT * FROM way_tags) as tags " \
        "WHERE tags.key='cuisine' " \
        "GROUP BY tags.value " \
        "ORDER BY num DESC " \
        "LIMIT 10;"
c.execute(QUERY)
df = pd.DataFrame(c.fetchall())
print df


# Further investigate streets
QUERY = "SELECT distinct(value) " \
        "FROM node_tags " \
        "WHERE key='street';"
c.execute(QUERY)
df = pd.DataFrame(c.fetchall())
print df

# Further investigate countries
QUERY = "SELECT distinct(value) " \
        "FROM node_tags " \
        "WHERE key='country';"
c.execute(QUERY)
df = pd.DataFrame(c.fetchall())
print df

# Further investigate cities
QUERY = "SELECT distinct(value) " \
        "FROM node_tags WHERE key='city' " \
        "ORDER BY value COLLATE NOCASE ASC;"
c.execute(QUERY)
df = pd.DataFrame(c.fetchall())
print df


db.close()
