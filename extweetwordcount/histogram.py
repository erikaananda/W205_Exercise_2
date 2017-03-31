import sys
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

class histogram():
	try:
		start = int(sys.argv[1])
		end = int(sys.argv[2])
		#print(start, end)
	except:
		print("Incorrect arguments provided")
		quit()
	#Connecting to tcount
	conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
	cur = conn.cursor()
	cur.execute("SELECT * from tweetwordcount")
	records = cur.fetchall()
	if (len(records) > 0):
		for rec in records:
			if (rec[1] >= start and rec[1] <= end):
				print (rec[0], rec[1])
 	else:
 		print("Table is empty.")

if __name__ == '__main__':
	histogram()
