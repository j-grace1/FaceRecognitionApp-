import imp
from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np
import random








def recognize():
    # Load the model
    model = load_model('keras_model.h5')


#load labels
    with open('labels.txt','r') as f:
        class_names = f.read().split('\n')



# Create the array of the right shape to feed into the keras model
# The 'length' or number of images you can put into the array is
# determined by the first position in the shape tuple, in this case 1.
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
# Replace this with the path to your image
    image = Image.open('./project_app/me.jpg')


    #resize the image to a 224x224 with the same strategy as in TM2:
    #resizing the image to be at least 224x224 and then cropping from the center
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.ANTIALIAS)

#turn the image into a numpy array
    image_array = np.asarray(image)
# Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
# Load the image into the array
    data[0] = normalized_image_array





# run the inference
    prediction = model.predict(data)


    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score =prediction


    
    if(int(confidence_score[0][0]) < 0.80):
        
        rand_idx = random.randint(0, 9)
        return rand_idx
    else:
        return(7)


      

x = recognize()
print(x)