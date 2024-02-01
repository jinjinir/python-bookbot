# Python Bookbot

## Project Description
This is a guided project from [boot.dev](https://www.boot.dev/) which aims to showcase what I have learned from their Python course.
The application takes in a text file, preferrably a book, and counts the number of instances a character is used.

## Installation
- Ensure that you have the latest Python version. `Python 3.10.13` was used to build this project.
- Clone the repository locally.
  ```bash
  git clone https://github.com/jinjinir/python-bookbot
  ```

## Usage
- `cd` into the project:
  ```bash
  cd python-bookbot 
  ```
- Edit `main.py` and replace the value of `book_loc` in the `main()` function. Pass the path of the book/text you want the application to run against.
  It's recommended to make a `books` directory and place the book/text there.
- Run the application:
  ```bash
  python3 main.py
  ```
- The application will count the number of times a character (letter) is used in the text and will print out a report on how frequently it was used. 
  Think of it as something like the `wc` utility in `*nix`-based systems.
