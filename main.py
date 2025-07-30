import sys
from stats import num_words, num_letters_dict

def main():
    if len(sys.argv) == 2:
        file_path = sys.argv[1]
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    with open(file_path) as f:
        file_contents = f.read()
        report(file_contents, file_path)

def report(file_string, file_path):
    just_letters_dict = num_letters_dict(file_string)
    for key in list(just_letters_dict.keys()):
        if key not in "abcdefghijklmnopqrstuvwxyz":
            del just_letters_dict[key]
    
    sorted_letters_dict = dict(sorted(just_letters_dict.items(), key=lambda item: item[1], reverse=True))

    print("============ BOOKBOT ============\n")
    print(f"Analyzing book found at {file_path}\n")
    print("----------- Word Count ----------\n")
    print(f"Found {num_words(file_string)} total words\n")
    print("--------- Character Count -------\n")
    for key in sorted_letters_dict:
        #print(f"The '{key}' character was found {sorted_letters_dict[key]} times")
        print(f"{key}: {sorted_letters_dict[key]}")

main()