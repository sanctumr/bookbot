def count_characters(file_contents):
    characters = {}

    for char in file_contents:
        char = char.lower()

        characters[char] = characters.get(char, 0) + 1

    return characters

def count_words(file_contents):
    list_of_words = file_contents.split()
    return len(list_of_words)

def __main__():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        # print(file_contents)

    # print(count_words(file_contents))

    print(count_characters(file_contents))

__main__()