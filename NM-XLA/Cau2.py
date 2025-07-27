import cv2
import numpy as np
import random
import sys


def inverse(img):
    return 255 - img
def gamma_correction(img):
    gamma = random.uniform(0.5, 2.0)
    inv_gamma = 1.0 / gamma
    table = np.array([((i / 255.0) ** inv_gamma) * 255 for i in np.arange(256)]).astype("uint8")
    return cv2.LUT(img, table)
def log_transform(img):
    c = random.uniform(1.0, 5.0)
    img_float = img.astype(np.float32) + 1.0
    log_img = c * np.log(img_float)
    log_img = np.clip(log_img, 0, 255).astype(np.uint8)
    return log_img

def histogram_equalization(img):
    if len(img.shape) == 2:
        return cv2.equalizeHist(img)
    else:
        img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
        img_yuv[:, :, 0] = cv2.equalizeHist(img_yuv[:, :, 0])
        return cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)

def contrast_stretching(img):
    min_val = random.randint(0, 100)
    max_val = random.randint(150, 255)
    img = np.clip(img, min_val, max_val)
    stretched = ((img - min_val) / (max_val - min_val)) * 255
    return np.clip(stretched, 0, 255).astype(np.uint8)

def adaptive_histogram_equalization(img):
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    if len(img.shape) == 2:
        return clahe.apply(img)
    else:
        lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
        lab[:, :, 0] = clahe.apply(lab[:, :, 0])
        return cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)
img_names = ['image1.jpg', 'image2.jpg', 'image3.jpg']
images = []
for name in img_names:
    img = cv2.imread(name)
    if img is None:
        print(f"Không thể đọc ảnh: {name}")
        sys.exit(1)
    images.append(img)
menu = """
🔧 Ấn phím để chọn phương pháp biến đổi:
 I - Image Inverse
 G - Gamma Correction
 L - Log Transformation
 H - Histogram Equalization
 C - Contrast Stretching
 A - Adaptive Histogram Equalization
 Q - Thoát chương trình
"""
print(menu)
while True:
    key = input("Nhập lựa chọn (I/G/L/H/C/A hoặc Q để thoát): ").strip().lower()

    if key == 'q':
        print("Thoát chương trình.")
        break

    operation = None
    if key == 'i':
        operation = ("inverse", inverse)
    elif key == 'g':
        operation = ("gamma", gamma_correction)
    elif key == 'l':
        operation = ("log", log_transform)
    elif key == 'h':
        operation = ("hist", histogram_equalization)
    elif key == 'c':
        operation = ("contrast", contrast_stretching)
    elif key == 'a':
        operation = ("adaptive", adaptive_histogram_equalization)

    if operation is not None:
        op_name, op_func = operation
        for i, img in enumerate(images):
            result = op_func(img)
            filename = f"output_{op_name}_{i+1}.jpg"
            cv2.imwrite(filename, result)
            print(f"Đã lưu: {filename}")
    else:
        print("Lựa chọn không hợp lệ! Vui lòng thử lại.")

