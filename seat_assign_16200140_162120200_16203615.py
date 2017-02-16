import sqlite3
import csv



class readCSV(object):

	def __init__(self,fileName):
		self.fileName=fileName
		self.bookingData=[]

	#reads csv file into bookingData variable
	def readFile(self):
		with open(self.fileName,'rb') as f:
			reader=csv.reader(f)
			for row in reader:
				self.bookingData.append(row)


class database(object):

	def __init__(self,fileName):
		self.fileName=fileName
		self.seatChars=[]

	#returns number of the rows in the plane from the database
	def getRows(self):
		conn=sqlite3.connect(self.fileName)
		c=conn.cursor()
		c.execute('Select nrows from rows_cols')
		rows = c.fetchone()[0]
		conn.close()
		return rows

	#returns number of columns in the plane and get column codes for seats from the database
	def getColumns(self):
		conn=sqlite3.connect(self.fileName)
		c=conn.cursor()
		c.execute('Select seats from rows_cols')
		cols = c.fetchone()[0]
		count=0
		for char in cols:
			self.seatChars.append(char)
			count=count+1
		conn.close()
		return count

	#returns the number of empty seats in a row
	def getEmptySeatsInRow(self):
		conn=sqlite3.connect(self.fileName)
		c=conn.cursor()
		cmd='Select count(seat) from seating where row=(?) and name is null'
		c.execute(cmd,(rowNumber,))
		emptySeats=c.fetchone()[0]
		print(rowNumber)
		conn.close()
		return emptySeats
		





class seatAllocator(object):

	def __init__(self,rows,columns):
		self.maxSeats=rows*columns
		self.rows=rows
		self.columns=columns
		self.seatsAvailable=self.maxSeats
		self.seatsBooked=0
		self.bookingsRefused=0
		self.awayPassengers=0
		self.seatsInRow=self.maxSeats/columns
		self.seatChars=[]


	def printInfo(self):
		print("Maximum number of seats: {}".format(self.maxSeats))
		print("Number of rows: {}".format(self.rows))
		print("Number of columns: {}".format(self.columns))
		print("Number of seats in a row: {}".format(self.seatsInRow))

	def checkSeats(self,requestedSeats):
		if(self.seatsAvailable<requestedSeats):
			print("Seats not available")
			self.bookingsRefused+=requestedSeats
			print("Total bookings refused till now {}".format(self.bookingsRefused))

	def bookSeat(self,)



database=database('data.db')
rows=database.getRows()
cols=database.getColumns()


booking=seatAllocator(rows,cols)
booking.seatChars=database.seatChars
booking.printInfo()


readCSV=readCSV('bookings.csv')
readCSV.readFile()


