import random
c_score = p_score = 0
def comp():
    c_choice = random.randint(1,3)
    if c_choice==1:
        print("Comp : Rock")
    if c_choice==2:
        print("Comp : Paper")
    if c_choice==3:
        print("Comp : Scissor")

    return c_choice

def player():
    p_choice = input("select one:\nRock(r)\nPaper(p)\nScissor(s)\t")
    p_choice.lower()
    if p_choice == "r":
        p_choice = 1
    elif p_choice == "p":
        p_choice = 2
    elif p_choice == "s":
        p_choice = 3
    else:
        print("Invalid choice")
        player()
    return p_choice
def result(p_choice,c_choice,p_score,c_score):
    if (p_choice == 1 and c_choice == 2) or (p_choice == 3 and c_choice == 1) or (p_choice == 2 and c_choice == 3):
        c_score +=1
    elif (c_choice == 1 and p_choice == 2) or (c_choice == 3 and p_choice == 1) or (c_choice == 2 and p_choice == 3):
        p_score +=1
    return p_score,c_score


turns = int(input("How many games do you want to play ?"))
for i in range(turns):
    p_choice = player()
    c_choice = comp()
    p_score,c_score = result(p_choice,c_choice,p_score,c_score)
print(f"Comp score : {c_score}\nPlayer score: {p_score}")
if c_score > p_score:
    print("Computer won")
elif p_score > c_score:
    print("You won")
else:
    print("Tie")