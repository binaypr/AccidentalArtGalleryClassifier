import tensorflow as tf
from tensorflow.keras.preprocessing import image
import requests
import numpy as np
import PIL.Image as Image


#Gets the image from a link:
model = tf.keras.models.load_model("savedModel")
model.summary()

def getPrediction(url):
    
    # img = image.load_img("me_1.jpg", target_size=(512,512))
    # imgArr = image.img_to_array(img)
    # imgArr = np.expand_dims(imgArr, axis=0)

    OrigImg = Image.open(requests.get(url, stream=True).raw)
    OrigImg =  OrigImg.resize((512, 512), Image.NEAREST)

    imgArr = np.asarray(OrigImg)
    imgArr = np.expand_dims(imgArr, axis=0)

    predictions = model.predict(np.array(imgArr))
    print("Predictions:", predictions)
    classes = np.argmax(predictions, axis = 1)
    print("Classes:", classes)


getPrediction("https://d1lfxha3ugu3d4.cloudfront.net/images/opencollection/objects/size4/76.79_bt_PS4.jpg")
