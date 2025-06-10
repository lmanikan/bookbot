def get_num_words(text:str) -> int:
    list_words = text.split()
    num_words = len(list_words)
    return num_words

def count_characters(text:str) -> dict[str:int]:

    list_words = text.split()
    char_count_dict = {}

    for word in list_words:
        for char in word.lower():
            if char in char_count_dict.keys():
                char_count_dict[char] += 1
            else:
                char_count_dict.update({char:1})
    
    return char_count_dict

def sort_on(in_dict: dict):
    return in_dict["num"]


def make_formatted_list(in_dict: dict):

    formatted_list = []
    for key,value in in_dict.items():
        formatted_list.append({'char':key,'num':value})
    formatted_list.sort(reverse=True, key=sort_on)

    return formatted_list



