import csv
import sys
import time
i = 0
userID = 0
j = 1
workOn = []

finalDict = {
	"2011":[0,0,0,0,0,0,0,0,0,0,0,0],
	"2012":[0,0,0,0,0,0,0,0,0,0,0,0],
	"2013":[0,0,0,0,0,0,0,0,0,0,0,0],
	"2014":[0,0,0,0,0,0,0,0,0,0,0,0],
	"2015":[0,0,0,0,0,0,0,0,0,0,0,0],
	"2016":[0,0,0,0,0,0,0,0,0,0,0,0]
}

# print time.strftime("%Y")
# print time.strftime("%m")

def addToFinalMatrix(fromMonth, fromYear, toMonth, toYear):
	if int(toYear)>2010 and int(fromYear)>2010:
		for x in xrange(int(fromYear)+1,int(toYear)):
			for y in xrange(12):
				finalDict[str(x)][y] = finalDict[str(x)][y] + 1

		for x in xrange(0,int(toMonth)):
			finalDict[str(toYear)][x] = finalDict[str(toYear)][x] + 1 

		for x in xrange(int(fromMonth)-1,12):
			finalDict[str(fromYear)][x] = finalDict[str(fromYear)][x] + 1 






with open('/Users/prathamtheempowerer/Desktop/FINAL.csv', 'rb') as inp:
	reader = csv.reader(inp)
	nextRow = reader.next();
	while i<5000000:
		workOn = []
		row = nextRow
		nextRow = reader.next()
		i = i+1
		while nextRow[0] == row[0] and i < 5000000:
			workOn.append(row)
			row = nextRow
			nextRow = reader.next()
			i = i+1

		workOn.append(row)
		#Work on now has the exact records from a single customer. Hence the name workOn :P

		count = 0
		if len(workOn) == 1:

			value = workOn[0]
			# print "procssing single entry"
			if (int(time.strftime("%Y")) - int(value[1]) > 1):
				# print "customer: " + str(value[0]) + " lapsed from " + str(value[2]) + "/" + str(int(value[1]) + 1) + " to " + time.strftime("%m") + "/" + time.strftime("%Y")
				addToFinalMatrix(value[2],value[1],time.strftime("%m"),time.strftime("%Y"))
			elif (int(value[1]) < int(time.strftime("%Y"))) and (int(value[2]) < int(time.strftime("%m"))):
				# print "customer: " + str(value[0]) + " lapsed from " + str(value[2]) + "/" + str(int(value[1]) + 1) + " to " + time.strftime("%m") + "/" + time.strftime("%Y")
				addToFinalMatrix(value[2],value[1],time.strftime("%m"),time.strftime("%Y"))
		else:
			for x in xrange(len(workOn)-1):
				# print "iteration " + str(count)
				count = count + 1
				one  = workOn[x]
				two  = workOn[x+1]

				if int(one[1])<int(two[1]) and int(one[2])<int(two[2]):
					# print "customer: " + str(one[0]) + " lapsed from " + str(one[2]) + "/" + str(int(one[1]) + 1) + " to " + str(two[2]) + "/" + str(two[1])
					addToFinalMatrix(one[2],one[1],two[2],two[1])
				elif (int(two[1]) - int(one[1]))>1:
					# print "customer: " + str(one[0]) + " lapsed from " + str(one[2]) + "/" + str(int(one[1]) + 1) + " to " + str(two[2]) + "/" + str(two[1])
					addToFinalMatrix(one[2],one[1],two[2],two[1])
				

				if (int(time.strftime("%Y")) - int(two[1]) > 1) and x == (len(workOn)-2):
					# print "customer: " + str(two[0]) + " lapsed from " + str(two[2]) + "/" + str(int(two[1]) + 1) + " to " + time.strftime("%m") + "/" + time.strftime("%Y")
					addToFinalMatrix(one[2],one[1],time.strftime("%m"),time.strftime("%Y"))
				elif (int(two[1]) < int(time.strftime("%Y"))) and (int(two[2]) < int(time.strftime("%m"))) and (x == len(workOn)-2):
					# print "customer: " + str(two[0]) + " lapsed from " + str(two[2]) + "/" + str(int(two[1]) + 1) + " to " + time.strftime("%m") + "/" + time.strftime("%Y")
					addToFinalMatrix(one[2],one[1],time.strftime("%m"),time.strftime("%Y"))

print finalDict
outFile = open("/Users/prathamtheempowerer/Desktop/out.csv","wb")
csvWriter = csv.writer(outFile)
csvWriter.writerow([" ","Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"])

for key in finalDict:
	cool = [str(key)]
	cool = cool + finalDict[key]
	csvWriter.writerow(cool)




