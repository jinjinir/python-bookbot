#!/usr/bin/env python3

def read_book(book):
    with open(book) as f:
        return f.read()


def main():
    book_loc = "books/frankenstein.txt"
    book_text = read_book(book_loc)
    print(book_text)


if __name__ == "__main__":
    main()
