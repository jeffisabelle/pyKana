"""
This module contains dictionary array
for both Vocabulary Practice and
Romanize Words section. 
"""

import cPickle

def save_array(dict_arr, file_name):
    """
    
    Arguments:
    - `dict_arr`: the array that is going to be saved
    - `file_name`: the file_name that holds the saved array
    """
    the_file = open(file_name,'w')
    cPickle.dump(dict_arr, the_file)
    the_file.close()

def load_array(file_name):
    """
    return a 2d-array from the given file

    Arguments:
    - `file_name`: the the_file that is going to be loaded
    """
    the_file = open(file_name, 'r')
    the_arr = cPickle.load(the_file)
    the_file.close()
    return the_arr

def remove_word(word, dict_arr, file_name):
    """
    Removes given word from the array

    Arguments:
    - `word`: word that is going to be removed.
    - `dict_arr`: dictionary array which contains the words
    - `file_name`: the array will instantly written on this
    file after the word removed from it.
    """

    removed_row = 0
    range_of_arr = len(dict_arr)

    for row in range(range_of_arr):
        if dict_arr[row][0] == word:
            removed_row = row

    if dict_arr[removed_row][0] == word:
        dict_arr.pop(removed_row)

    save_array(dict_arr, file_name)
    
def get_picture_array(string):
    """    
    returns given string as an array after removing minus signs 
    and adding '.png' to every syllable.

    Arguments:
    - `string`: the word that is going to be processed  
    """

    new_string = ""
    for letter in string:
        if letter == "-":
            new_string += ".png "
        else:
            new_string += letter

    new_string += ".png" #for the last syllable
    new_string = str(new_string)
    new_string = new_string.split() 

    return new_string

def size_of_the_word(string):
    """
    returns the size of the given string
    Arguments:
    - `string`: the word that is going to be processed  
    """
    word = get_picture_array(string)
    return len(word)

def has_this_word(word, dict_arr):
    """
    Checks if given word is already in dictionary
    """
    for row in dict_arr:
        if row[0] == word:
            return True

    return False
    

def add_new_word(new_row, dict_arr, file_name):
    """
    Adds a new word to the dictionary
    and saves it

    Arguments:
    - `new_row`: the new set of the word (word, syllable, meaning, char_set)
    - `dict_arr`: the array that is going to be appended with new row
    - `file_name`: the file that holds the dictionary array
    """
    dict_arr.append(new_row)
    save_array(dict_arr,file_name)

DICT_ARR = load_array("data.dat")
