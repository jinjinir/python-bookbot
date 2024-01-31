#!/usr/bin/env python3

def read_book(book):
    with open(book) as f:
        return f.read()
