About the Project:
------------------
A music streaming startup, Sparkify, has grown their user base and song database and want to move their processes and data onto the cloud. Their data resides in S3, in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

To find what songs users are listening in the app, Datawarehousing concepts are applied by building a ETL pipeline in AWS. Data is loaded S3 to staging tables on Redshift and execute SQL statements that create the analytics tables from these staging tables.

Database Schema Design:
-----------------------
- Star Schema is followed in project.
- Staging tables(songs and events) are created.JSON data from S3 are pulled without any modification and loaded them into staging tables. 
- New fact table(songplays) and dimension tables(time,users,songs,artists) are designed for easy analyis.  Data from staging tables are loaded into the actual tables.

Repository Files: 
-----------------

- create_tables.py : This python script file performs the below functions:
    1. Calls the local functions 'Drop' and 'Create' which will run the sql queries to drop and create new fact table(songplays) and dimension tables(time,users,songs,artists). 
    2. Sql queryies are imported from the python file sql_queries.py 
- sql_queries.py : This python sql drops the table if already present in the database, creates new tables and inserts the records.
- etl.py : 
    1. After successfully processing, and inserting the single record, this ETL python file is executed via the terminal and entire file is processed. 
- dwh.cfg : Configuration file filled with the details about the cluster, IAM roles and s3 data files

ETL Pipeline Process:
---------------------
1. Redshift cluster is created in AWS .
2. Staging tables 'staging_events' and 'staging_songs' are created . JSON files are pulled from S3 and data is copied into the tables without any modification.
3. New fact table(songplays) and dimension tables(time,users,songs,artists) are designed by following the Star Schema
4. SQL Insert queries are run to Select the data from staging tables and loaded into their respective table columns in proper data format.

Analytic Queries:
-----------------
1. To ensure the tables are loaded from staging tables to the respective tables, count sql query was run to check whether data is loaded or not.

SELECT COUNT(*)
FROM songplays

2. Following query was run to calculates the most frequently played song, calling on the songplays, artists and songs tables:

SELECT a.name, so.title, COUNT(so.title) FROM songplays sp
JOIN artists a
ON a.artist_id = sp.artist_id
JOIN songs so
ON sp.song_id = so.song_id
GROUP BY 1, 2
ORDER BY 3 DESC
LIMIT 1

output : Dwight Yoakam / You're The One/ 37
