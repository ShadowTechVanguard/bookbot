def read_book(txt):
    with open(txt) as f:
        file_contents = f.read()
    return file_contents

def sort_on(dict):
    return dict["Num"]

def get_num_words(read): 
    words = read.split()
    return len(words)
    
def char_frequency(read):
    character_dic = {} 
    for char in read.lower():
        if char.isalpha():
            if char in character_dic:
                character_dic[char] += 1
            else:
                character_dic[char] = 1
    return character_dic

def sorted_char_list(char):
    sorted_char = []
    for ch in char:
        sorted_char.append({"Char": ch, "Num":char[ch]})
    sorted_char.sort(reverse=True, key=sort_on)
    return sorted_char