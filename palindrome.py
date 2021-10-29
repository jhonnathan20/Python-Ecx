""""
Your goal is to write a Python function that determines if a given string is  a palindrome.
A palindrome is a word or phrase that reads the same forwards as it does backwards.

Your function should accept a single input of the string to evaluate and return a Boolean value indicating whether
or not that string was a palindrome.

Your function should only consider letters, A through Z, when evaluating the  string and you should ignore
their case, treating uppercase and lowercase letters as being the same.

For example, if if you call it on the phrase "Go hang a salami, I'm a lasagna hog," it should return true
"""

#My solution: 
s = input("Ingrese la palabra o frase para saber si es un palindromo:")

def is_palindrome(s):
    s = s.replace(",","") #remove commas
    s = s.replace(".","") #remove dot symbol 
    s = s.replace(" ","") #replace blanks with no spaces.
    s = s.upper() #replace all the letters to have all of them in upper case.

    si = s[::-1]
    print("\n String invertido:",si)

    list(s) #make the string a list 
    list(si) #make the inverted string a list
    
    if(s==si):
        print("La frase ingresada SI es un palindromo: \n")
        print("Original: \n",s)
        print("Inversa: \n",si)
    else:
        print("La frase ingresada NO es palindromo:", s)
        print("Original: \n",s)
        print("Inversa: \n",si)
        
    #Long way:
    """
    j=len(s)-1 # variable to loop through the list in the opposite way
    i=0 # variable to loop the list
    
    #
    while(i<j):
        if (s[i]==s[j]):
            i = i+1
            j = j-1
            if(i==j)or (i>j):
                print("La frase ingresada SI es un palindromo: \n")
                print("Original: \n",s)
                print("Inversa: \n", si)
        else:
            print("La frase ingresada NO es palindromo:")
            print("Original: \n",s)
            print("Inversa: \n", si)
            break
    """
is_palindrome(s)

#Palindrome examples:
#A Mercedes, ese de crema.
#Adán no cede con Eva y Yavé no cede con nada.
#Amo la pacífica paloma.

