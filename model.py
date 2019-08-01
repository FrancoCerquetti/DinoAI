import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Conv2D, Flatten, MaxPooling2D, Activation, Dropout
from sklearn.model_selection import train_test_split
import load_data

x, y = load_data.load_data(85, 85)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20)

model = Sequential()
model.add(Conv2D(256, (5, 5), input_shape=x.shape[1:]))
model.add(MaxPooling2D(pool_size=(4, 4)))

model.add(Conv2D(128, (4, 4)))
model.add(MaxPooling2D(pool_size=(3, 3)))

model.add(Conv2D(64, (3, 3)))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.3))

model.add(Dense(128, activation='relu'))
model.add(Dropout(0.2))

model.add(Dense(64, activation='relu'))
model.add(Dropout(0.2))

model.add(Dense(32, activation='relu'))
model.add(Dropout(0.15))

model.add(Dense(1, activation='sigmoid'))

model.compile(optimizer='adam', 
        loss='binary_crossentropy', 
        metrics=['accuracy'])

model.fit(x_train, y_train, epochs=20)

scores = model.test_on_batch(x_test, y_test)
print(scores)

model.save('./model/train.h5')
