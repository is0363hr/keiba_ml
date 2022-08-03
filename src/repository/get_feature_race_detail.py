"""
レース詳細情報の取得
"""

import logging
from tokenize import Double
logger = logging.getLogger(__name__) #ファイルの名前を渡す

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import urllib.parse


race_data_columns = [
    'race_id',
    'race_track_name',
    'race_track_type',
    'participant_detail_link',
    'race_track_distance',
    'direction',
]


horse_data_columns = [
    'race_id',
    'horse_name',
    'horse_name_link',
    'horse_sex',
    'horse_weight',
    'jockey',
    'trainer',
    'odds',
    'population',
]


def get_race_detail(url):
    WAIT_SECOND = 5
    options = Options()
    # ヘッドレスモードを有効(画面を表示せずに動作するモード)
    options.add_argument('--headless')
    options.add_argument('--lang=ja-JP')
    driver = webdriver.Chrome(options=options)
    # # 設定した待ち時間を越えても要素が見つからない場合は、Exceptionが発生
    driver.implicitly_wait(10)
    driver.get(url)
    title = driver.find_element(By.CLASS_NAME, 'SpecialMainImageData')
    race_track_name = title.text.split(' ')[0] # 競馬場名
    tem = title.text.split(' ')[1]
    race_track_type = tem[:1] # 芝、ダ、障
    race_track_distance = tem[1:] # 距離
    
    tem = driver.find_element(By.CLASS_NAME, 'Title_BtnMore').find_elements(By.TAG_NAME, "a")
    participant_detail_link = tem[0].get_attribute("href") # 出場馬の詳細リンク取得
    
    driver.get(participant_detail_link)
    tem = driver.find_element(By.CLASS_NAME, 'RaceData01')
    direction = tem.text.split('(')[1][:1] # 左、右回り
    
    tem_tbody = driver.find_element(By.TAG_NAME, 'tbody')
    tem_tr = tem_tbody.find_elements(By.TAG_NAME, 'tr')
    
    race_list = []
    race_list.append({
        'race_id': urllib.parse.parse_qs(urllib.parse.urlparse(participant_detail_link).query)['race_id'],
        'race_track_name': race_track_name,
        'race_track_type': race_track_type,
        'race_track_distance': race_track_distance,
        'direction': direction,
    })
    
    horse_list = []
    for tr in tem_tr:
        horse_name = tr.find_element(By.CLASS_NAME, 'HorseName').text # 馬名
        horse_name_link_tem = tr.find_element(By.CLASS_NAME, 'HorseName').find_elements(By.TAG_NAME, "a")
        horse_name_link = horse_name_link_tem[0].get_attribute("href") # 馬詳細リンク
        horse_sex = tr.find_element(By.CLASS_NAME, 'Barei').text # 性齢
        horse_weight = tr.find_element(By.CLASS_NAME, 'Txt_C').text # 体重
        jockey = tr.find_element(By.CLASS_NAME, 'Jockey').text # 騎手名
        trainer = tr.find_element(By.CLASS_NAME, 'Trainer').text # 厩舎
        odds = tr.find_element(By.CLASS_NAME, 'Txt_R').text # オッズ
        population = tr.find_element(By.CLASS_NAME, 'Popular_Ninki').text # 人気順
        
        horse_list.append({
            'horse_name': horse_name,
            'horse_name_link': horse_name_link,
            'horse_sex': horse_sex,
            'horse_weight': horse_weight,
            'jockey': jockey,
            'trainer': trainer,
            'odds': odds,
            'population': int(population),
        })
    return race_list, horse_list


def main():
    URL = "https://race.netkeiba.com/special/index.html?id=0085"
    get_race_detail(URL)


if __name__ == '__main__':
    main()
    