def main():
    path_to_file = "books/frankenstein.txt"
    with open(path_to_file) as f:
        file_contents = f.read()
    word_count_str = str(num_of_words(file_contents))
    char_count_dict = count_letters(file_contents)
    print(word_count_str)
    print(char_count_dict)
    
def num_of_words(text):
    words = len(text.split())
    return words

def count_letters(text):
    lowercase_text = text.lower().split()
    chars = "".join(lowercase_text)
    chars_dict = {}
    for char in chars:
        if char in chars_dict:
            chars_dict[char] += 1   
        else:
            chars_dict[char] = 1   
    return chars_dict

if __name__ == '__main__':
    main()