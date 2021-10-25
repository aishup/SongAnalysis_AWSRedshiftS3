import configparser
import psycopg2
from sql_queries import create_table_queries, drop_table_queries

"""
Function drop_tables : This function will drop the tables if already exists in the cluster. 
"""

def drop_tables(cur, conn):
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()

"""
Function create_tables : This function will create the staging tables and star schema based tables for ETL processing .
"""

def create_tables(cur, conn):
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()
"""
Function Main: Connects to the AWS Redshift Cluster and calls the functions drop_tables and create_tables. 
After the creation of tables, connection to the Redshift Cluster is closed.

"""

def main():
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()

    drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()
