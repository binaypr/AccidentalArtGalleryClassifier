import requests
import json
import time
import os

from PIL import Image, ImageOps

def get200():
    array = []
    try:
        base_url = 'https://www.reddit.com/r/AccidentalArtGallery/top/.json?limit=100&t=all'
        request = requests.get(base_url, headers = {'User-agent': 'Mgaodd\'s Potential Classifier'})
        array = parseURL(request.json())

        time.sleep(5)

        base_url = 'https://www.reddit.com/r/AccidentalArtGallery/top/.json?limit=100&t=all&after=t3_el23h4'
        request = requests.get(base_url, headers = {'User-agent': 'Mgaodd\'s Potential Classifier'})
        array_200 = array + parseURL(request.json())

        base_url = 'https://www.reddit.com/r/AccidentalArtGallery/top/.json?limit=100&t=all&after=t3_g434oz'
        request = requests.get(base_url, headers = {'User-agent': 'Mgaodd\'s Potential Classifier'})
        
        array_200 = array + parseURL(request.json())


        return array_200

    except:
        print(array_200)
        print(array)
        print(request.json())
        print('An Error Occured')
    
    
def parseURL(data):
    array = []
    distSize = data['data']['dist']

    for x in range(distSize):
        flair = data['data']['children'][x]['data']['link_flair_text']
        if flair == "Help Classify":
            continue
        url = data['data']['children'][x]['data']['url']
        if "external" in url:
            continue;
        author = data['data']['children'][x]['data']['created']
        temp = CustomImage(url, flair, author)
        array.append(temp)
    return array

def getSaved():
    file = open("data200.txt")
    data = json.load(file)
    return data




class CustomImage:
    def __init__(self, url, tag, author):
        self.url = url;
        self.tag = tag.replace(" ", "_");
        self.author = author        
        # print(self.url, self.tag, self.author)

    def __str__(self):
        jason = json.dumps(self.__dict__)
        return jason
    def __repr__(self):
        jason = json.dumps(self.__dict__)
        return jason
    
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)
    
    def properDirectory(self):
        path = os.getcwd() + "\\data"
        try: 
            os.mkdir(path) 
        except Exception as e:
            if "already exists" not in repr(e):
                print(repr(e))
        
        path = path + "\\" + self.tag        
        
        try: 
            os.mkdir(path) 
        except Exception as e:
            if "already exists" not in repr(e):
                print(repr(e))
                
        
    def dataAugment(self, OrigImg):

        num= 1
        img = ImageOps.grayscale(OrigImg)
        img.save("data/" + self.tag + "/" + self.author + "_" + str(num) +".jpg")

        num+= 1
        img = ImageOps.equalize(OrigImg, mask=None)
        img.save("data/" + self.tag + "/" + self.author + "_" + str(num) +".jpg")
        
        num+= 1
        img = ImageOps.scale(OrigImg, .5)
        img.save("data/" + self.tag + "/" + self.author + "_" + str(num) +".jpg")

        # Versions of the flipped image
        num += 1
        FlipImg = ImageOps.mirror(OrigImg)
        FlipImg.save("data/" + self.tag + "/" + self.author + "_" + str(num) +".jpg")

        num+= 1
        img = ImageOps.grayscale(FlipImg)
        img.save("data/" + self.tag + "/" + self.author + "_" + str(num) +".jpg")

        num+= 1
        img = ImageOps.equalize(FlipImg, mask=None)
        img.save("data/" + self.tag + "/" + self.author + "_" + str(num) +".jpg")
        
        num+= 1
        img = ImageOps.scale(FlipImg, .5)
        img.save("data/" + self.tag + "/" + self.author + "_" + str(num) +".jpg")
    
    def saveImage(self):
        self.properDirectory()

        # Versions of the original image
        num = 1;
        try:
            OrigImg = Image.open(requests.get(self.url, stream=True).raw)
            OrigImg =  OrigImg.resize((512, 512), Image.NEAREST)
            OrigImg.save("data/" + self.tag + "/" + self.author + "_" + str(num) +".jpg")
            print(self.author, "has been saved in: ", self.tag)
        except Exception as e:
            print(self, "Error: ", repr(e))

def writeImageArrayToFile(data):
    print(len(data))
    with open('data200.txt', 'w') as f:
        f.write("{")
        for x in range(len(data)):
            string = "\"" + str(x) + "\":"
            string = string +  data[x].toJSON()
            if (x != len(data) - 1):
                string= string + ",\n"
            f.write(string)
        print(data[x])
        f.write("}")






# savedData[8].saveImage()

data = get200();
writeImageArrayToFile(data);


data = getSaved()

print(len(data))
imageArray = []
print(data)
for x in data:
    print(data[x]['url'], data[x]['tag'], data[x]['author'])
    imageArray = imageArray + [CustomImage(data[x]['url'], data[x]['tag'], data[x]['author'])]



print(imageArray)

#Testing Image Array Saver
for x in range(10):
    imageArray[x].saveImage();
    time.sleep(20);


# for x in imageArray:
#      x.saveImage()
#      time.sleep(20)



# for x in data:
#     with open("urlTag.txt", "w") as file:
#         print(json.dump(x, file))

        












