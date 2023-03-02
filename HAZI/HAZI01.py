def subset(input_list, start_index, end_index):
    temp_list = []
    for i in range(start_index, end_index):
        temp_list.append(input_list[i])
    return temp_list

def every_nth(input_list, step_size):
    temp_list = []
    for i in range(0, len(input_list), step_size): #, step_size
        temp_list.append(input_list[i])
    return temp_list    

def unique(input_list):
    flag = False
    for i in input_list:
        if (input_list.count(i) == 1):
            flag = True
            break

    return flag

def flatten(input_list):
    output_list = []
    for i in input_list:
        if  type(i) == list:
            output_list = output_list + flatten(i)
        else:
            output_list.append(i)
    
    return output_list

def merge_lists(*args):
    output_list = []
    for i in args:
        output_list += i
    
    return output_list

def reverse_tuples(input_list):
    output_list = []
    for i in input_list:
        output_list.append((i[1], i[0]))
    
    return output_list

def remove_tuplicates(input_list):
    output_list = []

    for i in input_list:
        if i not in output_list:
            output_list.append(i)

    return output_list

def transpose(input_list):
    output_list = []
    #elobb az oszlopokin iteralunk, belso cilkus a sor
    for i in range(len(input_list[0])):
        temp_list = []
        for j in range(len(input_list)):
            temp_list.append(input_list[j][i])
        output_list.append(temp_list)
    
    return output_list

print(transpose([[1,2,3], [4,5,6], [7,8,9], [10,11,12]]), sep="\n")

"""def split_into_chunks(input_list : list, chunk_size):
    output_list = []
    chunk_counter = 0
    temp_list = []

    for i in range(len(input_list)):
        j = 0
        while j < len(input_list[i]):
            if len(temp_list) < chunk_size:
                temp_list.append(input_list[i][j])
            j += 1
        output_list.append(temp_list)


    return output_list

split_into_chunks([[1,1],[1,2,2,2,3,3,3,4,4,4,5,5,5]], 3)"""

#TODO
            

#Create a function that can merge n dictionaries
#return type: dictionary
#function name must be: merge_dicts
#input parameters: *dict



#Create a function that receives a list of integers and sort them by parity
#and returns with a dictionary like this: {"even":[...],"odd":[...]}
#return type: dict
#function name must be: by_parity
#input parameters: input_list


def by_parity(input_list):
    output_dict = {}
    for i in input_list:
        if i % 2 == 0:
            output_dict[i] = "even"
        elif i % 2 == 1:
            output_dict[i] = "odd"

    return output_dict


#Create a function that receives a dictionary like this: {"some_key":[1,2,3,4],"another_key":[1,2,3,4],....}
#and return a dictionary like this : {"some_key":mean_of_values,"another_key":mean_of_values,....}
#in short calculates the mean of the values key wise
#return type: dict
#function name must be: mean_key_value
#input parameters: input_dict



#If all the functions are created convert this notebook into a .py file and push to your repo


