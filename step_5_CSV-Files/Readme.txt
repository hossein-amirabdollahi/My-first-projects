1_calculate-and-sort:

	In this project, the program reads grades of different individuals from a CSV file 
	and performs the following calculations on the grades, saving the results in an output file.

	There are 5 different tasks implemented in this project:

	1_It calculates the average grade for each individual and saves it along with their name. 
	  The order of the output should exactly match the order of the input file.

	2_It calculates the average grades in ascending order along with the names of the individuals.

	3_It saves the top three average grades along with the names of the individuals.

	4_It saves the bottom three average grades without the names of the individuals.

	5_It calculates the average of all the average grades and saves it.

Example:
Input:
mandana,5,7,3,15
hamid,3,9,4,20,9,1,8,16,0,5,2,4,7,2,1
sina,19,10,19,6,8,14,3
sara,0,5,20,14
soheila,13,2,5,1,3,10,12,4,13,17,7,7
ali,1,9
sarvin,0,16,16,13,19,2,17,8

Task 1 output:
mandana,7.5
hamid,6.066666666666666
sina,11.285714285714286
sara,9.75
soheila,7.833333333333333
ali,5.0
sarvin,11.375

Task 2 output:
ali,5.0
hamid,6.066666666666666
mandana,7.5
soheila,7.833333333333333
sara,9.75
sina,11.285714285714286
sarvin,11.375

Task 3 output:
sarvin,11.375
sina,11.285714285714286
sara,9.75

Task 4 output:
5.0
6.066666666666666
7.5

Task 5 output:
8.401530612244898

	Please note that in each task, if multiple individuals have the same average grade, 
	the order of the output will be alphabetically sorted. For example:

hossein 16.5
mona 16.5