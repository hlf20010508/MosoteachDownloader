用来下载蓝墨云班课上的资源

运行于Macos

本软件仅作学习用途

本软件使用Python写成，使用Tkinter可视化，依赖scrapy，需要chromedriver且chromedriver需要放置在系统应用程序文件夹中，需要pyinstaller来make

<br/>

通过源码编译方式如下：
```

git clone https://github.com/hlf20010508/MosoteachDownloader.git

cd MosoteachDownloader

bash make.sh
```
<br/>

软件将自动复制到系统应用程序文件夹中

如果要更改位置，可以更改make.sh中的最后一行

<br/>
使用方法：

点击更新Cookie

之后会弹出网页，登录成功后，不要关闭网页，回到程序，点击确定

自动返回起始页，点击更新数据

在蓝墨云班课中点击需要爬取的课程，点击资源，然后复制该页面的网址，填入软件的链接中，课程名称可以随意写，保存

然后可以双击列表中的课程，等待片刻，提示成功后，返回

点击下载文件

在列表中双击需要下载的文件即可
