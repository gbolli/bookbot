from stats import num_words, num_letters_dict

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        report(file_contents)

def report(file_string):
    just_letters_dict = num_letters_dict(file_string)
    for key in list(just_letters_dict.keys()):
        if key not in "abcdefghijklmnopqrstuvwxyz":
            del just_letters_dict[key]
    
    sorted_letters_dict = dict(sorted(just_letters_dict.items(), key=lambda item: item[1], reverse=True))

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words(file_string)} words found in the document\n")
    for key in sorted_letters_dict:
        print(f"The '{key}' character was found {sorted_letters_dict[key]} times")


main()