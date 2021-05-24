# from matplotlib.font_manager import FontProperties
# font = FontProperties(fname='/Users/wdt/Library/Fonts/KaiTi.ttf')

# 查询当前系统所有字体
from matplotlib.font_manager import FontManager
import subprocess

mpl_fonts = set(f.name for f in FontManager().ttflist)

print('all font list get from matplotlib.font_manager:')
for f in sorted(mpl_fonts):
    print('\t' + f)
    
import os
os.getcwd()


import matplotlib.pyplot as plt

from matplotlib import font_manager

for font in font_manager.fontManager.ttflist:

    if 'Kai' in font.name:
        print(font.name, '-', font.fname)

