
# **Nhập Môn Xử Lý Ảnh Số – Lab 4**  
## **Phân Ngưỡng Ảnh & Biến Đổi Hình Thái (Morphological Operations)**  

## **Giới thiệu**  
Bài lab này giúp sinh viên nắm vững các kỹ thuật phân ngưỡng ảnh và các phép biến đổi hình thái học cơ bản trong xử lý ảnh nhị phân. Các thao tác này đóng vai trò quan trọng trong:  

- Tách vật thể ra khỏi nền  
- Làm sạch ảnh nhị phân (giảm nhiễu, lấp lỗ, nối vùng)  
- Phục vụ tiền xử lý cho các bài toán nhận dạng, phân vùng, phát hiện biên...

---

## **Công nghệ sử dụng**
- **Python**: Ngôn ngữ chính
- **Pillow (PIL)**: Đọc/hiển thị ảnh
- **NumPy**: Xử lý ảnh dưới dạng mảng
- **OpenCV**: Phân ngưỡng và xử lý ảnh
- **SciPy.ndimage**: Các phép toán morphology
- **scikit-image**: Các hàm ngưỡng hóa cao cấp
- **Matplotlib**: Hiển thị ảnh trực quan

---

## **Chi tiết bài tập**

### **2.1. Phân ngưỡng ảnh**

#### **2.1.1. Phương pháp Otsu**  
**Mục đích:**  
- Tự động tìm ngưỡng tách ảnh nhị phân dựa trên histogram.

**Code chính:**  
```python
from skimage.filters.thresholding import threshold_otsu
data = Image.open('fruit.jpg').convert('L')
a = np.asarray(data)
thres = threshold_otsu(a)
b = a > thres
b = Image.fromarray(b)
plt.imshow(b)
plt.show()
```

**Giải thích:**  
Otsu tối ưu hóa độ lệch trong/ngoài lớp để phân vùng ảnh xám thành ảnh nhị phân.

---

#### **2.1.2. Adaptive Thresholding (Ngưỡng cục bộ)**  
**Mục đích:**  
- Phân ngưỡng theo từng vùng nhỏ của ảnh – thích hợp ảnh có ánh sáng không đồng đều.

**Code chính:**  
```python
from skimage.filters import threshold_local
data = Image.open('fruit.jpg').convert('L')
a = np.asarray(data)
b = threshold_local(a, 39, offset=10)
b = Image.fromarray(b)
plt.imshow(b)
plt.show()
```

**Giải thích:**  
Ngưỡng hóa dựa trên giá trị lân cận (block size 39), offset giúp tăng độ nhạy.

---

### **2.2. Phân vùng theo vùng ảnh (Watershed + Distance Transform)**  
**Mục đích:**  
- Tách các vật thể liền kề bằng kỹ thuật distance transform và watershed.

**Code chính:**  
```python
from scipy.ndimage import label
data = cv2.imread('fruit.jpg')
a = cv2.cvtColor(data, cv2.COLOR_BGR2GRAY)
thresh, b1 = cv2.threshold(a, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
b2 = cv2.erode(b1, None, iterations = 2)
dist_trans = cv2.distanceTransform(b2, 2, 3)
thresh, dt = cv2.threshold(dist_trans, 1, 255, cv2.THRESH_BINARY)
labelled, ncc = label(dt)
labelled = labelled.astype(np.int32)
cv2.watershed(data, labelled)
b = Image.fromarray(labelled)
plt.imshow(b)
plt.show()
```

**Giải thích:**  
Watershed coi ảnh như địa hình; dựa trên vùng seed từ distance transform để phân chia vùng sát nhau.

---

### **2.3. Biến đổi hình thái ảnh nhị phân (Morphological Ops)**  

#### **2.3.1. Dilation (Giãn ảnh)**  
**Mục đích:**  
- Làm to vật thể, nối các lỗ nhỏ và chi tiết đứt rời.

**Code chính:**  
```python
b = nd.binary_dilation(data, iterations=50)
```

**Kết quả:**  
Sau 50 lần giãn, vật thể lan rộng ra, bít các khoảng trống nhỏ.

---

#### **2.3.2. Opening (Erosion + Dilation)**  
**Mục đích:**  
- Loại bỏ nhiễu nhỏ, giữ lại vật thể lớn.

**Structuring Element:**  
```python
s = [[0, 1, 0], [1, 1, 1], [0, 1, 0]]
```

**Code chính:**  
```python
b = nd.binary_opening(data, structure=s, iterations=25)
```

**Kết quả:**  
Lọc nhiễu, thu nhỏ nhẹ vật thể, giữ được hình dạng chính.

---

#### **2.3.3. Closing (Dilation + Erosion)**  
**Mục đích:**  
- Lấp kín các lỗ nhỏ bên trong vật thể.

**Structuring Element:**  
```python
s = [[0, 1, 0], [1, 1, 1], [0, 1, 0]]
```

**Code chính:**  
```python
b = nd.binary_closing(data, structure=s, iterations=50)
```

**Kết quả:**  
Đường viền vật thể được làm kín, loại bỏ khe nứt hẹp.

---

## **Cấu trúc file**
```
├── main.ipynb             # Notebook chính
├── fruit.jpg              # Ảnh dùng để phân ngưỡng
├── dil_img.gif            # Ảnh dùng để test morphology
├── README.md              # File mô tả này
```
## BÀI TẬP VỀ NHÀ
---
## Bài 1 - LangBiang (Otsu Thresholding)
- Ảnh đầu vào: `dalat.jpg`.
- Cắt vùng (0:400, 0:600), dịch ảnh sang phải 100px.
- Áp dụng ngưỡng Otsu, nhân thêm hệ số 0.3 để tăng độ nhạy.
- Lưu ảnh dưới tên `lang_biang.jpg`.

## Bài 2 - Hồ Xuân Hương (Adaptive Thresholding)
- Cắt ROI (400:800, 200:700), xoay 45 độ.
- Áp dụng `threshold_local` với block size = 35, offset = 60.
- Lưu kết quả thành `ho_xuan_huong.jpg`.

## Bài 3 - Quảng Trường Lâm Viên (Morphology Closing)
- Cắt vùng (x=500, y=50, w=300, h=300).
- Dịch vùng chọn sang phải 100px.
- Áp dụng phép `binary_closing` 5 lần.
- Gắn vùng đã xử lý trở lại ảnh gốc.
- Lưu ảnh dưới tên `quan_truong_lam_vien.jpg`.

## Bài 4 – Menu tương tác

- Ảnh đầu vào: dalat.jpg
- Cho phép người dùng chọn một trong các phép biến đổi hình học và phân ngưỡng:
- Geometric Transformations
    - a. Rotate (xoay 45 độ quanh tâm)
    - b. Scale (phóng to 1.5 lần)
    - c. Shift (dịch phải 100px, xuống 50px)
- Segmentation Methods
    - a. Adaptive Thresholding (block size = 39, offset = 10)
    - b. Binary Dilation (iterations = 5)
    - c. Binary Erosion (iterations = 5)
    - d. Otsu Thresholding
- Cho phép thực hiện một hoặc cả hai lựa chọn biến đổi và phân ngưỡng
- Hiển thị kết quả bằng matplotlib

## **Hướng dẫn chạy**
### 1. Cài đặt thư viện  
```bash
pip install pillow numpy matplotlib imageio opencv-python scikit-image
```

### 2. Chạy notebook  
- Dùng VSCode, Jupyter Notebook hoặc Google Colab.  
- Đảm bảo file ảnh đặt đúng thư mục với notebook.  
- Chạy từng cell để xem kết quả.

### 3. Tùy chỉnh thông số  
- Thay đổi số vòng lặp (`iterations`), structuring element, hoặc `offset` để quan sát hiệu ứng khác nhau.

---

## **Tài liệu tham khảo**
- **Digital Image Processing** – Rafael C. Gonzalez  
- **Scikit-Image** Documentation  
- **OpenCV Python Docs**  
