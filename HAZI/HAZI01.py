# %%
#Create a function that returns with a subsest of a list.
#The subset's starting and ending indexes should be set as input parameters (the list aswell).
#return type: list
#function name must be: subset
#input parameters: input_list,start_index,end_index

# %%
def subset(input_list, start_index, end_index):
    temp_list = []
    for i in range(start_index, end_index):
        temp_list.append(input_list[i])
    return temp_list     #input_list[start_index:end_index] 


#subset([1,2,3,4,5,6,7], 2, 5)

# %%
#Create a function that returns every nth element of a list.
#return type: list
#function name must be: every_nth
#input parameters: input_list,step_size

# %%
def every_nth(input_list, step_size):
    temp_list = []
    for i in range(0, len(input_list), step_size): #, step_size
        temp_list.append(input_list[i])
    return temp_list    

#every_nth([1,2,3,4,5,6,7], 6)

# %%
#Create a function that can decide whether a list contains unique values or not
#return type: bool
#function name must be: unique
#input parameters: input_list

# %%
def unique(input_list) -> bool:
    flag = False
    for i in input_list:
        if (input_list.count(i) == 1):
            flag = True
            break

    return flag

#unique([1,1,2,3,4,5])
#unique([1,1,1,1,1])

# %%
#Create a function that can flatten a nested list ([[..],[..],..])
#return type: list
#fucntion name must be: flatten
#input parameters: input_list

# %%
def flatten(input_list):
    output_list = []
    for i in input_list:
        if  type(i) == list:
            output_list = output_list + flatten(i)
        else:
            output_list.append(i)
    
    return output_list

#flatten([1, [2, [3, 4], 5], 6, [7, 8, 9]])
#flatten([1, [2, 3, 4, 5], 6, [7, 8, 9]])
#flatten([1, 2, 3, 4, 5, 6, 7, 8, 9])

# %%
#Create a function that concatenates n lists
#return type: list
#function name must be: merge_lists
#input parameters: *args


# %%
def merge_lists(*args):
    output_list = []
    for i in args:
        output_list += i
    
    return output_list

#merge_lists([1,2], [3,4], [5,6])

# %%
#Create a function that can reverse a list of tuples
#example [(1,2),...] => [(2,1),...]
#return type: list
#fucntion name must be: reverse_tuples
#input parameters: input_list

# %%
def reverse_tuples(input_list):
    output_list = []
    for i in input_list:
        output_list.append((i[1], i[0]))
    
    return output_list

#reverse_tuples([(1,2), (3,4), (5,6)])


# %%
#Create a function that removes duplicates from a list
#return type: list
#fucntion name must be: remove_tuplicates
#input parameters: input_list

# %%
def remove_tuplicates(input_list):
    output_list = []

    for i in input_list:
        if i not in output_list:
            output_list.append(i)

    return output_list

#remove_tuplicates([11,11,2,3,4,5,6,6,7,7,8])

# %%
#Create a function that transposes a nested list (matrix)
#return type: list
#function name must be: transpose
#input parameters: input_list

# %%
def transpose(input_list):
    output_list = []
    #elobb az oszlopokin iteralunk, belso cilkus a sor
    for i in range(len(input_list[0])):
        temp_list = []
        for j in range(len(input_list)):
            temp_list.append(input_list[j][i])
        output_list.append(temp_list)
    
    return output_list

#print(transpose([[1,2,3], [4,5,6], [7,8,9], [10,11,12]]), sep="\n")



# %%
#Create a function that can split a nested list into chunks
#chunk size is given by parameter
#return type: list
#function name must be: split_into_chunks
#input parameters: input_list,chunk_size

# %%

def split_into_chunks(input_list : list, chunk_size):
    output_list = []
    flat_list = sum(input_list, [])

    for i in range(0, len(flat_list), chunk_size):
        temp_list = [x for x in flat_list[i:i+chunk_size]]
        output_list.append(temp_list)

    return output_list
    



#split_into_chunks([[1,1],[1,2,2,2,3,3,3,4,4,4,5,5,5,6], [6,6,7,7]], 3)
            

# %%
#Create a function that can merge n dictionaries
#return type: dictionary
#function name must be: merge_dicts
#input parameters: *dict

# %%
def merge_dicts(*input_dict : dict):
    output_dict = {}
    for i in input_dict:
        output_dict.update(i)
    
    return output_dict

#merge_dicts({1:"a"}, {2:"b"}, {3:"c"}, {4:"d", 5:"e"})

# %%
#Create a function that receives a list of integers and sort them by parity
#and returns with a dictionary like this: {"even":[...],"odd":[...]}
#return type: dict
#function name must be: by_parity
#input parameters: input_list

# %%
def by_parity(input_list):
    output_dict = {}
    even = []
    odd = []
    for i in input_list:
        if i % 2 == 0:
            even.append(i)
        elif i % 2 == 1:
            odd.append(i)
    output_dict["even"] = even
    output_dict["odd"] = odd
    return output_dict

#by_parity([1,1,3,4,5,6,7,8,9])

# %%
#Create a function that receives a dictionary like this: {"some_key":[1,2,3,4],"another_key":[1,2,3,4],....}
#and return a dictionary like this : {"some_key":mean_of_values,"another_key":mean_of_values,....}
#in short calculates the mean of the values key wise
#return type: dict
#function name must be: mean_key_value
#input parameters: input_dict

# %%
def mean_key_value(input_dict : dict):
    output_dict = {}
    for key, value in input_dict.items():
        output_dict[key] = sum(value) / len(value)

    return output_dict

#mean_key_value({"a":[1,2,3], "b":[4,5,6], "c":[7,8,9]})

# %%
#If all the functions are created convert this notebook into a .py file and push to your repo


