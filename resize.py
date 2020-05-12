#画像のサイズを512×512に統一するためのプログラム

import cv2
import os,sys

input_path = sys.argv[1]
image_names = os.listdir('./'+input_path)#ファイル、ディレクトリの一覧を取得
output_path = './data/'+ input_path
output_image_num = 0

for image in image_names:
    print(image)
    # まず、画像を読み込む
    img = cv2.imread(os.path.join(input_path,image), cv2.IMREAD_COLOR)

    #リサイズ
    newimg = cv2.resize(img,(512,512))
    #ファイルへ書き込み
    cv2.imwrite(os.path.join(output_path, str(output_image_num))+".jpg", newimg)


    output_image_num += 1

print("変換終了です！")
