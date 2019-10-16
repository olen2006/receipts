import os
import glob
import json
import shutil

try:
    os.mkdir('./processed')
#OSError is for baward compatibility
except OSError:
    print("'processed' directory already exists")

#looking for all files in a folder

subtotal = 0.0

#processing receipts

for path in glob.iglob('./new/receipt-[0-9]*.json'):
    with open(path) as f:
        content = json.load(f) #we load content from each receipt into json file as a list with values
        subtotal += float(content['value']) #counting value subtotal from all receipts
        destination = path.replace('new', 'processed')
    #moving file into processed folder using shutil library
    shutil.move(path, destination)
    print(f"moved '{path}' to '{destination}'")

print(f"Receipt subtotal: ${round(subtotal, 2)}")#string interpolation 12:45 !Lecture: shutil & glob!

