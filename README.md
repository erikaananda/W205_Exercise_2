# W205_Exercise_2
## extweetwordcount
The goal of this exercise is to create an end to end streaming application which takes twitter data 
in through a storm spout, parses the words, and stores the count of each word occurrence in a postgres 
table. Two python scripts can be used to query the results: one for the count of a word supplied in a 
parameter, and another for the words with counts between numbers supplied in parameters. 

## Directory and File Structure
Files under the root/extweetwordcount directory are stored as follows:
Storm Files (all required)

topologies: 

tweetwordcount.clj file directing spouts and bolts processing

src/spouts:

     tweets.py: pulls tweets in a dynamic stream

src/bolts:

     parse.py: tokenizes all tweet words
    
     wordcount.py: keeps a running count of tokens and stores results in the postgres table tweetwordcount

## To Run the Application 
Copy the extweetwordcount directory to an AWS instance using UCBMIDSW205EX2-FULL 
Replace the existing twitter application credentials with a new set. 
Attach a disk to the instance that includes an installation of postgres.

Create a postgres database and table: 

psql -U postgres
create database tcount;
\c tcount

CREATE TABLE tweetwordcount
       (word TEXT PRIMARY KEY     NOT NULL,
       count INT     NOT NULL);

tcount-# \dt

             List of relations
 Schema |      Name      | Type  |  Owner   
--------+----------------+-------+----------

 public | tweetwordcount | table | postgres
(1 row)

\q

From the extweetwordcount directory, type ‘sparse run’ and hit enter. 

Use Ctrl-C to break when ready.

Use finalResults.py and histogram.py to review the results.
