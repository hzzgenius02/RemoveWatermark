# RemoveWatermark
去除PDF中的水印，前提是水印的颜色与PDF的其它所有颜色都不一样

主要思路是：

1. 使用取色器工具获得水印的RGB，如示例代码里的灰色(243,243,243)~(254,254,254)

2. 将同目录下的PDF分解为图片放到PIC文件夹

3. 最后将该文件夹下所有图片的灰色像素点改为白色，存到RES文件夹

4. 手动将图片集合成为新的PDF文件

Requirements:

Python=3.8

pip install fitz

pip install pymupdf==1.18.14
