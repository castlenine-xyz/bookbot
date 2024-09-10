def main():
    book_path = "books/frankenstein.txt"
    # text = get_book_text(book_path)
    # num_words = get_num_words(text)
    # letter_counts = get_char_counts(text)
    # print(f"{num_words} words found in the document")
    # print(f"{letter_counts} letters in doc")
    print_report(book_path)


def print_report(book_path):
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    letter_counts = get_char_counts(text)
    filtered_letter_counts=filterLetterCounts(letter_counts)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document\n")
    for entry in filtered_letter_counts:
         char=entry["letter"]
         num=entry["num"]
         print(f"The {char} character was found {num} times")
    print("--- End report ---")



def filterLetterCounts(letter_counts):
    # take dict give back list of dics
    filtered=[]
    for key in letter_counts:
        if key.isalpha():
            filtered.append({"letter":key, "num":letter_counts[key]})
    return sorted(filtered, key=lambda x:x["num"], reverse=True)


def get_char_counts(text):
    txt_lower=text.lower()
    letter_counts = {}
    for letter in txt_lower:
        if letter in letter_counts:
            letter_counts[letter]+=1
        else:
            letter_counts[letter]=1
    return letter_counts


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
