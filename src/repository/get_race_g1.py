###
# 重賞レース日程の取得
###

import logging
logger = logging.getLogger(__name__) #ファイルの名前を渡す

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from datetime import datetime, date


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
    text_race_year = title.text.split('年')[0]
    schedule_ = race_calendar.find_element(By.TAG_NAME, 'tbody')
    trs = schedule_.find_elements(By.TAG_NAME, "tr")
    
    # race_list_header = 
    race_list = []
    # ヘッダ行は除いて取得
    try:
        for i in range(1, len(trs)):
            tds = trs[i].find_elements(By.TAG_NAME, "td")
            tem = []
            for j in range(0, len(tds)):
                tem.append(tds[j].text)
                if j == 1:
                    element_a = tds[j].find_elements(By.TAG_NAME, "a")
                    if len(element_a) == 0:
                        tem.append('-')
                    else:
                        tem.append(element_a[0].get_attribute("href"))
            tem_race_date = date(int(text_race_year), int(tem[0].split('(')[0].split('/')[0]), int(tem[0].split('(')[0].split('/')[1]))
            
            race_list.append({
                'race_date': tem_race_date.strftime('%Y-%m-%d'),
                'race_name': tem[1],
                'race_detail_link': tem[2],
                'race_grade': tem[3],
                'race_city': tem[4],
                'race_distance': tem[5],
                'race_terms': tem[6],
                'race_weight': tem[7],
            })
        return race_list
    except Exception:
        logger.info("error get_race_schedule")

def main():
    data = get_race_schedule()
    print(data)
    

if __name__ == '__main__':
    main()
