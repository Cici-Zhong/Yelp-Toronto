import json
from os.path import join

def getFileContentToList(path):
    lines = [line.rstrip('\n') for line in open(path)]
    line_list = []
    for line in lines:
        line_dict = json.loads(line)
        line_list.append(line_dict)
    return line_list

def getFileContentToListAndFilter(path, key, operator, value):
    lines = [line.rstrip('\n') for line in open(path)]
    line_list = []
    for line in lines:
        line_dict = json.loads(line)
        if filter_set(line_dict, key, operator, value):
            line_list.append(line_dict)
    return line_list

def filter(original_list, key, operator, value):
    filtered_list = []
    for list_dict in original_list:
        if filter_set(list_dict, key, operator, value):
            filtered_list.append(list_dict)                
    return filtered_list

def filter_set(original_set, key, operator, value):
    valid = False
    if operator in ('equal', '=='):
        if original_set[key] == value:
            valid = True
    elif operator in ('greater', '>'):
        if original_set[key] > value:
            valid = True
    elif operator in ('less', '<'):
        if original_set[key] < value:
            valid = True
    elif operator in ('equal greater', '>='):
        if original_set[key] >= value:
            valid = True
    elif operator in ('equal less', '<='):
        if original_set[key] <= value:
            valid = True
    elif operator in ('in'):
        if original_set[key] in value:
            valid = True
    return valid