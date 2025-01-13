#!/usr/bin/python3
import sys

if __name__ == "__main__":
    for i in range(1, len(sys.argv)):  # Commence à 1 au lieu de 0
        print(sys.argv[i])