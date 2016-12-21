#https://github.com/puentesarrin/pymongolab/blob/159a46c6cf88313c11522503d9243e2e16d3d72c/doc/examples.rst

import random
from pymongolab import MongoClient

con = MongoClient("t3md-y8OEJDs1vmPqIzuqfjqNUvckV12")
db = con.testebanco4

q1 = db.q1

data = []

for i in range(0, 1000):
	data.append({str(i): i})

while True:
	q1.insert(data)
	print "inserted"


