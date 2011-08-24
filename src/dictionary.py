"""
This module contains dictionary array
for both Vocabulary Practice and
Romanize Words section. 
"""

DICT_ARR = [
    ["anohito","a-no-hi-to","hiragana", "that person"],
    ["konnichiwa","ko-n-ni-chi-wa","hiragana", "hello"],    
    ["arigatou","a-ri-ga-to-u","hiragana", "thank you"],
    ["sensei","se-n-se-i","hiragana", "teacher/sir"],
    ["hajimemashite","ha-ji-me-ma-shi-te","hiragana", "i'm glad to meet you"],
    ["oyasuminasai","o-ya-su-mi-na-sa-i","hiragana","good night"],
    ["itaria","i-ta-ri-a","katakana", "italy"],
    ["amerika","a-me-ri-ka","katakana", "america"],
    ["furansu","fu-ra-n-su","katakana", "france"],
    ["doitsu","do-i-tsu","katakana", "germany"],
    ["kanada","ka-na-da","katakana", "canada"],
    ["sumimasen","su-mi-ma-se-n","hiragana", "excuse me"],
    ["raiburari","ra-i-bu-ra-ri","katakana", "library"],
    ["ohayou","o-ha-yo-u","hiragana", "good morning"],
    ["gomennasai","go-me-n-na-sa-i","hiragana", "I'm sorry"],
    ["isha","i-sha","hiragana", "doctor"]
    ]
    
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
        
# print get_picture_array("ko-tsuS-ni-chi-wa")
# print size_of_the_word("ko-tsuS-ni-chi-wa")
