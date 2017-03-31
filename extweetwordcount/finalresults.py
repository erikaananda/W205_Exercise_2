import sys
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

class finalResult():
	try:
		word = sys.argv[1]
	except:
		word = ''
	#Connecting to tcount
	conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
	cur = conn.cursor()
	# check for a single word
	if (len(word) > 0):
		#Select  
		sql = (''.join(["SELECT * FROM tweetwordcount WHERE word = '", word, "'"]))
		#cur.execute("SELECT * FROM tweetwordcount WHERE word = '{0}'", (word))
		#print(sql)
		cur.execute(sql)
		records = cur.fetchall()
		if (len(records) > 0):
			print(''.join(["Total number of occurences of '", word, "':", str(records[0][1])]))
 		else:
 			print("Word not found.")
	else:
		cur.execute("SELECT * from tweetwordcount")
		records = cur.fetchall()
		records = sorted(records)
		if (len(records) > 0):
			for rec in records:
				print (rec[0], rec[1])
 		else:
 			print("Table is empty.")

if __name__ == '__main__':
	finalResult()
