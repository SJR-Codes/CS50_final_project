"""
* CS50P Problem Set 7
* Watch on YouTube
* by Samu Reinikainen 28.07.2022
"""

import re
import sys


def main():
    print(parse(input("HTML: ")))
    #url = '<iframe src="http://www.youtube.com/embed/xvFZjo**gG0"></iframe>'
    print(parse(url))


def parse(s):
    p = r"src=\"https?://(?:www\.)?youtube\.com/embed/(\w*)"
    if m := re.search(p, s, re.IGNORECASE):
        return "https://youtu.be/" + m.group(1)


if __name__ == "__main__":
    main()