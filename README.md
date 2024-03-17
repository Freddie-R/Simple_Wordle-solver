Wordle Solver Program Readme

Description:
This program is designed to solve Wordle, a word-guessing game where the player tries to guess a secret five-letter word within a limited number of attempts. The program utilizes various strategies to make educated guesses and optimize the guessing process.

Files:
1. Getnow.py: Contains functions to fetch a list of valid five-letter words.
2. Notit.py: Contains functions to filter out words based on letters not present in the secret word.
3. Yellow.py: Contains functions to identify letters that are present in the secret word but in the wrong position.
4. Green.py: Contains functions to identify letters that are present in the secret word and in the correct position.
5. Score.py: Contains functions to score potential guesses based on their likelihood of being the secret word.
6. Return.py: Contains functions to handle returning a guessed word to the main program after evaluation.
7. average.py: Contains functions for calculating averages and statistical measures.
8. Input.py: Contains functions for user input and interaction.
9. scorept.py: Contains functions for scoring potential guesses based on various criteria.
10. main.py: The main program file that orchestrates the solving of Wordle.

Usage:
1. Ensure all Python files are in the same directory.
2. Run the WordleSolver.py file with appropriate parameters.
3. Follow on-screen instructions, if any, to input any required information.
4. When prompted to input a guessed word, use the following color code: 
   - Use '0' for gray (letters not present in the word).
   - Use '1' for yellow (letters present but in the wrong position).
   - Use '2' for green (letters present and in the correct position).

How to Run:
1. Open a terminal or command prompt.
2. Navigate to the directory containing the program files.
3. Run the command: python WordleSolver.py

Parameters:
- do_user: Boolean value indicating whether user interaction is enabled. Set to True to enable user input for each guess.
- total: Number of iterations or games to play. Determines how many times the program attempts to solve Wordle.
- wordset: (Optional) If provided, specifies a predetermined word for the program to attempt to solve. If left empty, the program will randomly select a word to solve for each iteration.

Output:
- The program prints the progress of each game, including the number of guesses made and the guessed words.
- Upon completion, it provides statistics such as the average number of guesses required across all games.

Example:
python WordleSolver.py

Note:
- This program is designed for educational and entertainment purposes. It aims to demonstrate various strategies for solving Wordle efficiently.
- Feel free to explore and modify the source code to enhance its functionality or adapt it to different word-guessing games.

Author:
Freddie R
GitHub: https://github.com/Freddie-R
