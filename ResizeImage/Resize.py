#/usr/bin/env python

import sys
import os.path
import PIL
from PIL import Image


if __name__ == "__main__":

    if len(sys.argv) != 3:
        print "usage: Resize.py <base_path> <width_of_resized_image>"
        sys.exit(1)

    BASE_PATH=sys.argv[1]
    width=sys.argv[2]
    SEPARATOR=";"
    DST_FOLDER="Resized_Images/"
    count=0
    label = 0
    for dirname, dirnames, filenames in os.walk(BASE_PATH):
        for subdirname in dirnames:
            subject_path = os.path.join(dirname, subdirname)
            for filename in os.listdir(subject_path):
                abs_path = "%s/%s" % (subject_path, filename)
                print "%s%s%d" % (abs_path, SEPARATOR, label)
		#<-----------------START RESIZING-------------------------------->		
		baseheight = int(width)
		img = Image.open(abs_path)
		hpercent = (baseheight / float(img.size[1]))
		wsize = int((float(img.size[0]) * float(hpercent)))
		img = img.resize((wsize, baseheight), PIL.Image.ANTIALIAS)
		img.save("%sresized_image%d.jpg" % (DST_FOLDER, count))
		count=count+1
		#<------------------END------------------------------------------>
            label = label + 1
