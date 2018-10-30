# -*- coding: utf-8 -*-
#!/usr/bin/python
#test_copyfile.py
import os,shutil
def mymovefile(srcfile,dstfile):
    if not os.path.isfile(srcfile):
        print ("==="+srcfile)
    else:
        fpath,fname=os.path.split(dstfile)    #分离文件名和路径
        if not os.path.exists(fpath):
            os.makedirs(fpath)                #创建路径
        shutil.copyfile(srcfile,dstfile)          #移动文件
        print ("move %s -> %s" ,srcfile,dstfile)
        
srcfile='./app/build/outputs/apk/xiaomi/release/AutoBuildTest-99-xiaomi-release.apk'
dstfile='D:/download/AutoBuildTest-v1.0.1-xiaomi-release.apk'
mymovefile(srcfile,dstfile)