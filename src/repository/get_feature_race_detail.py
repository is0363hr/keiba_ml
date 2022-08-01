"""
レース詳細情報の取得
"""

import logging
logger = logging.getLogger(__name__) #ファイルの名前を渡す

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def get_race_detail(url):
    WAIT_SECOND = 5
    options = Options()
    # ヘッドレスモードを有効(画面を表示せずに動作するモード)
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    # 設定した待ち時間を越えても要素が見つからない場合は、Exceptionが発生
    driver.implicitly_wait(10)
    driver.get(url)
    title = race_calendar.find_element(By.CLASS_NAME, 'TitleHeadingNoLine')


def main():
    #TODO race_idはデータベースから取得
    URL = "https://race.netkeiba.com/special/index.html?id=0076"
    get_race_detail(URL)


if __name__ == '__main__':
    URL = "https://race.netkeiba.com/special/index.html?id=0076"