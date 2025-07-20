#!/usr/bin/env python3

# full imports
import argparse
import sys
# partial imports
from pathlib import Path

def get_text(file_path):    
    try:
        return file_path.read_text()
    except FileNotFoundError:
        print(f"Not sure how you got here. Path should have caught this issue ahead of time...but congrats on being statistically improbable.")
        return ""

def main():
    # CLI Setup
    parser = argparse.ArgumentParser(
        prog="Simple text swapper",
        usage="[TO-DO] - use this for the params you add, tripple quote and stack as needed.",
        description="Will swap pre-defined text blocks (in the input text) with argument defined text.",
        epilog="I'm poopen",
    )

    parser.add_argument("--file", help="relative file path", default="cover_letter.txt")
    #parser.add_argument("name", help="", type=)
    #parser.add_argument("name", help="", type=)
    #parser.add_argument("name", help="", type=)
    #parser.add_argument("name", help="", type=)
    #parser.add_argument("name", help="", type=)
    #parser.add_argument("name", help="", type=)
    #parser.add_argument("name", help="", type=)
    #parser.add_argument("name", help="", type=)
    args = parser.parse_args()

    print("You tried to use: " + args.file)

    # Read the file in, if it is indeed a file
    file_path = Path(args.file)
    if not file_path.is_file():
        raise FileNotFoundError(f"You dun goofed, {file_path} is not a file or DNE")
    else:
        letter_text = get_text(file_path)

        

if __name__ == "__main__":
    main()
