def count_words(text):
    words = text.split()
    num_words = len(words)
    return num_words

def count_char(text):
    char_dict = {}
    lowercase_text = text.lower()
    for char in lowercase_text:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def sort_on(items):
    for key in items:
        return items[key]

def sort_count_char(char_dict):
    dict_list = []
    count_list = []
    for key in char_dict:
        dict = {}
        dict[key] = char_dict[key]
        count_list.append(char_dict[key])
        dict_list.append(dict) 
    dict_list.sort(reverse=True,key=sort_on)
    return dict_list

