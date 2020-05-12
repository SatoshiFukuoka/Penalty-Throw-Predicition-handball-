from keras.models import load_model
from keras.preprocessing.image import img_to_array #PIL形式からndarrayに変換する
import os
import numpy as np
import cv2 #OpenCV
import time

model_dir = './'
model_name = 'model.h5'

#モデルの読み込み
model = load_model(os.path.join(model_dir, model_name))

image_path = 'data/test'
image_names = os.listdir(image_path) #ファイル、ディレクトリの一覧を取得

for image in image_names: #写真の一枚ずつ読み込む
    start = time.time() # 現在時刻
    img = cv2.imread(os.path.join(image_path,image), 3) #３チャンネルカラー画像として読み込む
    img = img.astype('float')/256 #正規化
    img = img_to_array(img) #PIL形式からndarrayに変換する
    img = np.expand_dims(img, axis=0) #次元の追加

    pred = model.predict(img) #予測値
    pred = pred.argmax(axis=1)[0] #予測

#結果のラベル
    label = ""
    if(pred == 0):
        label = "left"
    elif(pred == 1):
        label = "right"
    else:
        label = "unknown"

    end = time.time()

    img = cv2.imread(os.path.join(image_path,image), 3)
    cv2.putText(img, label, (3,20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 2)
    #画像にテキストを書き込む

    time_diff = str(end-start) + " sec" #かかった時間
    cv2.putText(img, time_diff, (180,20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 2)
    #かかった時間を書き込む
    cv2.imshow("img", img) #画像を表示
    cv2.waitKey(0) #キーボードを押したら次へ
