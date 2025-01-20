def count_characters(file_contents):
    characters = {}

    for char in file_contents:
        char = char.lower()
        if char.isalpha():
            characters[char] = characters.get(char, 0) + 1

    return characters

def count_words(file_contents):
    list_of_words = file_contents.split()
    return len(list_of_words)

def get_num(dict):
    return dict["num"]

def __main__():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        # print(file_contents)

    word_count = count_words(file_contents)
    characters = count_characters(file_contents)

    # Convert dictionary to list of dictionaries

    char_list = []
    for char,count in characters.items():
        char_list.append({"char": char, "num": count})

    # Sort the list by count (num) in descending order
    char_list.sort(reverse=True, key=get_num)
    
    # Let's print to see what we have
    # print(char_list)

    # Print the report
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document\n")

    for char_dict in char_list:
        print(f"The '{char_dict['char']}' character was found {char_dict['num']} times")

    print("--- End report ---")

__main__()