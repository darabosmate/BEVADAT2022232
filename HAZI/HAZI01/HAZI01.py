def subset(input_list, start_index, end_index):

    return input_list[start_index:end_index]

def every_nth(input_list, step_size):
    temp_list = []
    for i in range(0, len(input_list), step_size): #, step_size
        temp_list.append(input_list[i])
    return temp_list    

def unique(input_list:list) -> bool:
    temp_list = sum(input_list)
    i = 0
    while i < len(input_list) and input_list.count(input_list[i]) == 1:
        i += 1
    

    return len(input_list) == i

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

def remove_duplicates(input_list):
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

def split_into_chunks(input_list : list, chunk_size):
    output_list = []

    for i in range(0, len(input_list), chunk_size):
        temp_list = [x for x in input_list[i:i+chunk_size]]
        output_list.append(temp_list)

    return output_list

def merge_dicts(*input_dict : dict):
    output_dict = {}
    for i in input_dict:
        output_dict.update(i)
    
    return output_dict

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

def mean_key_value(input_dict : dict):
    output_dict = {}
    for key, value in input_dict.items():
        output_dict[key] = sum(value) / len(value)

    return output_dict