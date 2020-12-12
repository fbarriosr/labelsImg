import glob
import os
import pickle
import xml.etree.ElementTree as ET
from os import listdir, getcwd
from os.path import join

dirs = ['000','100', '200', '300', '400', '500', '600', '700','800', '900']
classes = ['achicoria', 'maleza']

def getImagesInDir(dir_path):
    image_list = []
    for filename in glob.glob(dir_path + '/*.jpg'):
        image_list.append(filename)

    return image_list

def convert(size, box):
    dw = round(1./(size[0]), 6)
    dh = round(1./(size[1]), 6)
    x = round((box[0] + box[1])/2.0 - 1, 6)
    y = round((box[2] + box[3])/2.0 - 1, 6)
    w = round(box[1] - box[0], 6)
    h = round(box[3] - box[2], 6)
    x = round(x*dw, 6)
    w = round(w*dw, 6)
    y = round(y*dh, 6)
    h = round(h*dh, 6)
    print(x,y,w,h)
    return (x,y,w,h)

def convert_annotation(dir_path, output_path, image_path):
    basename = os.path.basename(image_path)
    basename_no_ext = os.path.splitext(basename)[0]

    in_file = open(dir_path + '/' + basename_no_ext + '.xml')
    out_file = open(output_path + basename_no_ext + '.txt', 'w')
    tree = ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)

    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes or int(difficult)==1:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text), float(xmlbox.find('ymax').text))
        bb = convert((w,h), b)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')

cwd = getcwd()

for dir_path in dirs:
    full_dir_path = cwd + '/' + dir_path
    output_path = full_dir_path +'/yolo/'

    if not os.path.exists(output_path):
        os.makedirs(output_path)

    image_paths = getImagesInDir(full_dir_path)
    #list_file = open(full_dir_path + '.txt', 'w')

    for image_path in image_paths:
        #list_file.write(image_path + '\n')
        convert_annotation(full_dir_path, output_path, image_path)
    #list_file.close()

    print("Finished processing: " + dir_path)



with open ("classes.names", "w") as f: #Creamos el archivo
    f.write('\n'.join(classes)+'\n') #<-Escribimos en el
    f.close()