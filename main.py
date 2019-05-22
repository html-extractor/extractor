import sys

import requests
from bs4 import BeautifulSoup
from selenium import webdriver

url = 'http://v.media.daum.net/v/20170615203441266'


options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")
options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")
options.add_argument("lang=ko_KR") 

#드라이버
driver = webdriver.Chrome('/Users/CAU/source/repos/extractor/chromedriver_win32/chromedriver.exe', chrome_options=options)
#driver = webdriver.PhantomJS('/Users/CAU/source/repos/extractor/phantomjs-2.1.1-windows/bin/phantomjs')

driver.execute_script("Object.defineProperty(navigator, 'plugins', {get: function() {return[1, 2, 3, 4, 5]}})")
# lanuages 속성을 업데이트해주기
driver.execute_script("Object.defineProperty(navigator, 'languages', {get: function() {return ['ko-KR', 'ko']}})")


driver.get(url)

#driver.get('http://v.media.daum.net/v/20170615203441266')
driver.implicitly_wait(3)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

while True:
    #selector address
    print("Address 입력")
    selector = input()
    if selector == "exit":
        break
    try:
        notices = soup.select(selector)
    except :
        print("error")
    else :
        for i in notices :
            print(i)
        print('\n')
    
