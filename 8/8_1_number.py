#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
from keras.models import model_from_json
from keras.preprocessing import image


img_path = "7py.png"
img = image.load_img(img_path, target_size=(28, 28),grayscale=True)

x = image.img_to_array(img)

# Инвертируем и нормализуем изображение
x = 255 - x
x /= 255
x = np.expand_dims(x, axis=0)

# Loading model
json_file = open('mnist_conv.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights("mnist_conv.h5")
print("Loaded model from disk")
 
# evaluate loaded model on test data
loaded_model.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['accuracy'])

# Нейронная сеть предсказывает класс изображения
prediction = loaded_model.predict(x)
print(prediction)
# Преобразуем ответ из категориального представления в метку класса
prediction = np.argmax(prediction, axis=1)
# Печатаем результат
print('Result', prediction)
