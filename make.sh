#! /bin/bash
pip3 install pyinstaller
pip3 install scrapy
rm -rf scrapyLocation.txt
which scrapy >> scrapyLocation.txt
pyinstaller -F MosoteachDownloader.py --noconsole -i 104-2101151J3550-L.icns
export path=dist/MosoteachDownloader.app/Contents/MacOS
cp -r mosoteachSpider scrapy.cfg scrapyLocation.txt $path
cp -r dist/MosoteachDownloader.app /Applications
