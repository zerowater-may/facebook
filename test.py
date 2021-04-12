from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import os

class FaceBook:
    def __init__(self):
        super().__init__()
        USERNAME = 'zerowater'
        chrome_options = Options()
        chrome_options.add_argument(f'user-data-dir=/Users/{USERNAME}/AppData/Local/Google/Chrome/User Data')
        driver = webdriver.Chrome(chrome_options=chrome_options)
        driver.get('https://www.google.co.in')

    def get_group_members(self,data):
        '''공개그룹 or 허용가능한 그룹의 멤버리스트를 받아옵니다.'''
        self.url = data['url']
        self.number = data['number']


if '__main__' == __name__:
    fb = FaceBook()
    folderPath = os.path.dirname(os.path.realpath(__file__))
    print(folderPath)


    