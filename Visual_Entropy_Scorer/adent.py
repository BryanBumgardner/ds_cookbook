# -*- coding: utf-8 -*-
"""



http://scikit-image.org/docs/dev/user_guide

http://www.astro.cornell.edu/research/projects/compression/entropy.html

"""

from skimage.filter.rank import entropy
from skimage.morphology import disk
import numpy as np
import skimage
import os

#Declare here where you want the script to write the csv results
outputfile=open("C

#Provide the directory where all the .jpgs are
filepath="C:
shots=os.listdir(filepath)

#Loop to calculate the average entropy for each image in the directory, and write the "Name","Score" to each row of a csv.
#c is just a counter to print % progess. you can def delete it if you want.
c=0
for shot in shots:
    c+=1
    # deifning 16-bit images
    a16 = skimage.io.imread(filepath+shot,flatten=True).astype(np.uint16)*100
    ent16 = entropy(a16,disk(5))
    ent=np.average(ent16)
    outputfile.write(str(ent)+','+shot+'\n')
    print((float(c)/len(shots)*100))


