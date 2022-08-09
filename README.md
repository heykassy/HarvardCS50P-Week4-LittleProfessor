# HarvardCS50P-Week4-LittleProfessor

CS50P's Introduction to Programming with Python
Week 4, Problem Set 4

Project specifications:

"Little Professor
One of David’s first toys as a child, funny enough, was Little Professor, a “calculator” that would generate ten different math problems for David to solve. For instance, if the toy were to display 4 + 0 = , David would (hopefully) answer with 4. If the toy were to display 4 + 1 = , David would (hopefully) answer with 5. If David were to answer incorrectly, the toy would display EEE. And after three incorrect answers for the same problem, the toy would simply display the correct answer (e.g., 4 + 0 = 4 or 4 + 1 = 5).

In a file called professor.py, implement a program that:

Prompts the user for a level, . If the user does not input 1, 2, or 3, the program should prompt again.
Randomly generates ten (10) math problems formatted as X + Y = , wherein each of X and Y is a non-negative integer with  digits. No need to support operations other than addition (+).
Prompts the user to solve each of those problem. If an answer is not correct (or not even a number), the program should output EEE and prompt the user again, allowing the user up to three tries in total. If the user has still not answered correctly after three tries, the program should output the correct answer.
The program should ultimately output the user’s score, a number out of 10.
Structure your program as follows, wherein get_level prompts (and, if need be, re-prompts) the user for a level and returns 1, 2, or 3, and generate_integer returns a randomly generated non-negative integer with level digits or raises a ValueError if level is not 1, 2, or 3:

import random


def main():
    ...


def get_level():
    ...


def generate_integer(level):
    ...


if __name__ == "__main__":
    main()

How to Test
Here’s how to test your code manually:

Run your program with python professor.py. Type -1 and press Enter. Your program should reprompt you:
Level:   
Run your program with python professor.py. Type 4 and press Enter. Your program should reprompt you:
Level:   
Run your program with python professor.py. Type 1 and press Enter. Your program should begin posing addition problems with positive, single-digit integers. For example:
6 + 6 =    
Your program should output 10 distinct problems before printing the number of questions you answered correctly and exiting.

Run your program with python professor.py. Type 1 and press Enter. Answer the first question incorrectly. Your program should output:
EEE
before reprompting you with the same question.

Run your program with python professor.py. Type 1 and press Enter. Answer the first question incorrectly, three times. Your program should output the correct answer. For example:
6 + 6 = 12
and then move on to another question. Answer the remaining questions correctly. Your program should output a score of 9.

Run your program with python professor.py. Type 1 and press Enter. Answer all 10 questions correctly. Your program should output a score of 10.
"
