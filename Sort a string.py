#Your goal is to write a Python function to sort the words in a string. 
#It should accept a string containing one or more words separated by spaces as the input argument, 
#and then return a string containing those words sorted alphabetically. 

#A call to the function might look like this:
#sort_words('string of words') -> 'of string words'

#taking in a string of words and then returning the string of string words.

#You should ignore the case of the words when sorting them. 
#However, the output should have the same upper and lowercase letters as the corresponding input words.

#For example, the input string banana ORANGE apple should produce the output shown here with: apple banana ORANGE.

phrase = input(str("Indique la frase que desea ordenar de forma alafabetica: "))
print("\n Su frase es: ", phrase)
words = phrase.split() #separar la frase en palabras
words = [w.lower() + w for w in words]#agrega copia de palabras en minuscula al lado de palabra
words.sort() #ordena las palabras de forma alfabetica.
words = [w[len(w)//2:] for w in words] #elimina palabra repetida
" ".join(words) #une de nuevo las palabras
print("\n Su frase ordenada es: ", words)

#Para ignorar el caso de las palabras en mayuscula:
#append la palabra en minuscula al lado de la palabra que tenga mayuscula:
#bananabanana, orangeORANGE, appleaplle

#Luego se ordena el array y se elmina las palabras repetidas.

