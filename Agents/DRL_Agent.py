
## Agent architecture using keras rl 


### Model
# Agents representation of the environment. ( How the agent thinks the environment works) 

#### 1. 256 , 127, 256 are the channels- depth of the first layer, one can be colour, edges)
#### 2. Kernel size is the size of the matrix it will be use to make the convolution ( impair size is better)
#### 3. strides are the jumps the model make ( Ask A)

def create_model(input, actions):
  model = Sequential()
  model.add(Convolutional2D(256, kernel_size=(5,5), input_shape=input))
  model.add(Activation('relu'))
  
  model.add(Convolution2D(127, kernel_size=(3,3))
  model.add(Activation('relu'))
  
  model.add(Convolution2D(32, kernel_size=(5,5))
  model.add(Activation('relu'))
  
  model.add(Flatten())
  model.add(Dense(actions))
  model.add(Activation('softmax')
  
  model.compile(loss="categorical_crossentropy",
  optimizer="adam",
  metrics=["accuracy"])
  
