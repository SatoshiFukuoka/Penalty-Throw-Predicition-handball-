# Handball-Penalty-Throw-Predicition

## ハンドボールのペナルティースローおけるシュートコースを予測するCNN分類器です。シュートを打つ直前の画像にコースを表示します。

## 使い方
1.以下のdataダウンロード
https://d.kuku.lu/48277d9a1f

2.'./data'に置く

3.以下のトレーニング済みのmodelをダウンロード
https://d.kuku.lu/6854d70016

4.'./'に置く

5.python predict.py を実行する

## 環境
Tensorflow 2.1.0
Keras 2.3.1
python 3.6.6

## 追記
'./'にあるleft,rightフォルダにjpg画像をいれ

python resize.py left

python resize.py right

と実行することで

'./data'にあるleft,rightフォルダにリサイズされたjpg画像が入る
