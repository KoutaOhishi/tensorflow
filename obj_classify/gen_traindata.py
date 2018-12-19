# -*- coding: utf-8 -*-
import sys
import os
import csv
 
if __name__ == '__main__':
  #outdir = sys.argv[1]
  #outdir = './image/'
  outdir = './test_image/'
  
  if not os.path.isdir(outdir):
    sys.exit('%s is not directory' % outdir)
 
  names = {
    "BOSS_black_coffee": 0,
    "Royal_milk_tea": 1,
    "acerolajuice": 2,
    "apple": 3,
    "black_chocolate": 4,
    "cafe_au_lait": 5,
    "chip_star1": 6,
    "chip_star2": 7,
    "chip_star3": 8,
    "cookie": 9,
    "cupnoodle": 10,
    "dish_cleaner": 11,
    "egg_soup": 12,
    "georgia_emerald_mountain": 13,
    "grape_fruit_juice": 14,
    "green_tea": 15,
    "iced_tea": 16,
    "japanese_dressing": 17,
    "korean_soup": 18,
    "onion_dressing": 19,
    "orange": 20,
    "orange_juice": 21,
    "potage_soup": 22,
    "potato_stick": 23,
    "red_tea": 24,
    "seafood_noodle": 25,
    "strawberry_juice": 26,
    "white_chocolate": 27,
    
  }
  #学習用のデータが入っているフォルダを指定
  
  exts = ['.PNG','.JPG','.JPEG']
  #exts = ['.jpg','.JPG']
 
  #f = open('train.csv', 'w')
  f = open('test.csv', 'w')
  writer = csv.writer(f, lineterminator='\n')
 
  for dirpath, dirnames, filenames in os.walk(outdir):
    for dirname in dirnames:
      if dirname in names:
        n = names[dirname]
        member_dir = os.path.join(dirpath, dirname)
        for dirpath2, dirnames2, filenames2 in os.walk(member_dir):
          if not dirpath2.endswith(dirname):
            continue
          for filename2 in filenames2:
            (fn,ext) = os.path.splitext(filename2)
            if ext.upper() in exts:
              #img_path = os.path.join(dirpath2, filename2)
              img_path = os.path.join(filename2)
              print ('%s %s' % (img_path, n))
              writer.writerow([img_path, n])
  f.close()
