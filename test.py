import fitz
import os
import cv2
import numpy as np


def func(doc):
    for i in range(len(doc)):
        imglist = doc.getPageImageList(i)
        for j, img in enumerate(imglist):
            xref = img[0]
            pix = fitz.Pixmap(doc, xref)  # make pixmap from image
            if pix.n - pix.alpha < 4:  # can be saved as PNG
                pix.writePNG("./pic/p%s-%s.png" % (i + 1, j + 1))
            else:  # CMYK: must convert first
                pix0 = fitz.Pixmap(fitz.csRGB, pix)
                pix0.writePNG("./pic/p%s-%s.png" % (i + 1, j + 1))
                pix0 = None  # free Pixmap resources
            pix = None  # free Pixmap resources


def remove():
    """
    将图片中灰色像素[RGB为(243,243,243)~(254,254,254)]的颜色改为（255，255，255）
    """
    list_file = os.listdir('./pic')
    print(list_file)
    for i in list_file:
        img_path = './pic/' + i
        image = cv2.imread(img_path)

        # 将RGB为（243，243，243）的颜色改为（255，255，255）
        for j in range(243, 254):
            image[np.all(image == [j, j, j], axis=2)] = [255, 255, 255]

        # 将处理后的图像保存到"./res/"目录下
        cv2.imwrite("./res/" + i, image)
# def remove():
#     """
#     将图片左侧100个像素列和最右侧100个像素列中红色通道大于25且绿色和蓝色通道小于20的像素改为（255, 255, 255）
#     """
#     list_file = os.listdir('./pic')
#     print(list_file)
#     for i in list_file:
#         img_path = './pic/' + i
#         image = cv2.imread(img_path)
#
#         # 定义要修改的左侧100个像素列和最右侧100个像素列
#         left_100_cols = image[:, :100, :]
#         right_100_cols = image[:, -100:, :]
#
#         # 分别找到左侧100个像素列和最右侧100个像素列中红色通道大于70且绿色和蓝色通道小于15的像素
#         left_mask = np.logical_and(left_100_cols[:, :, 2] > 25,
#                                    np.logical_and(left_100_cols[:, :, 1] < 20, left_100_cols[:, :, 0] < 20))
#         right_mask = np.logical_and(right_100_cols[:, :, 2] > 25,
#                                     np.logical_and(right_100_cols[:, :, 1] < 20, right_100_cols[:, :, 0] < 20))
#
#         # 将满足条件的像素分别改为（255, 255, 255）
#         left_100_cols[left_mask] = [255, 255, 255]
#         right_100_cols[right_mask] = [255, 255, 255]
#
#         # 将处理后的图像保存到"./res/"目录下
#         cv2.imwrite("./res/" + i, image)


if __name__ == "__main__":
    # 第一步 将pdf中所有图片写入文件夹
    func(doc=fitz.open('财管和资评笔记.pdf'))
    # 第二步  去除文件夹内所有图片的水印
    remove()
