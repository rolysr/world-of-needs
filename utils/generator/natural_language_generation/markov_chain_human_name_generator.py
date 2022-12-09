import operator
import random

# implementation idea taken from https://medium.com/@PuchkovOleg/name-generator-tutorial-1c9a3dfb2ab0

def generate_human_names(number_of_names, min_length, max_length):
    """
        A method based on markov chains for generating human names
        given a number of names, max and min length. This method returns
        a list of names
    """

    gender = 'M' if random.uniform(0, 1) < 0.5 else 'F'

    data = []
    if gender.upper() == 'M':
        f = open("utils/generator/natural_language_generation/name_dataset/namesBoys.txt", "r")
        data = f.read().lower().split('\n')
        other_f = open("utils/generator/natural_language_generation/name_dataset/namesGirls.txt", "r")
        other_data = other_f.read().lower().split('\n')
        f.close(); other_f.close()
    else: 
        f = open("utils/generator/natural_language_generation/name_dataset/namesGirls.txt", "r")
        data = f.read().lower().split('\n')
        other_f = open("utils/generator/natural_language_generation/name_dataset/namesBoys.txt", "r")
        other_data = other_f.read().lower().split('\n')
        f.close(); other_f.close()

    my_dict = getNamesDict(data)
    final_names = []
    while len(final_names) < number_of_names:
        name = generateName(my_dict)
        if len(name) >= min_length and len(name) <= max_length and name not in final_names and name.title() not in data and name.title() not in other_data:
            final_names.append(name.title())

    return final_names       

# building data for Markov model 
def getNamesDict(names):
    # ease the parsing of data
    list_of_names = []
    for name in names:
        if (name != ""):
            list_of_names.append("__" + name + "__")
    #
    dict_of_names = {}
    for name in list_of_names:                                      # take 'alex' as example
        for i in range(len(name)-3):
            combination = name[i:i+2]                               # combination of two letters such as 'al'
            if combination not in dict_of_names:                    # check if combo has been seen, 
                dict_of_names[combination] = []                     # if not create a new array as its value     
            dict_of_names[combination].append(name[i+2])            # append the letter that went after this combination to its array 
    
    return dict_of_names                                            # so now the dict_of_names looks like this {('al', ['e'])}

# generating new name
def generateName(dict_of_names):
    combination = "__"
    next_letter = ""
    result = ""
    while True: 
        number_of_letters = len(dict_of_names[combination])         # get length of the array of letters that follow a combiation
        index = random.randint(0,number_of_letters - 1)             # get random index out of letters that follow a combination
        next_letter = dict_of_names[combination][index]             # this random index will get us the next predicted letter. 
        if next_letter == "_":                                      # random can be used because if there are 5 As and 6 Bs then B 
            break                                                   # has a higher probability of being the chosen letter
        else:
            result = result + next_letter
            combination = combination[1] + next_letter
    
    return result