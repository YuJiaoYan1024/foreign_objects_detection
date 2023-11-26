# .txt-->.xml
# ! /usr/bin/python
# -*- coding:UTF-8 -*-
import os
import cv2


def txt_to_xml(txt_path, img_path, xml_path):
    # 标签中标注的类别及所用的数字代号
    dict = {
        '0': 'bolt',
        '1': 'bulk',
        '2': 'gangue',
        '3': 'other'
    }

    files = os.listdir(txt_path)
    pre_img_name = ''
    # 遍历文件内的TXT文件
    for i, name in enumerate(files):
        print(name)

        txtFile = open(txt_path + name)
        txtList = txtFile.readlines()
        # 获取TXT文件所对应的原始图片的名称
        img_name = name.split(".t")[0]

        pic = cv2.imread(img_path + img_name + ".jpg")
        if pic is None:
            pic = cv2.imread(img_path + img_name + ".bmp")
        # 获取图像大小信息
        Pheight, Pwidth, Pdepth = pic.shape
        # 读取TXT文件中每一行的标签信息（每一行代表一个标注目标的位置信息）
        for row in txtList:
            # 按' '分割txt的一行的内容
            oneline = row.strip().split(" ")
            # 遇到的是一张新图片
            if img_name != pre_img_name:
                # 将标签信息写进xml文件
                xml_file = open((xml_path + img_name + '.xml'), 'w')
                xml_file.write('<annotation>/n')
                xml_file.write('    <folder>VOC2007</folder>/n')
                xml_file.write('    <filename>' + img_name + '.jpg' + '</filename>/n')
                xml_file.write('<path>C:/Users/GXUFE-204/Desktop/yolov5/datasets/guang/ceshi/imagetest</path>/n')
                xml_file.write('<source>/n')
                xml_file.write('<database>orgaquant</database>/n')
                xml_file.write('<annotation>organoids</annotation>/n')
                xml_file.write('</source>/n')
                xml_file.write('    <size>/n')
                xml_file.write('        <width>' + str(Pwidth) + '</width>/n')
                xml_file.write('        <height>' + str(Pheight) + '</height>/n')
                xml_file.write('        <depth>' + str(Pdepth) + '</depth>/n')
                xml_file.write('    </size>/n')
                xml_file.write('    <object>/n')
                xml_file.write('<name>' + dict[oneline[0]] + '</name>/n')
                xml_file.write('        <bndbox>/n')
                xml_file.write('            <xmin>' + str(
                    int(((float(oneline[1])) * Pwidth + 1) - (float(oneline[3])) * 0.5 * Pwidth)) + '</xmin>/n')
                xml_file.write('            <ymin>' + str(
                    int(((float(oneline[2])) * Pheight + 1) - (float(oneline[4])) * 0.5 * Pheight)) + '</ymin>/n')
                xml_file.write('            <xmax>' + str(
                    int(((float(oneline[1])) * Pwidth + 1) + (float(oneline[3])) * 0.5 * Pwidth)) + '</xmax>/n')
                xml_file.write('            <ymax>' + str(
                    int(((float(oneline[2])) * Pheight + 1) + (float(oneline[4])) * 0.5 * Pheight)) + '</ymax>/n')
                xml_file.write('        </bndbox>/n')
                xml_file.write('    </object>/n')
                xml_file.close()
                pre_img_name = img_name  # 将其标记为已经转换过的图片
            else:  # 转换过的图片
                # 同一张图片，只需要追加写入object
                xml_file = open((xml_path + img_name + '.xml'), 'a')
                xml_file.write('    <object>/n')
                xml_file.write('<name>' + dict[oneline[0]] + '</name>/n')
                '''  按需添加这里和上面
                xml_file.write('        <pose>Unspecified</pose>/n')
                xml_file.write('        <truncated>0</truncated>/n')
                xml_file.write('        <difficult>0</difficult>/n')
                '''
                xml_file.write('        <bndbox>/n')
                xml_file.write('            <xmin>' + str(
                    int(((float(oneline[1])) * Pwidth + 1) - (float(oneline[3])) * 0.5 * Pwidth)) + '</xmin>/n')
                xml_file.write('            <ymin>' + str(
                    int(((float(oneline[2])) * Pheight + 1) - (float(oneline[4])) * 0.5 * Pheight)) + '</ymin>/n')
                xml_file.write('            <xmax>' + str(
                    int(((float(oneline[1])) * Pwidth + 1) + (float(oneline[3])) * 0.5 * Pwidth)) + '</xmax>/n')
                xml_file.write('            <ymax>' + str(
                    int(((float(oneline[2])) * Pheight + 1) + (float(oneline[4])) * 0.5 * Pheight)) + '</ymax>/n')
                xml_file.write('        </bndbox>/n')
                xml_file.write('    </object>/n')
                xml_file.close()

        # 8.读完txt文件最后写入</annotation>
        xml_file1 = open((xml_path + pre_img_name + '.xml'), 'a')
        xml_file1.write('</annotation>')
        xml_file1.close()
    print("Done !")


# 修改文件夹的路径， 注意文件夹最后要加上/
txt_to_xml("./dataset/labels/",  # txt_path
           "./dataset/images/",  # img_path
           "./dataset/xml_labels/")  # xml_path  用来保存转换后生成的xml文件