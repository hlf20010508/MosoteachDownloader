import os
import frozen_dir
from custom_widget import Warning
path=frozen_dir.app_path()
f=os.popen('which scrapy')
location=f.read()
f.close()
if len(location)!=0:
    fp=open(path+'/scrapyLocation.txt','w+')
    fp.write(location.strip('\n'))
    fp.close()
    Warning(['初始化成功!'],1,True)
else:
    Warning(['请先安装scrapy模块!','尝试在终端输入命令','pip3 install scrapy'],3,True)
print('\nfinished')