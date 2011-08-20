romanize = [
    ["anohito","a-no-hi-to","hiragana"],
    ["konnichiwa","ko-tsuS-ni-chi-wa","hiragana"],    
    ["arigatou","a-ri-ga-to-u","hiragana"],
    ["sensei","se-n-se-i","hiragana"],
    ["hajimemashite","ha-ji-me-ma-shi-te","hiragana"],
    ["oyasumi","o-ya-su-mi","hiragana"],
    ["itaria","i-ta-ri-a","katakana"],
    ["amerika","a-me-ri-ka","katakana"],
    ["furansu","fu-ra-n-su","katakana"],
    ["doitsu","do-i-tsu","katakana"],
    ["kanada","ka-na-da","katakana"]
    ]
    
def removeMinusSign(string):
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

def sizeOfTheWord(string):
    """
    """
    word = removeMinusSign(string)
    return len(word)
        
# print removeMinusSign("ko-tsuS-ni-chi-wa")
# print sizeOfTheWord("ko-tsuS-ni-chi-wa")
