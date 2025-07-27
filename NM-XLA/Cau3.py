import cv2
import numpy as np
image_path = 'colorful-ripe-tropical-fruits.jpg'
image = cv2.imread(image_path)
if image is not None:
    h, w = image.shape[:2]
    resized_image = cv2.resize(image, (w + 30, h + 30))
    cv2.imshow('Resized Image', resized_image)
    cv2.waitKey(0)
image_path = 'quang-ninh.jpg'
image = cv2.imread(image_path)
if image is not None:
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    rotation_matrix = cv2.getRotationMatrix2D(center, -45, 1.0) # -45 độ cho chiều kim đồng hồ
    rotated_image = cv2.warpAffine(image, rotation_matrix, (w, h))
    flipped_image = cv2.flip(rotated_image, 1) # Lật ngang
    cv2.imshow('Rotated and Flipped Image', flipped_image)
    cv2.waitKey(0)
image_path = 'pagoda.jpg'
image = cv2.imread(image_path)
if image is not None:
    (h, w) = image.shape[:2]
    resized_image = cv2.resize(image, (w * 5, h * 5))
    blurred_image = cv2.GaussianBlur(resized_image, (7, 7), 0)
    cv2.imshow('Resized and Blurred Image', blurred_image)
    cv2.waitKey(0)
image_path = 'pagoda.jpg'
image = cv2.imread(image_path)
if image is not None:
    alpha = 1.5
    beta = 30
    new_image = np.zeros(image.shape, image.dtype)
    for y in range(image.shape[0]):
        for x in range(image.shape[1]):
            for c in range(image.shape[2]):
                new_image[y, x, c] = np.clip(alpha * image[y, x, c] + beta, 0, 255)
    cv2.imshow('Adjusted Image', new_image)
    cv2.waitKey(0)
cv2.destroyAllWindows()