#!/bin/bash
WORKING_DIR="custom"
if [ -d "$WORKING_DIR" ]; then rm -Rf $WORKING_DIR; fi

WORKING_DIR="images"
if [ -d "$WORKING_DIR" ]; then rm -Rf $WORKING_DIR; fi

WORKING_DIR="labels"
if [ -d "$WORKING_DIR" ]; then rm -Rf $WORKING_DIR; fi

file="custom.zip"

if [ -f "$file" ] ; then
    rm "$file"
fi

mkdir images
mkdir labels
mkdir custom


cp  data/000/*.jpg images/
cp  data/100/*.jpg images/
cp  data/200/*.jpg images/
cp  data/300/*.jpg images/
cp  data/400/*.jpg images/
cp  data/500/*.jpg images/
cp  data/600/*.jpg images/
cp  data/700/*.jpg images/
cp  data/800/*.jpg images/
cp  data/900/*.jpg images/




cp  data/000/yolo/*.txt labels/
cp  data/100/yolo/*.txt labels/
cp  data/200/yolo/*.txt labels/
cp  data/300/yolo/*.txt labels/
cp  data/400/yolo/*.txt labels/
cp  data/500/yolo/*.txt labels/
cp  data/600/yolo/*.txt labels/
cp  data/700/yolo/*.txt labels/
cp  data/800/yolo/*.txt labels/
cp  data/900/yolo/*.txt labels/

cp data/classes.names ./



mv classes.names custom/
mv labels custom/
mv images custom/

python checkImages.py 




if [ $? == 0 ]; then
echo "Comprimiendo"
zip -r custom.zip custom
else
echo "Hay errores corregir"
fi

#

