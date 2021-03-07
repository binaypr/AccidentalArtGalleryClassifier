import tensorflow as tf
from tensorflow.keras import datasets, layers, models
import matplotlib.pyplot as plt
from keras.preprocessing.image import ImageDataGenerator



image_size =(512,512)
batch_size = 4
directory = "data"



# Creates the different training and validation datasets from a single directory
image_generator = ImageDataGenerator(rescale=1/255, validation_split=0.5)    

train_dataset = image_generator.flow_from_directory(batch_size=batch_size,
                                                 directory=directory,
                                                 shuffle=True,
                                                 target_size=image_size, 
                                                 subset="training",
                                                 class_mode='categorical')

validation_dataset = image_generator.flow_from_directory(batch_size=batch_size,
                                                 directory=directory,
                                                 shuffle=True,
                                                 target_size=image_size, 
                                                 subset="validation",
                                                 class_mode='categorical')


model = models.Sequential()
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))


model.add(layers.Flatten())
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(10))

model.summary()

model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

history = model.fit(train_dataset, epochs=2, validation_data=validation_dataset)



plt.plot(history.history['accuracy'], label='accuracy')
plt.plot(history.history['val_accuracy'], label = 'val_accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.ylim([0.5, 1])
plt.legend(loc='lower right')

test_loss, test_acc = model.evaluate(train_dataset, verbose=2)

plt.savefig("modelgraph.jpg")

print(test_acc)




