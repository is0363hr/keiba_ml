# 競馬予測プログラム(Python)

## データ対象

https://db.netkeiba.com/?pid=race_search_detail

## ファイル概要

- get_race_url.py: seleniumでレースURLを取得する
- get_race_html.py: URLを使用してhtmlを取得する
- make_csv_from_html.py: htmlからレースデータや馬のデータを抽出してCSVにする
- main.py: 以上のことを一度に実行する
- data_clean.ipynb: 得られたcsvを整形する
- train_simple.py: 単純なモデルをkerasで作成する
- train_timesplit.py: 時系列を考慮したクロスバリデーション
- train_hyperas.py: hyperasを用いて自動パラメータチューニングを行う
- train_hyperas_no_obstacle.py: train_hyperas.pyとは違い、学習データから障害レースを取り除く
- evaluate_prediction.ipynb: モデルの予測値の評価を行う


## 定期実行ファイル

- get_race_g1.py: 年に一回
- (get_race_detail_g1.py: レースごとに必要)
- 予測のための特徴量データの作成


## 注意

ログはlogfileディレクトリ、htmlはrace_htmlディレクトリ、モデルはmodelディレクトリ、予想結果はpredictディレクトリに保存される。

# Encvironment

## Python

|  Library  |  Version  |
| ---- | ---- |
|  selenium  |  4.3.0  |
|  pandas  |  1.4.3  |
|  matplotlib  |  3.5.2  |
|  requests  |  2.28.1  |
|  beautifulsoup4  |  4.11.1  |
|  chromedriver-binary  |  104.0.5112.20.0  |
|  jupyter  |  1.0.0  |
|  scikit-learn  |  1.1.1  |
|  tensorflow-macos  |  2.9.2  |
|  SQLAlchemy  |  1.4.39  |
|  PyMySQL  |  1.0.2  |

* 実行パス：src直下

## Feature

netkeiba.com

### 予測

- 順位
- (ゴールタイム)

### 学習

#### [get_feature_race_detail][1]

- 枠番
- 馬番
- 性別
- 年齢
- 騎手
- 厩舎
- 予想オッズ
- 人気
- (レース名)
- レースに参加する馬の数
- 開催地
- 距離
- 芝かダートか
- コースが右回りか左回りか直線か
- ランク
- 過去5年のレース

#### [get_feature_race_overview][2]

- 過去5レースの情報
  - 近走成績
  - 場・芝ダ・距離
  - 着順・偏差値・上昇度

#### [get_feature_horce_info][3]

- 距離適正
- 脚質
- 負担重量（斤量）
- 日付
- 開催
- 頭数
- 枠番
- 馬番
- オッズ
- 人気
- 順位
- 騎手
- 距離
- (レース名)

計算して求める
- 前回と騎手やオーナーが変わっているかどうか
- 前回レースとの時間差
- 前回からの体重変化
- 障害レースかどうか

[1]:https://race.netkeiba.com/race/shutuba.html?race_id={race_id}&rf=race_submenu
[2]:https://race.sp.netkeiba.com/barometer/score.html?race_id={race_id}&rf=shutuba_submenu
[3]:https://db.netkeiba.com/horse/{horce_id}