#!/usr/bin/python3

# なんかわかんないけどimport必要らしいc3po
import cv2
# あとnumpy(でかぱいみたいだね)
import numpy as np

# 単純にディレクトリパス
dirpath = '/home/tsubu/repos/larning_1/image/'
# wget URL で落としてきたファイル名 curlでも行けるらしいけど、オプションとかめんどそうだった
filename = 'fruits.jpg'

# 読み込み処理
'''
cv2.IMREAD_COLOR デフォルト。カラーモード 1
cv2.IMREAD_GRAYSCALE グレースケール 0
cv2.IMREAD_UNCHANGED -1
'''
print(dirpath + filename)
img = cv2.imread(dirpath + filename, 1)

# 画像表示？
'''
imshow(windowname, img)
表示時のウインドウの名前, 読み込み済みの画像オブジェクト
'''
cv2.imshow('image', img)

# キーの入力待ち
cv2.waitKey(0)

# ウィンドウ閉じる
cv2.destroyAllWindows()