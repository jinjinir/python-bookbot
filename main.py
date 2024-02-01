#!/usr/bin/env python3

def read_book(book):
    with open(book) as f:
        return f.read()


def count_words(book_content):
    words = book_content.split()
    # return print(words)
    return len(words)


def char_counter(book_content):
    char_dict = {}
    for i in book_content:
        low_case = i.lower()
        if low_case in char_dict:
            char_dict[low_case] += 1
        else:
            char_dict[low_case] = 1
    return char_dict


def sort_on(d):
    return d["count"]


def sort_chars(char_count):
    sorted_list = []
    for i in char_count:
        sorted_list.append({"char": i, "count": char_count[i]})
    sorted_list.sort(reverse=False, key=sort_on)
    return sorted_list


def main():
    book_loc = "books/frankenstein.txt"
    book_content = read_book(book_loc)
    book_words = count_words(book_content)
    char_count = char_counter(book_content)
    sorted_char_list = sort_chars(char_count)
    # print(f"Total words in the book: {book_words}")
    # print(f"Total chars in the book: {char_count}")
    # print(f"List of sorted chars: {sorted_char_list}")
    print("+++++++++++++++++++++++++++++++++++")
    print(f"--- Begin report of {book_loc} ---")
    print("+++++++++++++++++++++++++++++++++++")
    print(f"{book_words} words found in the document")
    print()

    for item in sorted_char_list:
        if not item["char"].isalpha():
            continue
        print(
            f"The '{item['char']}' character was found {item['count']} times")

    print("+++++++++++++++++++++++++++++++++++")
    print(f"--- End report of {book_loc} ---")
    print("+++++++++++++++++++++++++++++++++++")


if __name__ == "__main__":
    main()
