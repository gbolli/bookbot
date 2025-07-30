def num_words(file_string):
    return len(file_string.split())

def num_letters_dict(file_string):
    letter_dict = {}
    for c in file_string:
        new_c = c.lower()
        if new_c in letter_dict:
            letter_dict[new_c] += 1
        else:
            letter_dict[new_c] = 1
    return letter_dict