#!/usr/bin/env python
#coding:utf-8
#from scan results import here

import os

result_path = 'down/'
save_path = 'IncExtensiveList/'

for i in os.listdir(result_path):
    save_tmp = set()

    if os.path.isdir(result_path+i):
        for j in os.listdir(result_path+i):
            result_tmp = result_path+i+'/'+j+'/extensive_ip.txt'
            if os.path.isfile(result_tmp):
                for f in open(result_tmp):
                    save_tmp.add(f.strip())

    if save_tmp:
        save_file = save_path + i + '.txt'
        try:
            os.remove(save_file)
        except:
            pass
        finally:
            f = open(save_file,'a')
            for i in save_tmp:
                f.write(i+'\n')
            f.close()