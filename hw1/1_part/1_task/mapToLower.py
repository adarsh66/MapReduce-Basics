#!/usr/bin/python

import sys

def main():
#Takes line from standard input and prints out lower case
        for line in sys.stdin:
                line = line.strip()
                print line.lower()


#main() func is a recurring feature in all my code
#I like functions better than running the code like a script
#More readable for a human
if __name__ == '__main__':
        main()

