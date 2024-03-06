def main():
    path_to_file = "books/frankenstein.txt"
    with open(path_to_file) as f:
        file_contents = f.read()
    word_count_str = str(num_of_words(file_contents))
    char_count_dict = count_letters(file_contents)
    char_count_dict_list = convert_dict(char_count_dict)
    char_count_dict_list.sort(reverse=True, key=sort_on)
    print(generate_report(word_count_str, char_count_dict_list))
    # print(char_count_dict_list)
    # dict_list = convert_dict(char_count_dict)
    # print(word_count_str)
    # print(char_count_dict)
    # print(convert_dict(char_count_dict))
    
def num_of_words(text):
    words = len(text.split())
    return words

def count_letters(text):
    lowercase_text = text.lower().split()
    chars = "".join(lowercase_text)
    chars_dict = {}
    for char in chars:
        if char.isalpha():
            if char in chars_dict:
                chars_dict[char] += 1   
            else:   
                chars_dict[char] = 1 
    return chars_dict

def convert_dict(my_dict):
    my_list = []
    for character, num in my_dict.items():
        my_list.append({'character': character, 'num': num})
    return my_list

def sort_on(dict):
    return dict['num']

def generate_report(str, list):
    report = f""
    report = f"--- Begin report of books/frankenstein.txt ---\n{str} words found in the document\n\n"
    for i in list:
        report += f"The {i['character']} character was found {i['num']} times \n"

    report += f"--- End report ---"
    return report

if __name__ == '__main__':
    main()