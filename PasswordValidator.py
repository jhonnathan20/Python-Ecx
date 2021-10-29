#Script to ask for a password and validate if it meet the requirements.
#Password characteristics: At least one Cap Letter, at least one symbol different from letters, at least 10 digits, no blancs spaces.

pwd = input("Please enter your password, \n Password characteristics: At least one Cap Letter, at least one number, at least 8 digits, no blancs spaces: \n")
def password_validator(pwd):
    print("\n-Validating pasword characteristics...")
    cap = False
    number = False
    digits = False
    noblancs = False
    valid = False

    if len(pwd)>8:
            digits =  True
            print("\n-Number of digits valid.")
    else:
        print("\n ***Passowrd not valid.***")
        return False

    for i in pwd:
        if i.isupper() ==  True:
            cap = True
            #print("\n-Cap Letter valid.")
            #print(cap)
        elif i.isdigit() == True:
            number = True
            #print("\n-Digit valid.")
            #print(number)
        elif i.isspace() ==  False:
            noblancs =  True
            #print("\n-No blanks valid.")
            #print(noblancs)
        
        if (cap == True and number == True and digits == True and noblancs == True):
            valid = True
            break

    #print("\n valores de variables: ",digits,cap,number,noblancs,valid)

    if (cap == True and number == True and digits == True and noblancs == True):
        print("\n-Valid Password. \n")
        validation = input("- Write your passowrd one more time: ")
        if(validation == pwd):
            print("\n --- Correct passowrd. ---\n")
        else:
            print("\n ***Incorrect password.***\n")
    
    else:
        print("\n ***Passowrd not valid.***")
    
password_validator(pwd)

