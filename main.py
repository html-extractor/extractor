import argparse
import re
from pprint import pprint

import requests
from bs4 import BeautifulSoup


def get_html(url):
    # HTTP GET Request
    req = requests.get(url)

    # HTML 소스 가져오기
    html = req.text
    # HTTP Header 가져오기
    header = req.headers
    # HTTP Status 가져오기 (200: 정상)
    status = req.status_code
    # HTTP가 정상적으로 되었는지 (True/False)
    is_ok = req.ok

    return html


def parse(html, select):
    soup = BeautifulSoup(html, 'html.parser')
    parse_datas = soup.select(select)

    data = {}

    for parse_data in parse_datas:
        title = parse_data.text.strip().replace("\n", " ")
        title = re.sub(r" +", " ", title)
        data[title] = parse_data.get('href')

    return data


parser = argparse.ArgumentParser(description='CSS selector-based crawling.')
parser.add_argument('address', metavar='address', nargs=1, help='site address to crawl')
parser.add_argument('-s', '--selector', required=True, metavar='selector', nargs='+', help='css selector')
parser.add_argument('-f', '--format', metavar='format', nargs='?', default="json")

# parser.print_help()

args = parser.parse_args()

html = get_html(args.address[0])
css_selector = args.selector
if css_selector[-1] != 'a':
    css_selector.append('a')

data = parse(html, " ".join(css_selector))
pprint(data)
