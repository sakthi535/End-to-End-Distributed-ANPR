import os
from Single_input import Pipeline
import cv2

if __name__ == "__main__":

    replicas = 10
    p = Pipeline()
    # p.addCrop(0.75, 0.95)
    p.addNoise(["gauss", "sp"])
    p.addJitter(["b", "c", "s"])
    p.addFilter(["gaussian", "blur", "median"])
    #the inputs suggest the base directory of all the frames or in our case we get the frames one by one from the training dataset and od the process
    #remove the # from the pipeline() in process.py and then use crop here
    for fname in os.listdir("./OCR_cropped_test/"):
        name, extension = fname.split(".")
        im = cv2.imread(os.path.join("./OCR_cropped_test/", fname))
        for i in range(replicas):
            res = p.processOne(im)
            cv2.imwrite(os.path.join("./OCR_data/test/", f"{name}_{i}.{extension}"), res)
