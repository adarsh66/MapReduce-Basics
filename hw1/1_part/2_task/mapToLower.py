#!/usr/bin/python

import sys

def main():
        for line in sys.stdin:
                line = line.strip()
                print line.lower()

if __name__ == '__main__':
        main()

