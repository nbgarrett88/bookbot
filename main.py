with open("books/frankenstein.txt") as f:
    file_contents =f.read()

def word_count(file):
    return len(file.split())

#print(word_count(file_contents))

def char_count(file):
    chars = {}

    for word in file.split():
        for char in word.lower():
            if char not in chars:
                chars[char] = 1
            else:
                chars[char] += 1
    return chars

#print(char_count(file_contents))

def create_report(file):

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count(file_contents)} words found in the document\n")

    for char, count in sorted(char_count(file_contents).items()):
        if char.isalpha():
            print(f"The '{char}' character was found {count} times")
    
    print("--- End report ---")

create_report(file_contents)