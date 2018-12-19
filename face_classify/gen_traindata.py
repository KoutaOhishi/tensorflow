# -*- coding: utf-8 -*-
import sys
import os
import csv
 
if __name__ == '__main__':
  #outdir = sys.argv[1]
  outdir = './'
 
  if not os.path.isdir(outdir):
    sys.exit('%s is not directory' % outdir)
 
  names = {
    "trump_cut_images": 0,
    "etc_cut_images_1": 1,
  }
  #学習用のデータが入っているフォルダを指定
  
  #exts = ['.PNG','.JPG','.JPEG']
  exts = ['.jpg','.JPG']
 
  f = open('train.csv', 'w')
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
