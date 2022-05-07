# -*- coding: utf-8 -*-
"""
Created on Sat May  7 14:27:43 2022

@author: Usuario1
"""

import pathlib
import os
import time

cf = (os.path.basename(__file__))

print('Tracing directory...')
time.sleep(3)

r = pathlib.Path().absolute()
print(f'Directory: {r}.')

print('Tracing documents and archives...')
time.sleep(4)

contents = os.listdir(r)
print(contents)

print('Deleting documents and archives...')
time.sleep(5)

for i in contents:
    if i == cf:
        pass
    else:
        os.remove(i)
        print(f'{i} deleted.')

print('All documents and archives succesfully deleted.')



