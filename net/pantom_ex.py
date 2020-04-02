# -*- coding:utf-8 -*-


__all__=[
    'WEB_CRAWLER'
]


################################################################################
from selenium import webdriver
import urllib

from bs4 import BeautifulSoup as bs
################################################################################
from settings import CHROME_DRIVER, URL_MD5, URL_LOGIN, USER_ID, USER_PASSWD
################################################################################

WAIT_TIME = 10

class WEB_CRAWLER:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument('window-size=1920x1080')
        options.add_argument("disable-gpu")
        #options.add_argument("--disable-gpu")
        options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")
        options.add_argument("lang=ko_KR")

        self.driver = webdriver.Chrome(CHROME_DRIVER, chrome_options=options)
        self.driver.implicitly_wait(WAIT_TIME)


    def url_login(self, u_id=USER_ID, u_passwd=USER_PASSWD):
        self.driver.get(URL_LOGIN)
        self.driver.find_element_by_name('user_id').send_keys(u_id)
        self.driver.find_element_by_name('user_password').send_keys(u_passwd)
        self.driver.find_element_by_xpath("//div[@class='col-sm-offset-3']/button[@class='btn btn-primary']").click()


    def get_report(self, hash_md5):
        md5_encode = urllib.urlencode({'md5': hash_md5}).encode('utf-8')
        self.driver.get(URL_MD5 + '?' + md5_encode)
        html = self.driver.page_source

        soup = bs(html, 'html.parser')
        my_titles = soup.select('table > tbody > tr')

        for title in my_titles:
            if title.find('td').text == 'ViRobot Mobile for Android 1.0':
                return title.find_all('td', limit=4)[3].text
        

    def close(self):
        self.driver.quit()        

   
