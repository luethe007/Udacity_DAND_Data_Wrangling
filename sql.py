import sqlite3
from sqlite3 import Error


# return database connection object
def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print e

    return None


# create table with connection object and create_table statement
def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print e


# main procedure to create database and tables
def main():
    db_file = "osm.db"

    # create table statements
    create_table_nodes = ''' CREATE TABLE nodes (
                                id TEXT PRIMARY KEY NOT NULL,
                                lat REAL,
                                lon REAL,
                                user TEXT,
                                uid INTEGER,
                                version TEXT,
                                changeset INTEGER,
                                timestamp TEXT
                            );'''

    create_table_node_tags = '''CREATE TABLE node_tags (
                                id INTEGER,
                                key TEXT,
                                value TEXT,
                                type TEXT,
                                FOREIGN KEY (id) REFERENCES nodes(id)
                            );'''

    create_table_ways = '''CREATE TABLE ways ( 
                                id TEXT PRIMARY KEY NOT NULL,
                                user TEXT,
                                uid INTEGER,
                                version TEXT, 
                                changeset INTEGER,
                                timestamp TEXT
                            );'''

    create_table_way_nodes = '''CREATE TABLE way_nodes (
                                id INTEGER NOT NULL,
                                node_id INTEGER,
                                position INTEGER, 
                                FOREIGN KEY (id) REFERENCES ways(id),
                                FOREIGN KEY (node_id) REFERENCES nodes(id)
                            );'''

    create_table_way_tags = '''CREATE TABLE way_tags (
                                id INTEGER NOT NULL,
                                key TEXT,
                                value TEXT,
                                type TEXT,
                                FOREIGN KEY (id) REFERENCES ways(id)
                            );'''

    # create connection object that represents database
    conn = create_connection("/Users/marvin-luethe/Desktop/My_Hawaii_Project/" + db_file)

    if conn is not None:
        create_table(conn, create_table_nodes)
        create_table(conn, create_table_node_tags)
        create_table(conn, create_table_ways)
        create_table(conn, create_table_way_nodes)
        create_table(conn, create_table_way_tags)
    else:
        print 'Error, database connection could not be created!'


if __name__ == '__main__':
    main()
