1_guess:

	The steps of the game are as follows:

	The user thinks of a number between 1 and 99 without telling the computer
	 (no input is given to the program).

	The program is executed.

	The program guesses a number and prints it.

	The printed number creates three possibilities:

	a. If the printed number is greater than the number in the user's mind, 
	the user types "less" to inform the program that the number in their mind is smaller. 
	The program should guess another number and display it.

	b. If the printed number is smaller than the number in the user's mind, 
	the user types "more" to inform the program that the number in their mind is greater. 
	The program should guess another number and display it.

	c. If the printed number is the same as the number in the user's mind, 
	the user types "right" to inform the program that it has guessed correctly. 
	The program ends.

2_prime-numbers:

	you enter a positive integer, and the program tells you whether the number is prime or not.

input:
23

output:
prime

3_sepidrud-dasht:

	In this program, the score that Team A has achieved in the Premier League matches 
	is received as input, and the program prints the total points of Team A along with 
	the number of victories in this season. Team A plays 30 matches in the Premier League, 
	so the scores of this team are given to the program in 30 lines. For each match, 
	Team A either earns 0 points, 1 point, or 3 points. In the case of a loss, 
	the team earns 0 points, in the case of a draw, it earns 1 point, and in the case of a win, 
	it earns 3 points.

for example:

input:
3
3
3
3
3
0
0
0
0
0
1
1
1
1
1
3
3
3
3
3
0
0
0
0
0
1
1
1
1
1

output:
40 10

4_oldest:

	This program reads the ages of candidates for the Consultative Assembly 
	from the input and prints the highest age among them in the output. The program 
	continues reading from the input until a negative number is entered. Once this 
	number appears in the input, the program terminates the input reading and prints 
	the highest age. The age of individuals is in the range of 10 to 90 years.

Example:

Input:
17
15
39
51
14
32
28
-1

Output:
51

5_two-oldest:

	This program reads the ages of candidates for the Council Assembly
	from the input and prints the highest and second-highest ages among 
	them in the output. The program continues reading from the input 
	until a negative number is entered. Once this number appears in 
	the input, the program terminates the input reading and prints the 
	highest age. The age of individuals is in the range of 10 to 90 years. 
	It must be ensured that the ages of candidates in the input are unique 
	(i.e., no two individuals have the same age in the input).

Example:
Input:
17
15
39
51
14
32
28
-1

Output:
51 39

6_number-of-divisors:

	This program reads 20 numbers from the input and, in the end, 
	prints the number with the highest number of divisors along 
	with the count of its divisors in the output. If multiple numbers 
	have the same maximum number of divisors, it prints the largest among them.

Example:
Input:
767
665
999
895
907
796
561
914
719
819
555
529
672
933
882
869
801
660
879
985

Output:
672 24