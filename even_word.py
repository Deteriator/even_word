'''
P: Given a word return the num of letters to remove to get a even word

E:even_word('aaaa') == 0
  even_word('potato') == 2
  even_word('aabbbb') == 0
  even_word('aaabbbccc') == 3
  
D: string, int, dictionary

A:  Give a string.
    Declare dictionary to hold numbers
    Loop over string 
        For each letter add to dict 
            if there increase amount by 1
    If any index % 2 = 0 continue
        Else return 0
    
    
    
'''










def even_word(string):
    dict = {}
    amount = 0
    for letter in string:
        if letter in dict:
            dict[letter] += 1
        else:
            dict[letter] = 1
    for item in dict:
        if dict[item] % 2 != 0:
            amount += 1
    return amount