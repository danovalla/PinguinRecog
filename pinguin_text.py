# Daniel Valla - Sept 2019
# Armo exporto el texto con la fecha y hora de las fotos

import glob
from PIL import Image
import pytesseract
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
import time
start_time = time.time()

# Path a las fotos
path = '/home/dani/python/Pinguins_figs/IDLE_PPA_CAM 2_A/' # use your path
all_files_path = sorted(glob.glob(path + "/*.JPG"))

# Me quedo con el nombre del archivo unicamente
all_files = []
nk = 2000
NumbSeq=len(all_files_path[0:nk])
for i in range(0,NumbSeq):
  all_files.append(os.path.basename(all_files_path[i]))

# Importo las fotos y leo el texto

dateandtime = []
temp = []
for filename in all_files_path[0:nk]:

    image = Image.open(filename) # Open image
    datetime_image = image.crop([0, 0, 800, 50]) #(left, upper, right, lower) # Crop date/time
    metadata = pytesseract.image_to_string(datetime_image, config='--psm 11') # OCR
    dateandtime.append(metadata)

    temp_image = image.crop([1850, 0, 2100, 50])  # (left, upper, right, lower) # Crop date/time
    temp.append(pytesseract.image_to_string(temp_image, config='--psm 11'))

df = pd.DataFrame(np.array([all_files[0:nk],dateandtime,temp]).transpose(),columns = ['Filename','Timeanddates','Temp'])

df['Timeanddates'] = df['Timeanddates'].str.replace('\n|_|,|“|‘|—','') # Clean up
df.to_csv('./dateandtime.csv', index=False)

print("--- %s seconds ---" % (time.time() - start_time))

#plt.imshow(datetime_image)
#plt.show()