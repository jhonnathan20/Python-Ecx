"""
Python's index method finds the index of the first item in a list, 
but what if there are multiple instances of that item? 

Your goal for this challenge is to write a Python function 
to find the indices for all items in a list that are equal to a given value. 

-It should accept two input parameters; the list to search and the value you're searching for. 

-The output should be a list of indices, each represented by a list of numbers. 

Keep in mind that Python lists can also contain other lists so your function should be 
able to traverse multidimensional lists to find all indices of the given value. 

For example, if I wanted to find all of the twos in this list:

>>example = [[[1,2,3], 2, [1,3]], [1,2,3]]

which contains several sub-lists, passing it to my index all function should find this first one, 

which is nested three lists deep and can be indexed at zero, zero, one. 

This next two, which is only two lists deep and can be indexed at zero one, 

and the third and final two, which is also two lists deep at index one, one. 

The resulting output is a list of lists, containing those indices.

>>index_all(example, 2)
[[0,0,1], [0,1], [1,1]]

VER IMAGEN DE EXPLICAION

"""
lista = [[[1,2,3], 2, [1,3]], [1,2,3], 2, 4]
print("La lista es: ", lista)
search = 2
indices = list()
for n in range(len(lista)):
    if lista[n] == search:
        print("Hay un 2 l1")
        indices.append([n])
    elif isinstance(lista[n], list):
        print("lev2")
        for elemento in range(len(lista[n])):
            if isinstance(lista[n][elemento], list):
                print("lev3")
                if elemento == search:
                    print("Hay un 2")
            
            
        
print(indices)
"""
search_list = [[[1,2,3], 2, [1,3]], [1,2,3]]
item = 2
indices = list()
for i in range(len(search_list)):
    if search_list[i] == item:
        indices.append([i])
    elif isinstance(search_list[i], list): #isintance(obj, type)->returns True if the object is of the type.
        for index in index_all(search_list[i], item):
            indices.append([i]+index)
print(indices)
"""            
        
