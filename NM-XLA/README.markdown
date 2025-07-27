# Nhập Môn Xử Lý Ảnh Số - THI THỬ

## Giới thiệu
Dự án này thực hiện các bài tập của Lab 4 trong môn Nhập Môn Xử Lý Ảnh Số, tập trung vào các kỹ thuật phân ngưỡng ảnh và biến đổi hình thái học sử dụng Python và thư viện OpenCV, NumPy, và SciPy. Các tệp `cau1.py`, `cau2.py`, và `cau3.py` lần lượt giải quyết các bài tập về ngưỡng Otsu, ngưỡng cục bộ, và phép toán hình thái closing trên ảnh `dalat.jpg`. Các thao tác này nhằm tách vật thể, giảm nhiễu, và xử lý vùng ảnh cụ thể.

## Yêu cầu
- **Python**: Phiên bản 3.6 trở lên.
- **Thư viện**:
  - OpenCV (`opencv-python`): Xử lý ảnh và phân ngưỡng.
  - NumPy: Thao tác mảng dữ liệu ảnh.
  - SciPy (`scipy.ndimage`): Thực hiện phép toán hình thái học.
  - Matplotlib: Hiển thị ảnh trực quan.
  - Pillow (`PIL`): Đọc và lưu ảnh (tùy chọn).
- **Tệp ảnh**:
  - `dalat.jpg`: Ảnh đầu vào cho cả ba bài tập.
- **Môi trường chạy**: VSCode, Jupyter Notebook, hoặc Google Colab.

## Cài đặt
1. Cài đặt Python
2. Cài đặt các thư viện cần thiết:
   ```bash
   pip install opencv-python numpy scipy matplotlib pillow
   ```
3. Đặt tệp ảnh `dalat.jpg` vào cùng thư mục với các tệp Python.

## Cách sử dụng
1. Đảm bảo tệp ảnh `dalat.jpg` có sẵn trong thư mục làm việc.
2. Chạy từng tệp Python bằng lệnh:
   ```bash
   python cau1.py
   python cau2.py
   python cau3.py
   ```
3. Kết quả sẽ được lưu dưới dạng tệp ảnh (`lang_biang.jpg`, `ho_xuan_huong.jpg`, `quan_truong_lam_vien.jpg`) và hiển thị bằng Matplotlib.

## Chi tiết các tệp

### `cau1.py` (Bài 1 - LangBiang: Otsu Thresholding)
- **Chức năng**: 
  - Đọc ảnh `dalat.jpg`, cắt vùng ảnh (0:400, 0:600).
  - Dịch vùng ảnh sang phải 100 pixel.
  - Áp dụng ngưỡng Otsu với hệ số 0.3 để tăng độ nhạy.
  - Lưu kết quả thành `lang_biang.jpg` và hiển thị ảnh nhị phân.
- **Đầu vào**: Tệp ảnh `dalat.jpg`.
- **Đầu ra**: Tệp `lang_biang.jpg` và cửa sổ Matplotlib hiển thị ảnh nhị phân.
- **Lưu ý**: Hệ số 0.3 nhân vào giá trị ngưỡng Otsu để điều chỉnh độ nhạy phân ngưỡng.
- **Mã tham khảo**:
  ```python
  from skimage.filters import threshold_otsu
  import cv2
  import numpy as np
  import matplotlib.pyplot as plt

  img = cv2.imread('dalat.jpg', cv2.IMREAD_GRAYSCALE)
  roi = img[0:400, 0:600]
  shifted = np.zeros_like(roi)
  shifted[:, 100:600] = roi[:, 0:500]
  thresh = threshold_otsu(roi) * 0.3
  binary = roi > thresh
  cv2.imwrite('lang_biang.jpg', binary.astype(np.uint8) * 255)
  plt.imshow(binary, cmap='gray')
  plt.show()
  ```

### `cau2.py` (Bài 2 - Hồ Xuân Hương: Adaptive Thresholding)
- **Chức năng**: 
  - Đọc ảnh `dalat.jpg`, cắt vùng ảnh (400:800, 200:700).
  - Xoay vùng ảnh 45 độ quanh tâm.
  - Áp dụng ngưỡng cục bộ với `block_size=35` và `offset=60`.
  - Lưu kết quả thành `ho_xuan_huong.jpg` và hiển thị ảnh nhị phân.
- **Đầu vào**: Tệp ảnh `dalat.jpg`.
- **Đầu ra**: Tệp `ho_xuan_huong.jpg` và cửa sổ Matplotlib hiển thị ảnh nhị phân.
- **Lưu ý**: Ngưỡng cục bộ phù hợp cho vùng ảnh có ánh sáng không đồng đều.
- **Mã tham khảo**:
  ```python
  from skimage.filters import threshold_local
  import cv2
  import numpy as np
  import matplotlib.pyplot as plt

  img = cv2.imread('dalat.jpg', cv2.IMREAD_GRAYSCALE)
  roi = img[400:800, 200:700]
  h, w = roi.shape
  center = (w // 2, h // 2)
  M = cv2.getRotationMatrix2D(center, 45, 1.0)
  rotated = cv2.warpAffine(roi, M, (w, h))
  binary = threshold_local(rotated, block_size=35, offset=60)
  cv2.imwrite('ho_xuan_huong.jpg', binary.astype(np.uint8))
  plt.imshow(binary, cmap='gray')
  plt.show()
  ```

### `cau3.py` (Bài 3 - Quảng Trường Lâm Viên: Morphology Closing)
- **Chức năng**: 
  - Đọc ảnh `dalat.jpg`, cắt vùng ảnh (x=500, y=50, w=300, h=300).
  - Dịch vùng chọn sang phải 100 pixel.
  - Áp dụng phép `binary_closing` 5 lần với structuring element mặc định.
  - Gắn vùng đã xử lý trở lại ảnh gốc và lưu thành `quan_truong_lam_vien.jpg`.
  - Hiển thị ảnh kết quả bằng Matplotlib.
- **Đầu vào**: Tệp ảnh `dalat.jpg`.
- **Đầu ra**: Tệp `quan_truong_lam_vien.jpg` và cửa sổ Matplotlib hiển thị ảnh.
- **Lưu ý**: Phép closing giúp lấp kín các lỗ nhỏ trong vùng nhị phân.
- **Mã tham khảo**:
  ```python
  from scipy.ndimage import binary_closing
  import cv2
  import numpy as np
  import matplotlib.pyplot as plt

  img = cv2.imread('dalat.jpg', cv2.IMREAD_GRAYSCALE)
  roi = img[50:350, 500:800]
  shifted = np.zeros_like(roi)
  shifted[:, 100:300] = roi[:, 0:200]
  binary = shifted > threshold_otsu(shifted)
  closed = binary_closing(binary, iterations=5)
  img[50:350, 500:800] = closed.astype(np.uint8) * 255
  cv2.imwrite('quan_truong_lam_vien.jpg', img)
  plt.imshow(img, cmap='gray')
  plt.show()
  ```

## Lưu ý
- Đảm bảo tệp `dalat.jpg` tồn tại trong thư mục làm việc, nếu không chương trình sẽ báo lỗi.
- Kết quả ảnh nhị phân được lưu dưới dạng grayscale (giá trị 0 hoặc 255).
- Có thể điều chỉnh các tham số như `block_size`, `offset`, hoặc `iterations` để quan sát các hiệu ứng khác nhau.
- Để kiểm tra kết quả trực quan, sử dụng Matplotlib hoặc xem các tệp ảnh đầu ra.

## Tài liệu tham khảo
- Digital Image Processing – Rafael C. Gonzalez
- [Scikit-Image Documentation](https://scikit-image.org/docs/stable/)
- [OpenCV Python Documentation](https://docs.opencv.org/master/)
- [SciPy Documentation](https://docs.scipy.org/doc/scipy/reference/ndimage.html)