# 2023 Dual Input Model Design   
## 2023-STUAX-Model[https://drive.google.com/file/d/1z2QobGFmejh8aftgSOK3opS68mwZGAny/view?usp=sharing]

This repository contains the implementation of a dual input convolutional neural network (CNN) designed in 2023. The model is structured to handle two separate inputs and merge their information for the final prediction. Below, you will find the details of the model architecture and instructions on how to use it.

## Model Architecture

The model is defined using the `create_dual_input_model` function, which accepts two input shapes and constructs a CNN for each input. These two CNNs are then merged and further processed through fully connected layers.

### Model Function

```python
def create_dual_input_model(input_shape1, input_shape2, learningrate=0.001, name=None, Debug=False):
    if name == None:
        name = 'Default'
    if Debug: print(f'Creating EL Dual Input AI, learningrate:[{learningrate}]')

    # First input
    input1 = Input(shape=input_shape1)
    x1 = Conv2D(16, (3, 3), activation='relu')(input1)
    x1 = MaxPooling2D((2, 2))(x1)
    x1 = Conv2D(32, (3, 3), activation='relu')(x1)
    x1 = MaxPooling2D((2, 2))(x1)
    x1 = Conv2D(64, (3, 3), activation='relu')(x1)
    x1 = Flatten()(x1)

    # Second input
    input2 = Input(shape=input_shape2)
    x2 = Conv2D(16, (3, 3), activation='relu')(input2)
    x2 = MaxPooling2D((2, 2))(x2)
    x2 = Conv2D(32, (3, 3), activation='relu')(x2)
    x2 = MaxPooling2D((2, 2))(x2)
    x2 = Conv2D(64, (3, 3), activation='relu')(x2)
    x2 = Flatten()(x2)

    # Merge both inputs
    merged = concatenate([x1, x2])

    # Fully connected layers
    x = Dense(128, activation='relu')(merged)
    x = Dense(64, activation='relu')(x)

    outputs = Dense(60, activation='sigmoid')(x)

    model = Model(inputs=[input1, input2], outputs=outputs, name=name)

    optimizer = Adam(learning_rate=learningrate)
    model.compile(optimizer=optimizer, loss='binary_crossentropy',
                  metrics=['accuracy', metrics.Precision(), metrics.Recall()])

    # debug summary
    if Debug: model.summary()
    return model
```
### Explanation
-*Inputs: The model accepts two inputs with specified shapes (input_shape1 and input_shape2).
-*Convolutional Layers: Each input is processed through a series of convolutional and max pooling layers.
-*Merging: The outputs from both inputs are flattened and merged.
-*Fully Connected Layers: The merged output is passed through two fully connected layers.
-*Output: The final layer outputs 60 values with a sigmoid activation function.


### Model Compilation
The model is compiled with the custom loss, and metrics for accuracy, precision, and recall.

### How to Use

## Requirements
-*TensorFlow
-*Keras

### Current and Future Value
## NOW:

Current Value: The model demonstrates significant potential and capability.

## Future:

Future Value: With further improvements and optimizations, this model could achieve higher accuracy and performance. 

Continued development could lead to substantial applications and potential revenue.

## Sigma Validity:

In scientific research, sigma (σ) is used to determine the validity and significance of an effect. 

This model, in its current state, shows promising results, 

but continuous refinement and testing are necessary to reach higher sigma levels of confidence.
