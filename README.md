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
