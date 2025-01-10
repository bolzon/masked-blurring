from dataclasses import dataclass

import cv2
import matplotlib.pyplot as plt
import numpy as np

from PIL import Image


IMG_PATH = '2.jpg'

blur_boxes = [Box(200, 300, 400, 500)]


@dataclass
class Box:
    xmin: int
    ymin: int
    xmax: int
    ymax: int

    @property
    def width(self) -> int:
        return self.xmax - self.xmin

    @property
    def height(self) -> int:
        return self.ymax - self.ymin


def blur(image: np.ndarray, boxes: list[Box]) -> np.ndarray:
    out_image = image.copy()
    for box in boxes:
        kernel_size = tuple(int(size / 10) * 2 + 1 for size in (box.width, box.height))
        out_image[box.ymin:box.ymax, box.xmin:box.xmax] = cv2.blur(out_image[box.ymin:box.ymax, box.xmin:box.xmax], kernel_size)
    return out_image


def gaussian_blur(image: np.ndarray, boxes: list[Box]) -> np.ndarray:
    border = 20
    out_image = image.copy()
    for box in boxes:
        kernel_size = tuple(int(size / 10) * 4 + 1 for size in (box.width, box.height))
        mask = np.zeros((box.width-border, box.height-border, 3), dtype=np.uint8)
        crop = out_image[box.ymin:box.ymax, box.xmin:box.xmax]
        blurred_crop = cv2.GaussianBlur(crop, kernel_size, 0)
        out_image[box.ymin:box.ymax, box.xmin:box.xmax] = np.where(mask==(255, 255, 255), crop, blurred_crop)
    return out_image


if __name__ == '__main__':
    img_pil = Image.open(IMG_PATH)
    img = np.array(img_pil)

    plt.imshow(img)
    plt.show()

    blur_img = blur(img, blur_boxes)
    gaussian_blur_img = gaussian_blur(img, blur_boxes)

    plt.imshow(blur_img)
    plt.show()

    plt.imshow(gaussian_blur_img)
    plt.show()
