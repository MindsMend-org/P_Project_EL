#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
# PRIVATE AND CONFIDENTIAL [Intellectual Property Of Brett Palmer mince@foldingcircles.co.uk]
# [No Copying Or Reading Or Use Permitted !]
"""
Copyright (c) 2023, Brett Palmer (Mince@foldingcircles.co.uk)

All rights reserved. No permission is granted for anyone, except the software owner, Brett Palmer, to use, copy, modify,
distribute, sublicense, or otherwise deal with the software in any manner.

Any unauthorized use, copying, or distribution of this software without the explicit written consent of the software
owner is strictly prohibited.

For permission requests, please contact the software owner, Brett Palmer, at Mince@foldingcircles.co.uk.
"""
# nda.py for git test live 2024

import shutil
import re
import os
import cv2  # pip install opencv-python
import numpy as np
import json
import csv
import time
from tensorflow.keras.layers import Input, Conv2D, MaxPooling2D, Flatten, Dense, concatenate, BatchNormalization
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.utils import to_categorical
from keras.models import model_from_json
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score
from tensorflow.keras.callbacks import ModelCheckpoint, LearningRateScheduler, Callback
from keras import metrics
from tensorflow.keras import backend as K
import sys
import requests


# add scraper get any result tbc # scrape_lottery_results.py
def get_lottery_results(date_str):
    api_key = "your_api_key"  # Replace with your actual API key
    url = f"https://api.example.com/lottery/results?date={date_str}&apiKey={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None


def create_dual_input_model(input_shape1, input_shape2, learning_rate=0.001, name='Default', debug=False):
    if debug:
        print(f'Creating Dual Input Model, learning rate: {learning_rate}')

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
    optimizer = Adam(learning_rate=learning_rate)
    model.compile(optimizer=optimizer, loss='binary_crossentropy',
                  metrics=['accuracy', metrics.Precision(), metrics.Recall()])

    if debug:
        model.summary()
    return model


def load_temporal_ai(model, name, best=True):
    model_name = model.name if name is None else name
    model_file = f'models/{model_name}/model_weights.h5'

    if best and os.path.exists(f'models/{model_name}/best_model.h5'):
        model_file = f'models/{model_name}/best_model.h5'

    print(f'Loading {model_file}')
    model.load_weights(model_file)
    return model


def load_prediction_images(image_name, directory='predict/'):
    img_path = os.path.join(directory, f"{image_name}.png")
    img_input2_path = os.path.join(directory, f"{image_name}_input2.png")

    img1 = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    img1 = cv2.resize(img1, (60, 2000))
    img1 = np.expand_dims(img1, axis=-1) / 255.0

    img2 = cv2.imread(img_input2_path, cv2.IMREAD_GRAYSCALE)
    img2 = cv2.resize(img2, (60, 2000))
    img2 = np.expand_dims(img2, axis=-1) / 255.0

    return np.expand_dims(img1, axis=0), np.expand_dims(img2, axis=0)


def predict_with_threshold(model, x_input1, x_input2, threshold=0.5, predict_by_count_value=7, model_mode="NRF",
                           debug=True):
    print(f'THRESHOLD HAS BEEN SET TO: {threshold}')
    if threshold == 0.0:
        print(f'Predicting top {predict_by_count_value} values')

    y_pred = model.predict([x_input1, x_input2])

    if threshold == 0.0:
        sorted_indices = np.argsort(y_pred[0])[::-1][:predict_by_count_value]
        top_percentages = y_pred[0][sorted_indices]
        find_threshold = min(top_percentages)
        y_pred_thresholded = (y_pred >= find_threshold).astype(int)
    else:
        y_pred_thresholded = (y_pred >= threshold).astype(int)

    return y_pred_thresholded, y_pred


def predict(model, image_name='x_val', threshold=0.6, model_mode="NRF", build_interpreter=False, debug=False,
            predict_count=9):
    if debug:
        print(f'Debug Mode: {debug} Model_Mode: {model_mode} Predict Count: {predict_count}')

    x_val1, x_val2 = load_prediction_images(image_name, directory='predict/')
    y_pred_thresholded, y_pred_pcent = predict_with_threshold(model, x_val1, x_val2, threshold,
                                                              model_mode=model_mode,
                                                              predict_by_count_value=predict_count)

    if build_interpreter and debug:
        print(f'Building interpreter data...')

    return y_pred_thresholded, y_pred_pcent


def send_to_predict(model, from_path, dest_path='predict', model_mode="NRF", threshold=0.5, predict_count=9,
                    answers=[], graph=False, plot_alwayz=False, read_mode=False, build_interpreter=False,
                    display_steps=False, interpreter_force_new_file=True, debug=False, show_at_end=False,
                    nda_build_data=False):
    if debug:
        print(f'Sending To Predict.')

    y_pred_thresholded, y_pred_pcent = predict(model, 'x_val', threshold, model_mode=model_mode,
                                               predict_count=predict_count, build_interpreter=build_interpreter)

    if nda_build_data:
        print('NDA Parties Data Builder.')
        nda_dest_dir = "NDA_parties/STUAX/images"
        pattern = r"/([a-zA-Z]+)-(\d{2}-\d{2}-\d{4})/(\d{4}-\d{2}-\d{2}T\d{2}-\d{2}-\d{2})"
        match = re.search(pattern, from_path)

        if match:
            day_abbreviation, date_value, timestamp_value = match.groups()
            nda_data_for = f"{day_abbreviation}_{date_value}"
            nda_data_from = timestamp_value
            nda_stamp = f"FC_M_MADE[{nda_data_from}]_For_Target[{nda_data_for}]"
            directory_path = os.path.join(nda_dest_dir, nda_stamp)

            os.makedirs(directory_path, exist_ok=True)
            shutil.copy("predict/x_val.png", os.path.join(directory_path, "x_val.png"))
            shutil.copy("predict/x_val_input2.png", os.path.join(directory_path, "x_val_input2.png"))
            print("NDA Files copied.")

    if read_mode:
        return y_pred_thresholded, y_pred_pcent

    return y_pred_thresholded, y_pred_pcent


def print_thresholded_values(y_pred_thresholded, y_pred_pcent, answers, threshold, read_mode=False,
                             display_steps=False, addto_interpreter=False, file="", debug=False, show_at_end=False):
    reset, red, white, yellow = "\033[0m", "\033[31m", "\033[37m", "\033[93m"
    print("LABEL:")
    for sublist in y_pred_thresholded:
        for j, val in enumerate(sublist):
            color = red if j in answers else yellow
            val = 1 if j in answers else 0
            print(f"{color}{val}{reset}", end=' ')
        print()
    print(reset, end='')

    matched, predicted = [], []
    if display_steps:
        print("y_pred_thresholded:")
    for sublist in y_pred_thresholded:
        for j, val in enumerate(sublist):
            color = red if j in answers else yellow
            if val > threshold:
                predicted.append(j)
                if color == red:
                    matched.append(j)
                print(f"{color}{val}{reset}", end=' ')
            else:
                print(f"{white}{val}{reset}", end=' ')
        print()
    print(reset, end='')

    print("y_pred_pcent:", end=' ')
    for sublist in y_pred_pcent:
        for j, val in enumerate(sublist):
            if val > threshold:
                color = red if j in answers else white
                print(f"{color}{val}{reset}", end=' ')
        print()
    print(reset, end='')

    print(f'Predicted: {predicted}')
    print(f"answers: {', '.join(f'{red}{val}{reset}' for val in answers)}")
    print(f'Matched: {matched}')
    print(f"{white}{reset}")


def init_ai(name='Default', learning_rate=0.001):
    num_channels = 1
    height, width = 2000, 60
    input_shape1 = (height, width, num_channels)
    input_shape2 = (height, width, num_channels)
    model = create_dual_input_model(input_shape1, input_shape2, learning_rate, name=name)
    return model


def get_prediction_list_to_process(base_directory="images"):
    if os.path.exists(base_directory) and os.path.isdir(base_directory):
        subdirectories = [name for name in os.listdir(base_directory) if
                          os.path.isdir(os.path.join(base_directory, name))]
        print("Subdirectories in 'images':", subdirectories)
        return subdirectories
    print("The 'images' directory does not exist.")
    return []


def copy_from_to(dir_from="", dir_to="predict"):
    dir_from = os.path.join("images", dir_from)
    shutil.copy(os.path.join(dir_from, "x_val.png"), os.path.join(dir_to, "x_val.png"))
    shutil.copy(os.path.join(dir_from, "x_val_input2.png"), os.path.join(dir_to, "x_val_input2.png"))
    print("Files copied.")


def load_cleaned_results(file_path='cleaned_lottery_results.json'):
    with open(file_path, 'r') as file:
        return json.load(file)


def get_labels_for_date(date, cleaned_results):
    return cleaned_results.get(date, [])


PREDICTION_COUNT = 4
threshold = 0.0
SHOW_AT_END = False
build_interpreter = False
debug = False
DisplaySteps = False
interpreter_file_dir = ""

# Load the cleaned lottery results
lottery_results = load_cleaned_results()

model = init_ai('STUAX')
model = load_temporal_ai(model, name='STUAX', best=False)
to_process = get_prediction_list_to_process("images")

for item in to_process:
    print(f'\nDissabled&Removed[Build Holographic Binary Representation] for file: {item}')
    copy_from_to(dir_from=item)

    # Regular expression pattern to extract made and for_target
    pattern = r"FC_M_MADE\[(.*?)\]_For_Target\[(.*?)\]"

    # Search for the pattern in the example string
    match = re.search(pattern, item)

    if match:
        made = match.group(1)
        for_target = match.group(2)
        print(f"made = '{made}'")
        print(f"for_target = '{for_target}'")
    else:
        print("Pattern not found")

    # Remove brackets and format target_label
    target_label = for_target.replace('[', '').replace(']', '').replace('_', '-')
    print('-')
    print(target_label)
    print('-')

    # Fetch labels from cleaned results
    labels = []
    for date_key, numbers in lottery_results.items():
        if target_label in date_key:
            labels = numbers
            break
    flattened_labels = [item for sublist in labels for item in sublist]

    print(flattened_labels)

    y_pred_thresholded, y_pred_pcent = predict(model=model, threshold=threshold, predict_count=PREDICTION_COUNT)
    print(y_pred_thresholded, y_pred_pcent)
    print_thresholded_values(y_pred_thresholded, y_pred_pcent, flattened_labels, threshold,
                             display_steps=DisplaySteps, addto_interpreter=build_interpreter,
                             file=interpreter_file_dir, debug=debug, show_at_end=SHOW_AT_END)
