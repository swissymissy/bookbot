def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    lower_text = text.lower()
    num_each_char = {}
    for i in lower_text:
        #checking if the character is in dictionary yet. if not, initilize it with 0 then increment it
        if i not in num_each_char: 
            num_each_char[i] = 0
        num_each_char[i] += 1
    return num_each_char  

def sort_on(dict):
    return dict["num"]

def print_report (report):
    list_of_dict = []
    
    for char,count in report.items():
        if char.isalpha():
            list_of_dict.append({"char": char, "num":count})
    
    list_of_dict.sort(reverse=True, key=sort_on)
    print("------------- Begin report -------------")

    for item in list_of_dict:
        print(f"The '{item['char']}' character was found {item['num']} times ")
    
    print("------------- End of report -------------")

def main():
    book_path = "books/frankenstein.txt"
    file_contents = get_book_text(book_path)

    #print(file_contents)
    
    num_words = count_words(file_contents)
    #print(num_words)

    num_character = count_characters(file_contents)
    #print(f"The number of each characters: {num_character}")

    print_report(num_character)



if __name__ == "__main__":
    main()
