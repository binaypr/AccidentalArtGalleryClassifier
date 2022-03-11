
import random
import shutil
import requests 
import matplotlib as plt
from PIL import Image
import io
import os
import math
import time
import os.path
import glob



def file_len(fname):
    with open(fname, "r", encoding='utf8') as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def save_image(url, titel, artist, location, year, type, identifier):
        headers = {
            'User-Agent': 'Machine Learning Art Decade Classifier--Binay Rijal--binaypr@vt.edu',
            'From': 'binaypr@vt.edu',  # This is another valid field
            'AIC-User-Agent': 'Binay Rijal--binaypr@vt.edu'
            }


        response = requests.get(url, headers=headers)
        print(response)

        image_bytes = io.BytesIO(response.content)

        img = Image.open(image_bytes)

        # direct = "images/" + str(year)

        # if(not os.path.isdir(direct)):
        #             os.mkdir(direct)

        img.save("images/" + str(identifier) + ".jpg")






with open("dataset.csv", "r", encoding="utf8") as f:

    for i, line in enumerate(f):
        if i < 144:
            continue
        print(i, end="\t")
        splitline = line.split(",")
        print(splitline)
        type = splitline[0]
        year = splitline[1]
        titel = splitline[2]
        
        
        location = splitline[3]
        artist = splitline[5]
        identifier = splitline[6]
        if("untitled" in titel or "Untitled" in titel or "Untitled" in artist or "untitled" in artist):
            titel = identifier
        
        url = f'https://www.artic.edu/iiif/2/{identifier}/full/843,/0/default.jpg'
        print(url)

        with open("error_idents.txt", "r+") as e:
            if(identifier in e.read().splitlines()):
                print("Already in error.txt\n")
                time.sleep(5)
                continue

        if(not glob.glob(os.getcwd() + "/**/"+str(titel)+".jpg", recursive=True)):
            try:
                save_image(url, titel, artist, location, str(round(int(year)/100) * 100) , type, identifier)
            except Exception as e:
                print(e)
                open("error.txt", "a+").write(str(e) + " ||| " + url + " ||| " + identifier + " \n")
                open("error_idents.txt", "a+").write(identifier + "\n")
            finally:
                pass
            time.sleep(10)
        else:
            print("image already exists")
            open("already_exists.txt", "a+").write(titel + " ||| " + url + " ||| " + identifier + " \n")
            time.sleep(2)
        print("\n")

        



            



