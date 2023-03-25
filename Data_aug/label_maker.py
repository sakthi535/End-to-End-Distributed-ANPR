import os
import cv2


for fname in os.listdir("./inputs/train/labels"):
    name, extension = fname.split(".")
    im = open(os.path.join("./inputs/train/labels", fname), "r")
    text = im.read()
    for i in range(10):
        wr = open(os.path.join("./outputs/labels", f"{name}_{i}.{extension}"), "a")
        wr.write(text)