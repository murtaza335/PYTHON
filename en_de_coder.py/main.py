import random
char_start_end = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
encode1_txt= []

def encode1():
    user_text = input("Enter text to encode: ")
    user_text_reverse = ""
    #this loop reverses the input string
    for i in range(len(user_text)):
        single = user_text[-i-1]
        user_text_reverse +=single
    words = user_text_reverse.split(" ")# to divide the sentence into a list of words on each space
    print("encode string: ")
    for i in range(len(words)):
        x = words[i]
        for j in range(len(x)):
            new = ord(x[j])
            new += 3
            char = chr(new)
            final = random.choice(char_start_end) +char+ random.choice(char_start_end)
            print(final,end="")
        print("#",end="")


def decode1():
    user_text = input("Enter text to decode: ")
    list_en_letters_unfiltered = []
    final_list_reversed=[]
    # splitting the list on # symbol
    list_encrypted_words = user_text.split("#")
    # looping thorugh the list of encrypted words
    for i in range(len(list_encrypted_words)):
        single_encrypted_word = list_encrypted_words[i]
        # looping throught the single encrypted word
        for i in range(0,len(single_encrypted_word),3):
            # saving each encrypted letter surrounded by special characters in list of encrypted letters
            list_en_letters_unfiltered.append(single_encrypted_word[i:i+3])
        
    # now loop through the list of encrypted letters and remove unwanted special characters from it.
    for i in range(len(list_en_letters_unfiltered)):
        # saving each encrypted unfiltered(surrounded by special charcaters)letter in en_letter_unfiltered variable.
        en_letter_unfiltered = list_en_letters_unfiltered[i]
        # removing first and last unwanted special character from en_letter_unfiltered and saving it in the variable en_letter_filtered
        en_letter_filtered = en_letter_unfiltered[1:-1]
        # now we are left with only one character in the variable en_letter_filtered
        # so we take it back three steps as in encode()
        # changing it to decimal code and then changing back to original one
        temp = ord(en_letter_filtered)
        temp -= 3
        de_char = chr(temp)
        final_list_reversed.append(de_char)
    # printing the list in reverse order
    for i in range(len(final_list_reversed)):
        print(final_list_reversed[-i-1],end=" ")


print("1. Encoding\n2, Decoding")              
choice = int(input("Select operation: "))
if choice== 1:
    encode1()
elif choice == 2:
    decode1()
else:
    print("Invalid choice")

'''
encoding method used in this program:
1. the input string will be reversed
2. make a list of the words present in the given sentence
3. assign a word to the variable:x
4. then we loop through variable:x that contains a single word from the sentence
5. each character of that word stored in variable:x is jumped by 3 characters
6. then a special character from the list: code-start_end[] is inserted in beginning and end of each character
'''
