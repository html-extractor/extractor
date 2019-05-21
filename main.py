import sys

from html import get_html

for arg in sys.argv:
    print(arg)

print(get_html("https://media.daum.net/ranking/age/"))
