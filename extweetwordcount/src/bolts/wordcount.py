from __future__ import absolute_import, print_function, unicode_literals

from collections import Counter
from streamparse.bolt import Bolt
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

#Connecting to tcount
conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
cur = conn.cursor()
# Delete old records
cur.execute("DELETE FROM tweetwordcount")
conn.commit()

class WordCounter(Bolt):

    def initialize(self, conf, ctx):
        self.counts = Counter()

    def process(self, tup):
        word = tup.values[0]
        # Increment the local count
        self.counts[word] += 1
        self.emit([word, self.counts[word]])

        # Log the count - just to see the topology running
        self.log('%s: %d' % (word, self.counts[word]))


        # Write codes to increment the word count in Postgres
        # Use psycopg to interact with Postgres
        # Database name: Tcount 
        # Table name: Tweetwordcount 
        # you need to create both the database and the table in advance.
        if (self.counts[word] == 1):
		cur.execute("INSERT INTO tweetwordcount VALUES (%s, %s)", (word, self.counts[word]))
	else:
        	cur.execute("UPDATE tweetwordcount SET count=%s WHERE word=%s", (self.counts[word], word))

	conn.commit()
        

#conn.close()
