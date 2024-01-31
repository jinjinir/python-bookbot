#!/usr/bin/env python3

def read_book(book):
    with open(book) as f:
        return f.read()


def count_words(book_content):
    words = book_content.split()
    # return print(words)
    return len(words)


def main():
    book_loc = "books/frankenstein.txt"
    book_content = read_book(book_loc)
    book_words = count_words(book_content)
    print(f"Total words in the book: {book_words}")


if __name__ == "__main__":
    main()
