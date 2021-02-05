# MosoteachDownloader
用来下载蓝墨云班课上的资源

运行于Macos

本软件仅作学习用途

本软件使用Python写成，使用Tkinter可视化，依赖scrapy

要正常运行，需要先安装scrapy

编译时，先编译运行configure.py，再编译MosoteachDownloader.py

使用pyinstaller打包
先打包configure.py，参数使用-F，得到configure

再打包MosoteachDownloader.py，参数使用-F --noconsole (-i 图标地址)

之后进入MosoteachDownloader.app包中
将mosoteachSpider文件夹、scrapy.cfg以及刚打包的configure
放入MosoteachDownloader.app/Contents/MacOS中

完成打包


使用时，需要确保本机装有scrapy，并运行MosoteachDownloader.app/Contents/MacOS/configure进行初始化
