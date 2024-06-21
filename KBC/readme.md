This Python script implements a text-based quiz game inspired by "Kaun Banega Crorepati" (KBC), where players answer multiple-choice questions across three levels to win virtual money. Here's a breakdown of the code and its functionality:

### Functions Overview:

1. **PRINT_OPTIONS(_options)**:
   - Prints the four options (a, b, c, d) for a given question.

2. **CHECK_ANSWER(_user_input, _correct_option)**:
   - Compares user input with the correct option and returns True/False.

3. **PRINT_Q_OP(rand_list, questions, options, correct_option)**:
   - Randomly selects and prints a question from the provided lists (`questions`, `options`, `correct_option`).
   - Ensures each question is asked only once using `rand_list`.

4. **RICHES_QUESTION_BANK(rand_list=[]), MILLIONER_QUESTION_BANK(rand_list=[]), ULTIMATE_QUESTION_BANK(rand_list=[])**:
   - Each function provides a set of questions, options, and correct answers for its respective level.
   - Calls `PRINT_Q_OP()` to display a random question.

5. **INPUT_ANSWER()**:
   - Takes user input for the answer (a, b, c, d).
   - Validates the input to ensure it's one of the options.

6. **GAME_OVER(_level)**:
   - Prints a game over message when the user answers more than two questions incorrectly in a level.

7. **LEVEL_PRIZE(_level)**:
   - Returns the prize money corresponding to the level.

8. **LEVEL_NAME(_level)**:
   - Returns the name of the level based on the level number.

9. **LEVEL_COMPLETE_THEN_LEAVE(_level, _level_name, _prize)**:
   - Displays a congratulations message when the user completes a level and chooses to leave the game.

10. **WON_ALL_LEVEL(_level)**:
    - Displays a congratulations message when the user completes all three levels.

11. **ASK_NEXT_LEVEL(_level, _level_name, _prize)**:
    - Asks the user whether they want to proceed to the next level or leave the game after completing a level.

12. **LEVEL_COMPLETE(_level)**:
    - Handles tasks after completing a level (e.g., calling `ASK_NEXT_LEVEL()` or `WON_ALL_LEVEL()`).

13. **LEVEL(_game_over, _level)**:
    - Main function to execute each level of the game.
    - Calls respective question banks (`RICHES_QUESTION_BANK()`, `MILLIONER_QUESTION_BANK()`, `ULTIMATE_QUESTION_BANK()`).
    - Tracks the number of wrong answers (`_game_over`).
    - Handles game over conditions and level completion.

14. **START_GAME(_current_balance=0, _level=1)**:
    - Initiates the game by calling `LEVEL()` for the first level.

15. **MENU_CHOICE(_choice)**:
    - Executes actions based on user menu choice (start game, view instructions, exit game).

16. **MAIN_MENU()**:
    - Displays the main menu and takes user input to navigate through the game.

17. **INSTRUCTIONS()**:
    - Provides instructions about the game's rules and mechanics.
    - Allows users to return to the main menu after reading.

### Execution Flow:
- The game starts with `MAIN_MENU()`, where users can choose to start the game, view instructions, or exit.
- `START_GAME()` begins the game loop, starting from Level 1.
- Each level (`LEVEL()`) presents 10 questions randomly selected from its respective question bank.
- After completing each level, the user can choose to proceed to the next level or leave the game.
- If the user answers more than two questions incorrectly in a single level, `GAME_OVER()` is called.
- After completing all three levels successfully, `WON_ALL_LEVEL()` congratulates the user.

### Additional Notes:
- The game employs `random` module for random question selection and `os` module for clearing the screen and exiting gracefully.
- Input validation ensures users can only enter valid answer choices (a, b, c, d).

This game structure offers a fun and interactive way for users to test their knowledge while simulating the format of a popular quiz show.
