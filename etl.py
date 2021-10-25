import configparser
import psycopg2
from sql_queries import copy_table_queries, insert_table_queries

"""
Function drop_tables : This function loads the staging songs and events tables using the copy query 
"""

def load_staging_tables(cur, conn):
    for query in copy_table_queries:
        cur.execute(query)
        conn.commit()


"""
Function drop_tables : This function inserts the records in fact and dimension tables from the staging tables. 
"""

def insert_tables(cur, conn):
    for query in insert_table_queries:
        cur.execute(query)
        conn.commit()

        
"""
Main function inserts the records in fact and dimension tables from the staging tables.
After the insertion of data, connection to the Redshift Cluster is closed.
"""

def main():
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()
    
    load_staging_tables(cur, conn)
    insert_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()
