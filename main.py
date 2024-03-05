def main():
    path_to_file = "books/frankenstein.txt"
    with open(path_to_file) as f:
        file_contents = f.read()
    word_count_str = str(num_of_words(file_contents))
    print(word_count_str)
    
def num_of_words(text):
    words = len(text.split())
    return words

if __name__ == '__main__':
    main()