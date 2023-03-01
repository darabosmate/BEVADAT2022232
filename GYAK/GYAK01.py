def contains_odd(input_list):
    c = False
    for i in input_list:
        if (i % 2 != 0):
            c = True
    return c

def is_odd(input_list):
    output_list = []
    for i in input_list:
        if (i % 2 == 0):
            output_list.append(False)
        else:
            output_list.append(True)
    return output_list

def element_wise_sum(input_list_1, input_list_2):
    output_list = []
    for i in range(0, len(input_list_1)):
        output_list.append(input_list_1[i] + input_list_2[i])
    return output_list

def dict_to_list(input_dict):
    output_list = []
    for i in input_dict:
        output_list.append((i, input_dict[i]))
    return output_list