

# The purpose of this program is to write a software algorithm to allocate seats when passengers make bookings.
# The inputs are data.db,bookings.csv and the output is data.db as required

import sqlite3 as lite
import sys
import csv

#file name of SQLite database 
databaseFilename = "data.db"

#file name for the bookings
csvFilename = "bookings.csv"  

#this function serves the purpose of printing the matrix for testing.
def matrixPrint(nrows, seats, seatings):
    
    for column in range(len(seats)): 

        print ("%15s" % seats[column], end='') 

    print ()
        
    for row in range(nrows):

        print (row + 1, end=' ')

        for column in range(len(seats)):

            print ("%15s" % seatings[row][column], end=' ')

        print ("")
        
#reading the number of rows and seats from the database
def readNumberOfRowsAndSeats():

    # the connection
    con = None 

    try:
        con = lite.connect(databaseFilename) #creating the connection to the database

        cur = con.cursor()   #creating the cursor  

        cur.execute('select nrows, seats from rows_cols')  #execute selecting the query

        data = cur.fetchone() #retrieving the first row

        return data # returning the data 
    
    except lite.Error:
        print ("There is an error in the database that is read")
        sys.exit(1)
    finally:
        if con: 
        #close  the connection
            con.close()

#firstly, read the cs file, return the number of passengers (list) and the name of the person making a airline booking)

def csvFileReading():
    
    seatBookings = [] #the list of bookings is initially empty

    
    with open(csvFilename, 'rt') as f: # read the file that is opened

        reader = csv.reader(f) # reading the file
        
        for row in reader: # for each row that is being read

            seatBookings.append(row);

    return seatBookings; #return the seat bookings

#loading the current seats of the airplane, the input could be seats such as ACDF and row numbers such as 15
def theLoadingOfSeats(nrows, flightSeats):
    
    airplaneSeatings = [['' for c in range(len(flightSeats))] for r in range(nrows)] 
    
    con = None #connection

    try:

        #create connection to database
        con = lite.connect(databaseFilename)

        #create the cursor
        current = con.cursor()   

        #execute select query
        current.execute('select row, seat, name from seating')

        #retrieve the records
        data = current.fetchall()
        
        for row in data:
            airplaneSeatings[row[0] - 1][flightSeats.index(row[1])] = row[2]
    
    except lite.Error:

        print (" There is an error in read database")
        sys.exit(1)

    finally:
        if con: #exit the connection
            con.close()
            
    return airplaneSeatings
    
#copy all the airplane seatings and return the flight seats
def airplaneSeatingsCopy(seatings):

    flightPassengerSeatsCopy = [['' for column in range(len(seats))] for row in range(nrows)] 
    
    for row in range(nrows):

        for column in range(len(seats)):

            flightPassengerSeatsCopy[row][column] = seatings[row][column]

    return flightPassengerSeatsCopy

# Implementing the algorithm for the recursive function to extend the empty position to all the directions, left , right, up, bottom
#return the seats that are seperated and then update the  matrix , request that is false fails

def findEmptySeatNumbers(row, column, theNumber, numberOfrows, flightSeats, theSeatings):

# if the quantity of empty seats is 0
    if theNumber == 0:
        return theNumber
    if theSeatings[row][column] != '':
        return theNumber
    
    #if the seat is occupied or taken, mark it with T
    theSeatings[row][column] = 'T'
    theNumber = theNumber - 1
    
    #find empty seat at right hand side ( west)
    if column > 0:
        theNumber = findEmptySeatNumbers(row, column - 1, theNumber, numberOfrows, flightSeats, theSeatings)
        if theNumber == 0:
            return theNumber

    #find empty seat at left hand side ( east)
    if column < len(flightSeats) - 1:
        theNumber = findEmptySeatNumbers(row, column + 1, theNumber, numberOfrows, flightSeats, theSeatings)
        if theNumber == 0:
            return theNumber
        
    #find empty seat above (North)
    if row > 0:
        theNumber = findEmptySeatNumbers(row - 1, column, theNumber, numberOfrows, flightSeats, theSeatings)
        if theNumber == 0:
            return theNumber

    #find empty seat below (south)
    if row < numberOfRows - 1:
        theNumber = findEmptySeatNumbers(row + 1, column, theNumber, numberOfrows, flightSeats, theSeatings)
        if theNumber == 0:
            return theNumber
    
    return theNumber

#find all the empty seats on the flight
#Until all empty seats are found (or some empty seats) , find the best positions (or any empty seat is unavailable)
#Returns the quantity of  seats remaining that can NOT be allocated
#If there is no empty seat found then return false. 

def searchEmptySeatPositions(theNumber, numberOfRows, seats, theSeatings):    
    
    seatSeparation = -1    
    
    copyFlightSeats = airplaneSeatingsCopy(theSeatings)
    seatRemainder = theNumber
   

    while True:

        idealNumber = seatRemainder
        bestflightPassengerSeatsCopy = airplaneSeatingsCopy(copyFlightSeats)
     
        
        for row in range(numberOfRows):

            for column in range(len(seats)):

                if copyFlightSeats[row][column] == '':

                    #(call recursive function)creating a copy of all seats and trying to find best location 
                    flightPassengerSeatsCopy = airplaneSeatingsCopy(copyFlightSeats)               
                    aRandomNumber = findEmptySeatNumbers(row, column, seatRemainder, numberOfRows, seats, flightPassengerSeatsCopy)

                    if aRandomNumber < idealNumber:

                        idealNumber = aRandomNumber

                        bestflightPassengerSeatsCopy = flightPassengerSeatsCopy
                        
        copyFlightSeats = bestflightPassengerSeatsCopy
        
    
        # if all the seats are taken then return 0 which is false
        if idealNumber == seatRemainder: 
            return 0, False
        
        #seting the seats which are seperated
        if seatSeparation == 0:
            seatSeparation = seatRemainder
        
        #set the remaining seat
        seatRemainder = idealNumber
        
        if seatRemainder == 0: 
            return seatSeparation, copyFlightSeats
        else:
            
            if seatSeparation == -1:
                seatSeparation = 0
             
#for every customer booking ,try to allocate the seats together if it is possible in a row
# seating and metrics table is updated
def flightSeatingAssign(numberOfRows, seats, theSeatings, bookings):
    
    for booking in bookings:
        customerName = booking[0]
        theNumber = int(booking[1])
        
        print (customerName, theNumber)
        
        seatSeparation, outcome = searchEmptySeatPositions(theNumber, numberOfRows, seats, theSeatings)

        if outcome == False:

            #saving to metrics ( standard of measurement)
            print ("Sorry, failed to assign flight seatings")
            
            #updating all the metrics , refusal of passenger
            measurementRenewal(theNumber, 0)
        
        else:
            theSeatings = outcome
            
            #update matrix and save to database
            for row in range(numberOfRows):
                for column in range(len(seats)):
                    if theSeatings[row][column] == 'X':
                        theSeatings[row][column] = customerName
                        #update seating 
                        customerSeatUpdates(row + 1, seats[column], customerName)
    
            #updating the standard of measurement 

            if seatSeparation != -1:
                print ("the separated seats are ", seatSeparation)
                
                #update metrics as passengers are seperated 
                measurementRenewal(0, seatSeparation)
        
        matrixPrint(numberOfRows, seats, theSeatings)
    
    

