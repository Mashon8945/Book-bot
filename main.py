
def main():
    with open("books/frankeinstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()
        string_count = len(words)
        print(string_count)

def characters(text):
    char_count = {}
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

with open("books/frankeinstein.txt") as f:
    file_contents = f.read()
    file_contents = file_contents.lower()
    result = characters(file_contents)
    word_count = len(file_contents.split())

    print(f"--- Begin report of books/frankenstein.txt ---{word_count} words found in the document\n\n")
    for char, count in result.items():
        if char.isalpha():
            print(f"The character '{char}' was found {count} times")

main()