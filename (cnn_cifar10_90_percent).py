# -*- coding: utf-8 -*-
"""(CNN CIFAR10 90%).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xWSTXzKl9LIkLFS_QgRF11tIrnTuhkeC
"""

!pip install tensorflow
!pip install keras
!pip install h5py
!pip install Matplotlib
!pip install numpy

import tensorflow as tf
import numpy as np
from tensorflow import keras
from keras.models import Sequential
from tensorflow.keras import datasets, layers, models
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D, BatchNormalization
import matplotlib.pyplot as plt
from keras.constraints import max_norm
from keras import regularizers, optimizers

(train_images, train_labels), (test_images, test_labels) = datasets.cifar10.load_data()

# Normalize pixel values to be between 0 and 1
train_images, test_images = train_images / 255.0, test_images / 255.0

class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer','dog', 'frog', 'horse', 'ship', 'truck']


plt.figure(figsize=(10,10))
for i in range(25):
    plt.subplot(5,5,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(train_images[i])
    # The CIFAR labels happen to be arrays, 
    # which is why you need the extra index
    plt.xlabel(class_names[train_labels[i][0]])
plt.show()

data_augmentation = keras.Sequential(
  [
    layers.RandomFlip("horizontal",
                      input_shape=(32,
                                  32,
                                  3)),
    layers.RandomRotation(0.1),
    layers.RandomZoom(0.1),
  ]
)

model = Sequential()
model.add(data_augmentation)
model.add(Conv2D(32, kernel_size=3, activation='relu', padding='same',input_shape=(32,32,3)))
model.add(BatchNormalization())
model.add(Conv2D(32, kernel_size=3, activation='relu', padding='same'))
model.add(BatchNormalization())
model.add(MaxPooling2D())
model.add(Dropout(0.1))

model.add(Conv2D(64, kernel_size=3, activation='relu', padding='same'))
model.add(BatchNormalization())
model.add(Conv2D(64, kernel_size=3, activation='relu', padding='same'))
model.add(BatchNormalization())
model.add(MaxPooling2D())
model.add(Dropout(0.2))

model.add(Conv2D(128, kernel_size=3, activation='relu', padding='same'))
model.add(BatchNormalization())
model.add(Conv2D(128, kernel_size=3, activation='relu', padding='same'))
model.add(BatchNormalization())
model.add(MaxPooling2D())
model.add(Dropout(0.3))

model.add(Conv2D(256, kernel_size=3, activation='relu', padding='same'))
model.add(BatchNormalization())
model.add(Conv2D(256, kernel_size=3, activation='relu', padding='same'))
model.add(BatchNormalization())
model.add(MaxPooling2D())
model.add(Dropout(0.4))

model.add(Conv2D(512, kernel_size=3, activation='relu', padding='same'))
model.add(BatchNormalization())
model.add(MaxPooling2D())
model.add(Dropout(0.5))

model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(BatchNormalization())
model.add(Dense(64, activation='relu'))
model.add(BatchNormalization())
model.add(Dense(32, activation='relu'))
model.add(BatchNormalization())
model.add(Dense(10))

model.summary()

model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

history = model.fit(train_images, train_labels, epochs=200, validation_data=(test_images, test_labels))

plt.plot(history.history['accuracy'], label='accuracy')
plt.plot(history.history['val_accuracy'], label = 'val_accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.ylim([0.5, 1])
plt.legend(loc='lower right')

test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)
print(test_acc)

## url= 'ADD A LINK BELOW"

#(Dog)
#(1)"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSfx__RoRYzLDgXDiJxYGxLihJC4zoqV3V0xg&usqp=CAU"
#(2)"https://chico.ca.us/sites/main/files/imagecache/lightbox/main-images/dog_license.jpg"
#(3)"https://res.cloudinary.com/dk-find-out/image/upload/q_80,w_1920,f_auto/580540_mjznrj.jpg"
#(4)"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTGWQT5tUV3pkyiai1EnGcgrqRvVzxg7xtBHg&usqp=CAU"
#(5)"https://www.forbes.com/advisor/wp-content/uploads/2021/03/pit-bull-featured.jpg"
#(Bird)
#(1)"https://i.guim.co.uk/img/media/af868a0884d1ac671de03b081ddcc1a5619d0efe/0_183_4256_2553/master/4256.jpg?width=1200&height=1200&quality=85&auto=format&fit=crop&s=6e7919995b4ae61ddc4f3305f2f0c536"
#(2)"https://upload.wikimedia.org/wikipedia/commons/thumb/4/45/Eopsaltria_australis_-_Mogo_Campground.jpg/1200px-Eopsaltria_australis_-_Mogo_Campground.jpg"
#(3)"https://www.allaboutbirds.org/news/wp-content/uploads/2009/04/WKingbird-James.jpg"
#(4)"https://cdn.the-scientist.com/assets/articleNo/66820/aImg/34883/bird-article-m.png"
#(5)"https://www.pestworld.org/media/560900/istock_000027713740_large.jpg?preset=pestFeature360"
#(Cat)
#(1)"https://i.natgeofe.com/n/3861de2a-04e6-45fd-aec8-02e7809f9d4e/02-cat-training-NationalGeographic_1484324_square.jpg"
#(2)"https://www.humanesociety.org/sites/default/files/styles/1240x698/public/2018/06/cat-217679.jpg?h=c4ed616d&itok=3qHaqQ56"
#(3)"https://ichef.bbci.co.uk/news/976/cpsprodpb/12A9B/production/_111434467_gettyimages-1143489763.jpg"
#(4)"https://jngnposwzs-flywheel.netdna-ssl.com/wp-content/uploads/2019/05/Transparent-OrangeWhiteCat-764x1024.png"
#(5)"https://myfox8.com/wp-content/uploads/sites/17/2021/09/GettyImages-1286723413.jpg?strip=1"
#(HORSE)
#(1)"https://upload.wikimedia.org/wikipedia/commons/0/03/American_quarter_horse.jpg"
#(2)"https://upload.wikimedia.org/wikipedia/commons/thumb/d/d1/Holsteiner_Apfelschimmel-2005.jpg/1200px-Holsteiner_Apfelschimmel-2005.jpg"
#(3)"https://www.treehugger.com/thmb/SShPLoEHvhEViNtPvs82-QcCPrQ=/2121x1193/smart/filters:no_upscale()/horse.primary-e9a47e1c486c4fb7bf729e05b59cf0df.jpg"
#(4)"https://upload.wikimedia.org/wikipedia/commons/d/de/Nokota_Horses_cropped.jpg"
#(5)"http://www.uwyo.edu/4-h/_images/projects/project-horses.jpg"
#(AUTOMOBILE)
#(1)"https://sniteartmuseum.nd.edu/assets/166204/original/ferrari.jpg"
#(2)"https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/2019-honda-civic-sedan-1558453497.jpg?crop=1xw:0.9997727789138833xh;center,top&resize=480:*"
#(3)"https://www.cnet.com/a/img/CSTqzAl5wJ57HHyASLD-a0vS2O0=/940x528/2021/04/05/9e065d90-51f2-46c5-bd3a-416fd4983c1a/elantra-1080p.jpg"
#(4)"https://cdn.motor1.com/images/mgl/mrz1e/s1/coolest-cars-feature.jpg"
#(5)"https://imagescdn.dealercarsearch.com/DealerImages/ImageLibrary/1920x800/92bc146b.jpg"
#(FROG)
#(1)"https://static.toiimg.com/thumb/msid-81319557,width-1200,height-900,resizemode-4/.jpg"
#(2)"https://res.cloudinary.com/dk-find-out/image/upload/q_80,w_960,f_auto/DCTM_Penguin_UK_DK_AL202555_liuy4y.jpg"
#(3)"https://static01.nyt.com/images/2019/04/02/science/28SCI-ZIMMER1/28SCI-ZIMMER1-superJumbo.jpg"
#(4)"https://www.news10.com/wp-content/uploads/sites/64/2021/06/Litoria_mira_Photo_S_Richards-1-1.jpg"
#(5)"https://www.amphibians.org/wp-content/uploads/2019/04/0_World-Frog-Day.jpg"
#(DEER)
#(1)"https://tpwd.texas.gov/huntwild/wild/game_management/deer/images/WTD-Headshot.jpg"
#(2)"https://s.hdnux.com/photos/01/16/51/72/20618894/3/1200x0.jpg"
#(3)"https://www.nydailynews.com/resizer/AM_159WFtQ6GabSkCpYjAaLBaBQ=/1200x0/top/cloudfront-us-east-1.images.arcpublishing.com/tronc/YWZOHUYWJRE37O4Y6Y6LO374GQ.jpg"
#(4)"https://cbsnews2.cbsistatic.com/hub/i/r/2019/10/24/0dd50cc6-a4ff-4e28-85b9-e93a3713c67b/thumbnail/1200x630g6/e95e604fa814b12146d25156460bd75b/gettyimages-1056491224.jpg"
#(5)"https://images.immediate.co.uk/production/volatile/sites/23/2019/05/GettyImages-521134948-41103fd.jpg?quality=90&resize=620%2C413"
#(SHIP)
#(1)"https://www.marineinsight.com/wp-content/uploads/2019/08/Cruise-ships-1.png"
#(2)"https://img.cruisecritic.net/img-cc-r/features/2017/09/wind-spirit.jpg?w=800"
#(3)"https://www.nps.gov/common/uploads/cropped_image/primary/E2D45333-CFE3-69EF-36B109EE41BEC208.jpg?width=1600&quality=90&mode=crop"
#(4)"https://www.om.org/img/mw55955_42-62.jpg"
#(5)"https://media-cldnry.s-nbcnews.com/image/upload/newscms/2019_40/3038331/191004-roald-amundsen-al-1316.jpg"
#(AIRPLANE)
#(1)"https://fox8.com/wp-content/uploads/sites/12/2021/06/DeltaPlaneGettyImages-1170328686-e1623504953879.jpg"
#(2)"https://m.media-amazon.com/images/I/51X6Sy72lLS._AC_SL1000_.jpg"
#(3)"https://www.cnet.com/a/img/7hWKUBYkt3M0qaiMQ4kHl4YLMic=/940x0/2021/06/30/8711c745-dd77-4a35-9a12-454d5861f69b/x-59-lockheed-martin.jpg"
#(4)"https://upload.wikimedia.org/wikipedia/commons/thumb/c/cb/Ryanair.arp.750pix.jpg/220px-Ryanair.arp.750pix.jpg"
#(5)"https://assets-us-01.kc-usercontent.com/0542d611-b6d8-4320-a4f4-35ac5cbf43a6/2c7b3737-5e68-4324-b388-0c9fae8e1174/airplane-insurance-facebook.jpg"
#(TRUCK)
#(1)"https://cdn.motor1.com/images/mgl/3KVzA/s1/fastest-trucks-lead.jpg"
#(2)"https://www.forbes.com/wheels/wp-content/uploads/2021/01/2020_Chevrolet_Silverado_Midnight_Featured.jpg"
#(3)"https://www.internationaltrucks.com/-/media/Project/International-Trucks/International-Trucks/USA/Models/eMV-Series/truck_card_eMV_Box_Truck_400x260.jpg?h=260&iar=0&w=400&hash=5DDB550C30F0EA71C2BE040F70D12F0B"
#(4)"https://m.media-amazon.com/images/I/61E49Wl-7iL._AC_SX425_.jpg"
#(5)"https://i5.walmartimages.com/asr/58ec4320-5e35-42b3-8cfe-6981432191cb.f5694b515fb8ca5c914f5e34381c02ed.jpeg"

path = tf.keras.utils.get_file(origin=url)

img = tf.keras.utils.load_img(
    path, color_mode='rgb',target_size=(32, 32), 
)
img_array = tf.keras.utils.img_to_array(img)
img_array = tf.expand_dims(img_array,0) # Create a batch

predictions = model.predict(img_array/255)
score = tf.nn.softmax(predictions[0])

print(
    "This image most likely belongs to {} with a {:.2f} percent confidence."
    .format(class_names[np.argmax(score)], 100 * np.max(score))
)