# MIS40750AirlineSeating
Module : Analytics Research And Implementation
Name : Sharon Luk
Student Number : 16203615

1. Algorithm Implementation
The algorithm involves a recursive function which find the best positions to book for the passenger.
Take a table with 10 columns and 8 rows. 
If a passenger books for 7 seats, the output would be the following, passenger bookings are represented by T , C represents column, R represents row:

   C1 C2 C3 C4 C5 C6 C7 C8 C9 C10
R1 T1 T1 T1 T1 T1 T1 T1 
R2
R3
R4
R5
R6
R7
R8

If a second passenger decides to book 5 seats, the output would be the following :

   C1 C2 C3 C4 C5 C6 C7 C8 C9 C10
R1 T1 T1 T1 T1 T1 T1 T1 T2 T2 T2
R2                         T2 T2
R3
R4
R5
R6
R7
R8

It can also create seperate passenger group bookings if there are not enough empty positions :

   C1 C2 C3 C4 C5 C6 C7 C8 C9 C10
R1 T1 T1 T1 T1 T1 T1 T1 T2 T2 T2
R2 Ti Ti Ti Ti Ti       Ti T2 T2
R3 Ti Ti Ti Ti Ti       Ti Ti Ti
R4 Ti Ti Ti Ti Ti Ti Ti Ti Ti Ti
R5 Ti          Ti Ti Ti Ti Ti Ti
R6 Ti Ti Ti Ti Ti Ti Ti Ti Ti Ti
R7 Ti Ti Ti Ti Ti Ti Ti Ti Ti Ti
R8 Ti Ti Ti Ti Ti Ti Ti Ti

If the third passenger decided to book 7 seats, firstly the 4 seats would be found and then the remaining 3 seats
available followd by another seat :

   C1 C2 C3 C4 C5 C6 C7 C8 C9 C10
R1 T1 T1 T1 T1 T1 T1 T1 T2 T2 T2
R2 Ti Ti Ti Ti Ti T3 T3 Ti T2 T2
R3 Ti Ti Ti Ti Ti T3 T3 Ti Ti Ti
R4 Ti Ti Ti Ti Ti Ti Ti Ti Ti Ti
R5 Ti T3 T3 T3 Ti Ti Ti Ti Ti Ti
R6 Ti Ti Ti Ti Ti Ti Ti Ti Ti Ti
R7 Ti Ti Ti Ti Ti Ti Ti Ti Ti Ti
R8 Ti Ti Ti Ti Ti Ti Ti Ti T3

At this point, if a another passenger decides to book more than one seat eg 5 seats. The seat allocation will fail
as there is only one seat remaining.

The recursive function finds the positions of north,south, east and west to book seats accordingly as a whole.
In the cases of not having enough empty seats to book the group of passengers, the recursive function will create
seperated groups.

2. Running the program 


3. Testing
