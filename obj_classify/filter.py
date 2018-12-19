import cv2
import matplotlib.pyplot as plt
import numpy as np
import sys, os
from PIL import Image
import glob


#入力ファイルのパスを指定
in_jpg =  "./image/white_chocolate/"

#出力ファイルのパスを指定
out_jpg = "./image/white_chocolate/"


#リストで結果を返す関数
def get_file(dir_path):
    filenames = os.listdir(dir_path)
    return filenames


pic = get_file(in_jpg)

no = 1
for i in pic:
    # 画像の読み込み
    image_gs = cv2.imread(in_jpg + i)

    # 5*5の箱型フィルタ
    blur = cv2.blur(image_gs, (5,5))
    save_path = out_jpg + '/' + 'out_('  + str(i) +')' + str(no) + '_box_5*5.png'
    a = cv2.imwrite(save_path, blur)

    # 10*10の箱型フィルタ
    blur = cv2.blur(image_gs, (10,10))
    save_path = out_jpg + '/' + 'out_('  + str(i) +')' + str(no) + '_box_10*10.png'
    a = cv2.imwrite(save_path, blur)

    # 5*5のガウシアンフィルタ
    blur = cv2.GaussianBlur(image_gs, (5, 5), 0)
    save_path = out_jpg + '/' + 'out_('  + str(i) +')' + str(no) + '_gaussian_5*5.png'
    a = cv2.imwrite(save_path, blur)

    #　10*10のガウシアンフィルタ
    #blur = cv2.GaussianBlur(image_gs, (10, 10), 0)
    #save_path = out_jpg + '/' + 'out_('  + str(i) +')' + str(no) + '_gaussian_10*10.png'
    #a = cv2.imwrite(save_path, blur)

    #　中央値フィルタ
    blur = cv2.medianBlur(image_gs, 5)
    save_path = out_jpg + '/' + 'out_('  + str(i) +')' + str(no) + '_median.png'
    a = cv2.imwrite(save_path, blur)

    # バイラテラルフィルタ（エッジを強調しつつ、画像全体をぼかす）
    blur = cv2.bilateralFilter(image_gs, 9, 75, 75)
    save_path = out_jpg + '/' + 'out_('  + str(i) +')' + str(no) + '_bilateral.png'
    a = cv2.imwrite(save_path, blur)

     # 左右の反転
    blur = cv2.flip(image_gs, 1)
    save_path = out_jpg + '/' + 'out_('  + str(i) +')' + str(no) + '_flip1.png'
    a = cv2.imwrite(save_path, blur)

     # 上下の反転
    blur = cv2.flip(image_gs, 0)
    save_path = out_jpg + '/' + 'out_('  + str(i) +')' + str(no) + '_flip0.png'
    a = cv2.imwrite(save_path, blur)



    print(no)
    no+=1
