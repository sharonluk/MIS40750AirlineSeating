# MIS40750AirlineSeating
Module : Analytics Research And Implementation
Name : Sharon Luk
Student Number : 16203615

Name : Apoorva Taneja
Studnt Number : 16200140

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

