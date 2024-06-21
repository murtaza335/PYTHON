### Overview
The code implements a command-line Rock-Paper-Scissors game where a player competes against the computer. The player can choose how many rounds to play, and the program keeps track of scores and determines the overall winner.

### Code Description

#### 1. Importing the `random` Library
```python
import random
```
This line imports the `random` library, which is used to generate random choices for the computer.

#### 2. Initializing Scores
```python
c_score = p_score = 0
```
These lines initialize the computer's score (`c_score`) and the player's score (`p_score`) to zero.

#### 3. Function: `comp`
```python
def comp():
    c_choice = random.randint(1,3)
    if c_choice == 1:
        print("Comp : Rock")
    if c_choice == 2:
        print("Comp : Paper")
    if c_choice == 3:
        print("Comp : Scissor")
    return c_choice
```
This function generates a random choice for the computer: 1 for Rock, 2 for Paper, and 3 for Scissors. It prints the computer's choice and returns the value.

#### 4. Function: `player`
```python
def player():
    p_choice = input("select one:\nRock(r)\nPaper(p)\nScissor(s)\t")
    p_choice = p_choice.lower()
    if p_choice == "r":
        p_choice = 1
    elif p_choice == "p":
        p_choice = 2
    elif p_choice == "s":
        p_choice = 3
    else:
        print("Invalid choice")
        return player()
    return p_choice
```
This function prompts the player to make a choice (Rock, Paper, or Scissors), accepts the input as 'r', 'p', or 's', converts it to lowercase, and maps it to 1, 2, or 3 respectively. If the player enters an invalid choice, the function prompts again recursively.

#### 5. Function: `result`
```python
def result(p_choice, c_choice, p_score, c_score):
    if (p_choice == 1 and c_choice == 2) or (p_choice == 3 and c_choice == 1) or (p_choice == 2 and c_choice == 3):
        c_score += 1
    elif (c_choice == 1 and p_choice == 2) or (c_choice == 3 and p_choice == 1) or (c_choice == 2 and p_choice == 3):
        p_score += 1
    return p_score, c_score
```
This function determines the result of a round. It updates and returns the scores based on the player's and computer's choices using the rules of Rock-Paper-Scissors.

#### 6. Main Logic
```python
turns = int(input("How many games do you want to play?"))
for i in range(turns):
    p_choice = player()
    c_choice = comp()
    p_score, c_score = result(p_choice, c_choice, p_score, c_score)
print(f"Comp score: {c_score}\nPlayer score: {p_score}")
if c_score > p_score:
    print("Computer won")
elif p_score > c_score:
    print("You won")
else:
    print("Tie")
```
- The program prompts the user to input the number of rounds to play.
- In each round, it gets the player's choice, generates the computer's choice, determines the result, and updates the scores.
- After all rounds, it prints the final scores and declares the overall winner based on the scores.

### Summary
This Rock-Paper-Scissors game allows the player to play multiple rounds against the computer. The computer's choice is random, and the program keeps track of scores for both the player and the computer, ultimately declaring the winner based on the highest score. The game includes input validation and prompts the user for valid inputs.
