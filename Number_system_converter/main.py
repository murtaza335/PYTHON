def input_number(choice_from):
    if choice_from ==2:
        base_name = "binary"
    elif choice_from ==8:
        base_name = "octal"
    elif choice_from ==10:
        base_name = "decimal"
    elif choice_from ==16:
        base_name = "hexadecimal" 

    if choice_from == 2 or choice_from==8 or choice_from==10:
        print(f"Enter a {base_name} number: ")
        input_u = int(input())
    elif choice_from == 16:
        print(f"Enter a {base_name} number: ")
        input_u = input()
    return input_u
def hexa_10_11_12(remainder):
    if remainder == 10:
        remainder = "A"
    elif remainder == 11:
        remainder = "B"
    elif remainder == 12:
        remainder = "C"
    elif remainder == 13:
        remainder = "D"
    elif remainder == 14:
        remainder = "E"
    elif remainder == 15:
        remainder = "F"
    return remainder    
def hexa_ABC(a):
    if a == 'A':
        temp = 10
    elif a=='B':
        temp =11
    elif a=='C':
        temp =12
    elif a=='D':
        temp =13
    elif a=='E':
        temp =14
    elif a=='F':
        temp =15
    return temp

# conversion to all bases from decimal
def from_decimal(choice_from,choice_to,ans):
    if choice_from == 10:
        input_u = input_number(choice_from)
    else:
        input_u = ans
    list_ans = []
    divident = input_u
    while divident != 0 :
        x = divmod(divident, choice_to) # type: ignore
        divident = x[0]
        remainder = x[1]
        if choice_to == 16:
            remainder = hexa_10_11_12(remainder)
        list_ans.append(remainder)
    for i in range(len(list_ans)):
        print(list_ans[-i-1],end = "")


def to_decimal(choice_from,choice_to):
    input_u = input_number(choice_from)
    input_u = str(input_u)
    input_u = input_u.upper()
    list_split = []
    ans = 0
    for i in range(len(input_u)):
        if choice_from == 16 and ( input_u[i] == 'A' or input_u[i] == 'B' or input_u[i] == 'C' or input_u[i] == 'D' or input_u[i] == 'E' or input_u[i] == 'F'):
            temp = hexa_ABC(input_u[i])
        else:
            temp = int(input_u[i])
        list_split.append(temp)
    for i in range(len(list_split)):
        ans = ans + list_split[-i-1]*(choice_from**i)
    return ans

def start():
    print("binary -> base:2")
    print("decimal -> base:10")
    print("octal -> base:8")
    print("hexadecimal -> base:16")
    ans = 0
    choice_from = int(input("select the base of the input number to convert from(2/8/10/16): "))
    choice_to = int(input("select the base of the number to convert to(2/8/10/16): ")) 
    if choice_from == 10 :
        from_decimal(choice_from,choice_to,ans)
    elif choice_to == 10:
        ans = to_decimal(choice_from,choice_to)
        print(ans)
    elif (choice_from == 2 or choice_from == 8 or choice_from == 16) and (choice_to == 2 or choice_to == 8 or choice_to == 16):
        ans = to_decimal(choice_from,choice_to)
        from_decimal(choice_from,choice_to,ans)

#  program starts from here
start()


