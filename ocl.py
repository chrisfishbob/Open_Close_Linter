#!/usr/bin/python3
import sys


def main():
    with open(sys.argv[1]) as f:
        contents = f.readlines()
        parse_lines(contents)
 

def parse_lines(contents):
    current_line_num = 1

    for line in contents:
        check_open_close(contents, line, current_line_num)
        check_quotes(contents, line, current_line_num)
        current_line_num += 1


def check_open_close(contents, line, current_line_num):
    open_count, close_count = 0, 0
    
    for token in line:
        if is_open_token(token):
            open_count += 1
        elif is_close_token(token):
            close_count += 1
    
    if open_count != close_count:
        print("\n########################################")
        print("Potential issue on line", str(current_line_num) + ":")
        print(contents[current_line_num - 1])
        print("########################################\n\n")


def check_quotes(contents, line, current_line_num):
    single, double = 0, 0

    for token in line:
        if token == "'":
            single += 1
        elif token == '"':
            double += 1

    if single % 2 != 0 or double % 2 != 0:
        print("\n########################################")
        print("Potential issue on line", str(current_line_num) + ":")
        print(contents[current_line_num])
        print("########################################\n\n")


def is_open_token(token):
    open_token = ['(', "{", "["]
    return token in open_token


def is_close_token(token):
    close_token = [')', "}", "]"]
    return token in close_token 


if __name__ == "__main__":
    main()
