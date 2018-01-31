#!/usr/bin/env python2
import io
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "home/pi/Desktop/Abbot/Abbot.json"


# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

#find the labels given an image name (example.jpg)
def find_labels(name):

    # Instantiates a client
    client = vision.ImageAnnotatorClient()

    # The name of the image file to annotate
    file_name = os.path.join('/home/pi/Desktop/Abbot/resources/',name)

    # Loads the image into memory
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    # Performs label detection on the image file
    response = client.label_detection(image=image)
    labels = response.label_annotations
   
    list = []
    for label in labels:
        list.append("".join(map(str,label.description)))
    return list
    
        
def detect_web(name):
    
    # Instantiates a client
    client = vision.ImageAnnotatorClient()
    
    # The name of the image file to annotate
    file_name = os.path.join('/home/pi/Desktop/Abbot/resources/',name)

    # Loads the image into memory
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)
    
    # Performs web detection on the image file
    response = client.web_detection(image=image)
    notes = response.web_detection
        
    list = []
    for image in notes.full_matching_images :
        list.append("".join(str(image)))
    for image in notes.partial_matching_images :
        list.append("".join(str(image)))
    return list


    

          
