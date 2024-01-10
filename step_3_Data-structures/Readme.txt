1_work-with-strings:

	It reads a string of characters from the input and applies the following changes:

Removes all vowel letters.
Prints a dot before each consonant letter.
Writes all remaining consonant letters in lowercase.

Example:
Input:
aBAcAba

Output:
.b.c.b

2_sum-of-numbers:

	Numeric expressions like the one below will be sorted in ascending order when 
	you provide them to the program.

Example:
Input:
1+1+3+1+3

Output:
1+1+1+3+3

3_standardization:

	When you provide a list of 10 names like the example below to the program, 
	the program will standardize all the names.

Example:
Input:
BaHram
MaHnaZ
hooman
FaribORZ
barAN
HedieH
ALI
EZATOLLAH
MOHAMADALI
JAMSHID

Output:
Bahram
Mahnaz
Hooman
Fariborz
Baran
Hedieh
Ali
Ezatollah
Mohamadali
Jamshid

4_say-hello-correctly:

	If the letters forming "hello" appear in the correct order 
	in the input phrase you provide, it will indicate "YES" or 
	"NO" as shown in the examples below.

Examples:
Input:
ahhellllloou

Output:
YES


Input:
hlelo

Output:
NO

5_small-word:

	In this program, if you enter any word in a non-standard 
	and scrambled form, such as the example below, the program 
	will convert all the letters to lowercase.

Example:
Input:
hasTAM

Output:
hastam

6_is-palindrome-or-not:

	This program checks whether a word entered is a palindrome or not.

Example:
Input:
madam

Output:
palindrome

Input:
tehran

Output:
not palindrome

7_ABBA:

	With this program, you can find out whether a string contains the letters 
	"AB" or "BA" or not. If both of them exist without any overlapping, the 
	program will indicate "YES" or "NO" to you. For example, in "ABBA" and 
	"BAAB" they exist, but in "BHA" and "BAB" they do not.

Example:
Input:
AAABBBBBBBBBB

Output:
NO

8_Noruz:

	For example: On the occasion of the Persian New Year, three old friends 
	want to meet each other. Azarmehr, Azargoon, and Mehrayan plan to meet 
	at a single point. Their houses are located on a straight line (the x-axis).
	 Azarmehr's house is at point x1, Azargoon's house is at point x2, 
	and Mehrayan's house is at point x3. They want to minimize the total 
	distance they have to travel. By entering x1, x2, and x3, the program 
	calculates the minimum distance that the three friends need to travel in 
	total to meet at a single point. If the answer is an integer, it will be 
	printed without any decimal point.

Example:
Input:
6 9 10

Output:
4

9_kabaddy:

	For example, the officials of the national Kabaddi federation are preparing teams 
	to participate in the World Kabaddi Championships. According to the rules of the 
	World Kabaddi Championships, each individual can only participate in 5 World Kabaddi 
	matches. The federation president has gathered all the athletes of this sport together, 
	and each player has participated in a certain number of World Championships matches 
	up to now. Kabaddi teams consist of exactly 3 members. Now, Mr. Shayan Ariamehr, 
	the president of the federation, wants to form teams that, if selected, can compete 
	together in the World Championships for at least 3 years (meaning each member of a 
	team has participated in the World Championships a maximum of 2 times).

	The first line of input consists of a number, n, which represents the desired number 
	of Kabaddi players. The next line of input contains n numbers separated by spaces, 
	indicating how many times each player has participated in the World Championships. 
	The program will print a single number in the output, indicating the maximum number 
	of teams that can be formed under the given conditions.

Example:
Input:
6
5 0 4 2 1 0

Output:
1

10_notebook-price:

	For example, one day Sindokht and Irsa were having a discussion about the prices and 
	quality of laptops. Sindokht guessed that the more expensive a laptop is, the better 
	its quality. However, Irsa claims that she can find two laptops where the price of 
	the first one is lower than the second one, but the quality of the first one is 
	higher, thus challenging Sindokht's assumption. Now, this program helps Irsa verify 
	her claim.

	You provide the specifications of n laptops to the program. The first line of input 
	contains a number, n, indicating the number of laptops. Each of the following n 
	lines contains two numbers representing the price and quality of each laptop. If the 
	program can find two laptops that meet the conditions stated by Irsa, it will print 
	"happy irsa." Otherwise, it will print "poor irsa."

Example:
Input:
2
1 10
7 3

Output:
happy irsa


Input:
4
1 5
7 9
5 6
20 30

Output:
poor irsa

11_Vote-counting-system:

	For example, Mr. Zhoubin Artabaz, the head of the United Nations, is about to 
	conduct a voting for the election of the executive committee! Dadmehr Jamshidi, 
	the UN's computer officer, has written a program that counts the number of 
	votes each country has received. This program is intended to assist Dadmehr in 
	tallying the votes.

	The first line of input consists of a number, n, which represents the total number 
	of votes. Each of the following n lines contains the name of a country. The names 
	of the countries are written in lowercase English letters.

	The output will consist of m lines, each line displaying the number of votes 
	for each country. The country names will be written in alphabetical order in 
	the output.

Example:
Input:
5
sara
hamid
ali
sara
sara

Output:
ali 1
hamid 1
sara 3

12_translator:

	For example, Sindokht is preparing an online translator for her university thesis. 
	The online translator that Sindokht is working on has a dictionary, and in the end, 
	this translator should translate a sentence.

	The first line of input contains a number, n, which represents the total number of 
	dictionary words. Each of the following n lines contains two words, indicating that 
	the second word is the translation of the first word. The next line contains a 
	sentence. A sentence consists of multiple words separated by spaces. Now, the 
	program helps Sindokht by reading the corresponding sentence from the input and 
	translating it. During the translation process, if a word is not found in the 
	dictionary, the program prints the word itself in the output. Please refer to the 
	sample input and output for more information.

Example:
5
hello salam
goodbye khodafez
say goftan
we ma
you shoma
we say goodbye to you tonight

Output:
ma goftan khodafez to shoma tonight
