import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Conv2D, Flatten, MaxPooling2D, Activation, Dropout
import load_data

x, y = load_data.load_data(85, 85)

model = Sequential()
model.add(Conv2D(128, (5, 5), input_shape=x.shape[1:]))
model.add(MaxPooling2D(pool_size=(4, 4)))

model.add(Conv2D(64, (4, 4)))
model.add(MaxPooling2D(pool_size=(3, 3)))

model.add(Conv2D(32, (3, 3)))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.4))

model.add(Dense(64, activation='relu'))
model.add(Dropout(0.3))

model.add(Dense(32, activation='relu'))
model.add(Dropout(0.2))

model.add(Dense(1, activation='sigmoid'))

model.compile(optimizer='adam', 
        loss='binary_crossentropy', 
        metrics=['accuracy'])

model.fit(x, y, epochs=15)