import io
import os

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

#find the labels given an image name (example.jpg)
def find_labels(name)

    # Instantiates a client
    client = vision.ImageAnnotatorClient()

    # The name of the image file to annotate
    file_name = os.path.join(
        os.path.dirname(__file__),name)

    # Loads the image into memory
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    # Performs label detection on the image file
    response = client.label_detection(image=image)
    labels = response.label_annotations

    #print all the labels
    #TODO set image labels
    print('Labels:')
    for label in labels:
        print(label.description)
