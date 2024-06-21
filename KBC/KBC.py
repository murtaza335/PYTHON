import random
import os


# this function just prints options
def PRINT_OPTIONS(_options):
    print("a. ", _options[0])
    print("b. ", _options[1])
    print("c. ", _options[2])
    print("d. ", _options[3])


# this functions compares user input with the correct option and returns true/false
def CHECK_ANSWER(_user_input, _correct_option):
    return _user_input == _correct_option


# ================================
# this function displays the question and options.
def PRINT_Q_OP(rand_list, questions, options, correct_option):
    # a random number is generated from 0 to len(questions)
    _rand = random.randrange(0, len(questions))
    # a rand_list is generated so that it stores the previous randomly selected indexes byr random function.
    # if the randomly selected index is already present in the rand_list then a new random number is generated.
    # if the randomly selected index is not present in the rand_list then the index is appended to the rand_list.
    # the question is printed and the options are printed.
    # finally the correct option is returned.
    while (_rand in rand_list):
        _rand = random.randrange(0, len(questions))
    rand_list.append(_rand)
    print(questions[_rand])
    PRINT_OPTIONS(options[_rand])
    print(correct_option[_rand])
    return correct_option[_rand]


# ================================
#  LEVEL 1: PATH TO RICHES --> this function acts like a question bank of the level 1  and returns the _coorect_option
def RICHES_QUESTION_BANK(rand_list=[]):
    questions = [
        "What is the capital city of Pakistan?",
        "Who is the founder of Pakistan?",
        "What is the national language of Pakistan?",
        "Which river is the longest in Pakistan?",
        "What is the national animal of Pakistan?",
        "In which year did Pakistan gain independence?",
        "Who was the first Prime Minister of Pakistan?",
        "What is the currency of Pakistan?",
        "Which city is known as the 'City of Lights' in Pakistan?",
        "What is the national flower of Pakistan?",
        "Which mountain is the highest in Pakistan?",
        "Who is known as the 'Poet of the East' in Pakistan?",
        "What is the national sport of Pakistan?",
        "Which sea borders Pakistan to the south?",
        "What is the name of Pakistan's national anthem?",
        "Which province is the largest by area in Pakistan?",
        "What is the official religion of Pakistan?",
        "Who was the first female Prime Minister of Pakistan?",
        "Which desert is located in Pakistan?",
        "What is the main export product of Pakistan?"
    ]
    options = [
        ["Karachi", "Islamabad", "Lahore", "Peshawar"],  # Correct: Islamabad
        [
            "Allama Iqbal", "Liaquat Ali Khan", "Benazir Bhutto",
            "Quaid-e-Azam Muhammad Ali Jinnah"
        ],  # Correct: Quaid-e-Azam Muhammad Ali Jinnah
        ["English", "Urdu", "Punjabi", "Sindhi"],  # Correct: Urdu
        ["Jhelum", "Indus", "Chenab", "Ravi"],  # Correct: Indus
        ["Snow Leopard", "Markhor", "Chukar",
         "Houbara Bustard"],  # Correct: Markhor
        ["1948", "1950", "1947", "1952"],  # Correct: 1947
        [
            "Zulfikar Ali Bhutto", "Nawaz Sharif", "Benazir Bhutto",
            "Liaquat Ali Khan"
        ],  # Correct: Liaquat Ali Khan
        ["Dollar", "Euro", "Pakistani Rupee",
         "Pound"],  # Correct: Pakistani Rupee
        ["Islamabad", "Lahore", "Rawalpindi", "Karachi"],  # Correct: Karachi
        ["Rose", "Jasmine", "Tulip", "Sunflower"],  # Correct: Jasmine
        ["Nanga Parbat", "Broad Peak", "K2", "Gasherbrum I"],  # Correct: K2
        ["Faiz Ahmed Faiz", "Allama Iqbal", "Mirza Ghalib",
         "Ahmad Faraz"],  # Correct: Allama Iqbal
        ["Cricket", "Football", "Squash", "Hockey"],  # Correct: Hockey
        ["Bay of Bengal", "Arabian Sea", "Persian Gulf",
         "Red Sea"],  # Correct: Arabian Sea
        [
            "Jeevay Jeevay Pakistan", "Qaumi Taranah", "Sohni Dharti",
            "Ae Rah-e-Haq Ke Shaheedo"
        ],  # Correct: Qaumi Taranah
        ["Sindh", "Punjab", "Balochistan",
         "Khyber Pakhtunkhwa"],  # Correct: Balochistan
        ["Hinduism", "Islam", "Christianity", "Sikhism"],  # Correct: Islam
        [
            "Fatima Jinnah", "Benazir Bhutto", "Hina Rabbani Khar",
            "Asma Jahangir"
        ],  # Correct: Benazir Bhutto
        ["Cholistan Desert", "Thar Desert", "Kharan Desert",
         "Nara Desert"],  # Correct: Thar Desert
        ["Rice", "Textiles", "Wheat", "Mangoes"]  # Correct: Textiles
    ]
    correct_option = [
        "b",  # Islamabad
        "d",  # Quaid-e-Azam Muhammad Ali Jinnah
        "b",  # Urdu
        "b",  # Indus
        "b",  # Markhor
        "c",  # 1947
        "d",  # Liaquat Ali Khan
        "c",  # Pakistani Rupee
        "d",  # Karachi
        "b",  # Jasmine
        "c",  # K2
        "b",  # Allama Iqbal
        "d",  # Hockey
        "b",  # Arabian Sea
        "b",  # Qaumi Taranah
        "c",  # Balochistan
        "b",  # Islam
        "b",  # Benazir Bhutto
        "b",  # Thar Desert
        "b"  # Textiles
    ]
    # PRINT_Q_OP() is called to print the question
    _correct_option = PRINT_Q_OP(rand_list, questions, options, correct_option)
    return _correct_option


# ================================
# LEVEL2 : MILLIONER'S LADDER --> this function acts like a question bank of the level 2  and returns the _coorect_option
def MILLIONER_QUESTION_BANK(rand_list=[]):
    questions = [
        "What is the capital of Azerbaijan?",
        "Who is the author of 'The Catcher in the Rye'?",
        "What is the chemical symbol for mercury?",
        "What is the largest moon of Jupiter?",
        "Who painted the famous artwork 'Guernica'?",
        "What is the tallest mountain in North America?",
        "Who wrote the 'Divine Comedy'?",
        "What is the chemical symbol for tungsten?",
        "What is the deepest part of the ocean?",
        "Who composed the opera 'The Magic Flute'?",
        "What is the currency of South Africa?",
        "Who discovered the law of gravitation?",
        "What is the largest organ in the human body?",
        "What is the main component of Earth's atmosphere?",
        "Who won the Nobel Prize in Literature in 2020?",
        "What is the longest river in Asia?",
        "Who developed the theory of natural selection?",
        "What is the chemical symbol for silver?",
        "What is the speed of light in a vacuum?",
        "Who is the Greek god of the sea?"
    ]
    options = [
        ["Dhaka", "Tehran", "Islamabad", "Baku"],
        ["Harper Lee", "F. Scott Fitzgerald", "J.D. Salinger", "Ernest Hemingway"],
        ["Hg", "Md", "Sn", "Rn"],
        ["Callisto", "Europa", "Ganymede", "Io"],
        ["Pablo Picasso", "Vincent van Gogh", "Claude Monet", "Salvador Dali"],
        ["Mount Denali", "Mount Kilimanjaro", "Mount Everest", "Mount Aconcagua"],
        ["Geoffrey Chaucer", "John Milton", "Dante Alighieri", "William Shakespeare"],
        ["W", "Tn", "Tg", "Te"],
        ["Sunda Trench", "Mariana Trench", "Java Trench", "Puerto Rico Trench"],
        ["Giuseppe Verdi", "Ludwig van Beethoven", "Wolfgang Amadeus Mozart", "Richard Wagner"],
        ["Peso", "Rand", "Yuan", "Real"],
        ["Albert Einstein", "Galileo Galilei", "Isaac Newton", "Niels Bohr"],
        ["Brain", "Liver", "Kidney", "Pancreas"],
        ["Carbon Dioxide", "Oxygen", "Nitrogen", "Helium"],
        ["Kazuo Ishiguro", "Peter Handke", "Olga Tokarczuk", "Louise Glück"],
        ["Ganges", "Yangtze", "Mekong", "Nile"],
        ["Charles Darwin", "Gregor Mendel", "Alfred Russel Wallace", "Thomas Huxley"],
        ["Ag", "Ti", "Sn", "Sb"],
        ["299,792,458 m/s", "300,000,000 m/s", "299,792,458 km/s", "300,000 km/s"],
        ["Zeus", "Poseidon", "Hades", "Athena"]
    ]
    correct_option = [
        "d",
        "a",
        "a",
        "c",
        "a",
        "b",
        "d",
        "a",
        "b",
        "c",
        "c",
        "a",
        "a",
        "b",
        "d",
        "b",
        "a",
        "a",
        "a",
        "a"
    ]
    _correct_option = PRINT_Q_OP(rand_list, questions, options, correct_option)
    return _correct_option


# ================================
#  LEVEL3 : ULTIMATE FORTUNE --> this function acts like a question bank of the level 3  and returns the _coorect_option
def ULTIMATE_QUESTION_BANK(rand_list=[]):
    questions = [
        "Which country has the highest rate of deforestation in the Amazon Rainforest?",
        "What is the primary objective of China's Belt and Road Initiative?",
        "Which pollutant is most commonly responsible for the severe air quality issues in Delhi and Beijing?",
        "What year did the European Union implement the General Data Protection Regulation (GDPR)?",
        "How many Sustainable Development Goals (SDGs) were set by the United Nations for the 2030 agenda?",
        "Which European country experienced a significant rise in populism with the election of Viktor Orban?",
        "What is the primary focus of the Arctic Council?",
        "Which country was the first to officially adopt Bitcoin as legal tender?",
        "What year did the civil war in Yemen begin?",
        "What is the official date of the United Kingdom's departure from the European Union (Brexit)?",
        "What event triggered the major protests in Hong Kong in 2019?",
        "Which Pacific Island nation is most at risk due to rising sea levels?",
        "What was the primary product at the center of the U.S.-China trade war?",
        "Which organization declared COVID-19 a global pandemic?",
        "What is the largest source of renewable energy in Sub-Saharan Africa?",
        "Which social media platform was most scrutinized for spreading misinformation during the 2016 U.S. presidential election?",
        "Which Hungarian leader is often cited as an example of rising authoritarianism in Europe?",
        "What is the main destination country for Syrian refugees since the beginning of the civil war?",
        "Which region of Antarctica is losing ice at the fastest rate?",
        "What was the central focus of the technological race between the U.S. and China?"
    ]
    options = [
        ["Brazil", "Peru", "Colombia", "Venezuela"],  # Options for Q1
        ["Promote global trade", "Enhance China's influence", "Reduce poverty", "Develop military alliances"],
        # Options for Q2
        ["Sulfur dioxide", "Carbon monoxide", "Particulate matter (PM2.5)", "Ozone"],  # Options for Q3
        ["2015", "2016", "2017", "2018"],  # Options for Q4
        ["10", "15", "17", "20"],  # Options for Q5
        ["Poland", "Hungary", "Greece", "Italy"],  # Options for Q6
        ["Trade regulations", "Environmental protection", "Military cooperation", "Immigration policies"],
        # Options for Q7
        ["El Salvador", "Malta", "Singapore", "Switzerland"],  # Options for Q8
        ["2011", "2012", "2013", "2014"],  # Options for Q9
        ["January 31, 2019", "January 31, 2020", "January 31, 2021", "January 31, 2022"],  # Options for Q10
        ["New labor laws", "Extradition bill", "Education reforms", "Housing crisis"],  # Options for Q11
        ["Fiji", "Tuvalu", "Solomon Islands", "Kiribati"],  # Options for Q12
        ["Steel", "Soybeans", "Technology products", "Automobiles"],  # Options for Q13
        ["World Health Organization", "Centers for Disease Control and Prevention", "United Nations",
         "International Red Cross"],  # Options for Q14
        ["Solar power", "Wind power", "Hydropower", "Geothermal energy"],  # Options for Q15
        ["Facebook", "Twitter", "Instagram", "YouTube"],  # Options for Q16
        ["Andrzej Duda", "Recep Tayyip Erdoğan", "Viktor Orbán", "Alexander Lukashenko"],  # Options for Q17
        ["Lebanon", "Jordan", "Turkey", "Greece"],  # Options for Q18
        ["East Antarctica", "West Antarctica", "South Pole", "Antarctic Peninsula"],  # Options for Q19
        ["Artificial intelligence", "Renewable energy", "Space exploration", "Biotechnology"]  # Options for Q20
    ]
    correct_option = [
        "a",  # Correct option for Q1
        "b",  # Correct option for Q2
        "c",  # Correct option for Q3
        "d",  # Correct option for Q4
        "c",  # Correct option for Q5
        "b",  # Correct option for Q6
        "b",  # Correct option for Q7
        "a",  # Correct option for Q8
        "d",  # Correct option for Q9
        "b",  # Correct option for Q10
        "b",  # Correct option for Q11
        "b",  # Correct option for Q12
        "b",  # Correct option for Q13
        "a",  # Correct option for Q14
        "c",  # Correct option for Q15
        "a",  # Correct option for Q16
        "c",  # Correct option for Q17
        "c",  # Correct option for Q18
        "b",  # Correct option for Q19
        "b"  # Correct option for Q20
    ]
    _correct_option = PRINT_Q_OP(rand_list, questions, options, correct_option)
    return _correct_option


# ===============================
# this function inputs the answer and validates it and returns the user input
def INPUT_ANSWER():
    _user_input = input("Enter your answer (a/b/c/d): ")
    _user_input = _user_input.lower()
    while (_user_input != 'a' and _user_input != 'b'
           and _user_input != 'c' and _user_input != 'd'):
        print("Invalid Input !")
        _user_input = input("Enter your answer (a/b/c/d): ")
    return _user_input


# game over in case of more than 2 wrong answers in a single level
def GAME_OVER(_level):
    print("You have LOST the game! Better luck next time!")


# this function returns the Prize of the level according to value of _level variable i-e (1,2,3)
def LEVEL_PRIZE(_level):
    if (_level == 1):
        _prize = "10 lakh"
    if (_level == 2):
        _prize = "1 crore"
    if (_level == 3):
        _prize = "10 crore"
    return _prize


#  this function returns the name of the level according to value of _level variable i-e (1,2,3)
def LEVEL_NAME(_level):
    _level_name = " "
    if (_level == 1):
        _level_name = "PATH TO RICHES"
    if (_level == 2):
        _level_name = "MILLIONER'S LADDER"
    if (_level == 3):
        _level_name = "Ultimate Fortune"

    return _level_name


# when user chooses to the leave the game after completion of a certain level this function is called
def LEVEL_COMPLETE_THEN_LEAVE(_level, _level_name, _prize):
    print(f"Congratulations! You have completed the level {_level_name} and won {_prize} Rupees!")
    print("Thank you for playing!")
    quit()


def WON_ALL_LEVEL(_level):
    os.system('cls')
    _prize = LEVEL_PRIZE(_level)
    print(
        "Congratulations on conquering all three levels of KBC! Your intellect, perseverance, and knowledge have propelled you to victory. You've demonstrated remarkable skill and determination, emerging as the ultimate champion of this thrilling game. Well done! ")
    print(f"You have won {_prize} pkr. Congratulations once again.")
    quit()


def ASK_NEXT_LEVEL(_level, _level_name, _prize):
    print("Would you like to play next level or to leave the game")
    print(f"In case you leave, you will win {_prize} PKR")
    while True:
        if _level <= 2:
            print("-> To play next level {press 1}")
            print("-> To leave the game {press 2}")
            try:
                _temp_inp = int(input("Select one: "))
                if _temp_inp == 1:
                    return _level + 1
                elif _temp_inp == 2:
                    LEVEL_COMPLETE_THEN_LEAVE(_level, _level_name, _prize)
                else:
                    print("Invalid input! Please enter 1 or 2.")
            except ValueError:
                print("Invalid input! Please enter a numeric value.")


# ===============================
# a level is completed and this function performs all the duties that are required ater completion
def LEVEL_COMPLETE(_level):
    # following line fetches the name of the level from the function LEVEL_NAME and stores it in the vzriable _level_name
    _level_name = LEVEL_NAME(_level)
    #  following line fetches the prize of the level from the function LEVEL_PRIZE and stores it in the vzriable _prize
    _prize = LEVEL_PRIZE(_level)
    print(f"Congratulations! You have completed LEVEL {_level} ({_level_name}) of KBC!")
    if _level <= 2:
        _level = ASK_NEXT_LEVEL(_level, _level_name, _prize)
        return _level
    else:
        WON_ALL_LEVEL(_level)


#  this function
def LEVEL(_game_over, _level):
    # this for loop shows 10 questions to the user from the current level
    for i in range(10):
        # this if statement confirms that the number of wrong answers entered by the user are not more than 2
        if (_game_over <= 2):
            # the following three if statements calls the specific level function out of 3 levels
            if _level == 1:
                _correct_option = RICHES_QUESTION_BANK()
            if _level == 2:
                _correct_option = MILLIONER_QUESTION_BANK()
            if _level == 3:
                _correct_option = ULTIMATE_QUESTION_BANK()
            # INPUT_ANSWER() is called that inputs the number from the user and it is stored in _user_input variable
            _user_input = INPUT_ANSWER()
            # CHECK_ANSWER() is called and true/false is stored in the variable _check
            _check = CHECK_ANSWER(_user_input, _correct_option)
            # this if statement informs the user that the answer entered is correct
            if _check:
                print("\n--> RIGHT! ")
            # in case the answer is incorrect else informs the user and increase the value of _game_over variable (wrong answers) by 1
            else:
                print("Oops! Incorrect. The correct answer is: ", _correct_option)
                _game_over = _game_over + 1
        # if the most outer if (that confirms that the number of wrong answers entered by the user are not more than 2) turned out to be false then GAME_OVER() is called
        else:
            GAME_OVER(_level)
            quit()
    #  the control will only come after all the ten questions are shown and the user has answered them correctly (minimum 8) i-e one level has been passed by the user. and its time to pass on to the next level
    # level_complete function will be called
    _level = LEVEL_COMPLETE(_level)
    print(_level)
    _level_name = LEVEL_NAME(_level)
    print(f"Welcome to LEVEL {_level} ({_level_name}) of KBC!")
    LEVEL(_game_over=0, _level=_level)


# if the user selects 1 then game will start and the whole execution of starting the game will start from here
def START_GAME(_current_balance=0, _level=1):
    # the _game_over variable counts the number of wrong answers entered by the user
    _game_over = 0
    os.system('cls')
    LEVEL(_game_over=0, _level=1)


#  perform the operations on the basis of user input 1. start game 2. instructions 3. end game
def MENU_CHOICE(_choice):
    if _choice == 1:
        START_GAME()
    elif _choice == 2:
        INSTRUCTIONS()
    elif _choice == 3:
        # exits the game completely
        os.system('cls')
        print("Successfully exited")
        quit()


# displays the main menu to the user
def MAIN_MENU():
    print("-> To start the game {press 1}")
    print("-> For Instructions {press 2}")
    print("-> To exit the game {press 3}")
    _user_choice = int(input("Select one: "))
    if (_user_choice == 1 or _user_choice == 2 or _user_choice == 3):
        MENU_CHOICE(_user_choice)
    else:
        os.system('cls')
        print("-----Inalid input! Try again-----")
        MAIN_MENU()


# displays instructions to the user
def INSTRUCTIONS():
    os.system('cls')
    print("-------Welcome to Kaun Banega Crorepati!-------")
    print(
        "-> This game has three levels.\nLEVEL 1: Path to riches\n LEVEL 2: Millionaire's Ladder \nLEVEL 3: Ultimate Fortune \n")
    print(
        "-> In each level you have to asnwer at least 8 questions out of 10")
    print("-> If you are not able to answer 8 questions correctly then you will lose the game")
    print("-> you can either quit the game or continue it after completing a level")
    print("-> once you have started a level, you cannot quit it ")

    input("Press 0 to go back to main menu")
    os.system('cls')
    MAIN_MENU()


# start of the program
print("Welcome to KBC")
MAIN_MENU()
