import logging
logger = logging.getLogger(__name__) #ファイルの名前を渡す

from selenium import webdriver
from selenium.webdriver.support.ui import Select,WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

from pprint import pprint
from datetime import datetime

URL = "https://race.netkeiba.com/top/schedule.html?rf=sidemenu"
WAIT_SECOND = 5


def get_race_schedule():
    options = Options()
    # ヘッドレスモードを有効(画面を表示せずに動作するモード)
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    # 設定した待ち時間を越えても要素が見つからない場合は、Exceptionが発生
    driver.implicitly_wait(10)
    driver.get(URL)
    
    race_calendar = driver.find_element(By.CLASS_NAME, 'Race_Calendar_List')
    title = race_calendar.find_element(By.CLASS_NAME, 'TitleHeadingNoLine')
    print(title.text)
    schedule_ = race_calendar.find_element(By.TAG_NAME, 'tbody')
    trs = schedule_.find_elements(By.TAG_NAME, "tr")
    
    # race_list_header = 
    race_list = []
    # ヘッダ行は除いて取得
    try:
        for i in range(1, len(trs)):
            tds = trs[i].find_elements(By.TAG_NAME, "td")
            line = ""
            tem = []
            for j in range(0, len(tds)):
                tem.append(tds[j].text)
                if j == 1:
                    element_a = tds[j].find_elements(By.TAG_NAME, "a")
                    print(tds[j].text)
                    if len(element_a) == 0:
                        tem.append('-')
                    else:
                        tem.append(element_a[0].get_attribute("href"))
            tem.append(datetime.now())
            race_list.append(tem)
            print(race_list)
            break
        # print('---')
        # pprint(race_list)
    except Exception:
        logger.info("error get_race_schedule")

def main():
    get_race_schedule()
    


if __name__ == '__main__':
    main()
