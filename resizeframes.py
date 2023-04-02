import os
from tqdm import tqdm
import cv2

paths = os.listdir("basicsr/data/gt")

for img_path in tqdm(paths):
    img = cv2.imread("basicsr/data/gt/" + img_path)
    img = cv2.resize(img, (384, 384))
    cv2.imwrite("basicsr/data/hq/" + img_path, img)