# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 13:25:21 2021

@author: Yauheny_Shaludzko
"""
import random as r  # Module random is imported to use randint
import string  # Module is imported to get lowercase letters

'''
Task: Create a list of random number of dicts (from 2 to 10)
dicts random numbers of keys should be letter,
dicts values should be a number (0-100),
example: [{'a': 5, 'b': 7, 'g': 11}, {'a': 3, 'c': 35, 'g': 42}]
'''
dict_list = []  # initialization of list
letters = string.ascii_lowercase  # method returns all lowercase letters
for i in range(r.randint(2, 10)):  # loop is used to fill list with random number of dictionaries
    '''
    Generator is used to create dictionary.
    r.choice(letters) is responsible for key generation, r.randint(0, 100) - for value generation.
    Number of key: value pairs inside dictionary is variable and determined by r.randint(2, 10)
    '''
    random_dict = {r.choice(letters): r.randint(0, 100) for i in range(r.randint(2, 10))}
    dict_list.append(random_dict)  # generated dictionary is added into dict_list
print("dict_list:", dict_list)  # print output result


def index_return(key1):  # creating func which returns index of dict, where defined key from parameter with max value
    kv_list = []  # create empty list
    vmax = 0  # variable for saving max value for current key
    for i in range(len(dict_list)):  # consider each dict separately
        # if key from parameter exists in this dictionary, this pair added into kv_list as dictionary
        if key1 in dict_list[i].keys():
            kv_list.append({key1: dict_list[i][key1]})
        # if this key doesn't exist in dict, pair {key:-1} will be add into kv_list
        # (-1 might not be in initial dict according to the task)
        else:
            kv_list.append({key1: -1})
    ''' for example if we had initial list as [{a:1,b:3},{a:5,c:9},{q:1,z:2}]
    f.e. for key1=a we will receive kv_list = [{a:1},{a:5},{a:-1}] ,
    it means that we leave only one pair in dictionary, and number of dict stay the same
    (if key was not in initial dict, we add key and value -1 for this case)
    it will helps to receive index of key:value (it equals to index of initial dict, which contain this kay:value'''

    for j in range(len(kv_list)):  # here we will find max value for current key
        if kv_list[j][key1] > vmax:
            vmax = kv_list[j][key1]
    # print(kv_list.index({'c': max}))
    # we receive index of dictionary, which contain pair {key1: max}, where key1-key from parameter, max-it's max value
    return kv_list.index({key1: vmax})+1

# here we count how much times some key appears in initial list of dict
# empty dict for saving pair key: number_of_times


num_of_keys = {}
for i in range(len(dict_list)):
    for key in dict_list[i].keys():
        # if key already exists in num_of_keys, we add 1 to it's value (as another one time, when it appears)
        if key in num_of_keys.keys():
            num_of_keys[key] = num_of_keys.get(key) + 1
        # if not, just add key with value = 1
        else:
            num_of_keys[key] = 1
# here we can print result - how much times key appeared
# print(num_of_keys)

# define new empty dictionary for combining all the dictionaries
result_dict = {}
# create cycle for each dictionary in previously defined list
for i in range(len(dict_list)):
    # create cycle which consider each pair of key and value in dictionaries from list
    for key, value in dict_list[i].items():
        # we compare current value with value of this key already existing in result_dict, if it's not exist
        # get(key, value) will return current value (second parameter), and max will be = value
        result_dict[key] = max(value, result_dict.get(key, value))
# we received final dict, but without changed names, below is a loop, which finds which keys appear more than once
# and change name of this key with the help of function, created above
# for each key in result dict (previously changed to list of keys)...
for key in list(result_dict):
    # print(key)
    # print(num_of_keys.get(key))
    # if this key appears more than once...
    if num_of_keys.get(key) > 1:
        # we change it's name according to the pattern key_index_of_dict
        result_dict[key+"_"+str(index_return(key))] = result_dict.pop(key)
# print result dictionary to console
print("Common dict with max values of repeated keys and number of dict in name:\n", result_dict)
