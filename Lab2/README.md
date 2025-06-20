# THỰC HÀNH LAB 2
## PHẦN 1 – CÁC PHÉP BIẾN ĐỔI CƠ BẢN
## 1.1. Image Inversion
- **Lý thuyết:**  
  Biến đổi âm bản đảo ngược toàn bộ giá trị pixel. Công thức: `output = 255 - input`.  
  Ứng dụng tạo hiệu ứng ảnh âm, làm rõ vùng sáng tối.
- **Đã làm:**  
  Dùng `np.asarray()` để chuyển ảnh sang mảng. Áp dụng phép trừ 255, sau đó dùng `Image.fromarray()` để chuyển lại thành ảnh.
- **Mục tiêu:**  
  Hiểu nguyên lý đảo màu và thao tác cơ bản với mảng ảnh.
## 1.2. Gamma Correction
- **Lý thuyết:**  
  Điều chỉnh độ sáng phi tuyến theo công thức: `output = 255 × (input/255)^γ`.  
  Với `γ < 1`: làm sáng ảnh, `γ > 1`: làm tối ảnh.
- **Đã làm:**  
  Chuẩn hóa giá trị pixel về [0,1], áp dụng `np.power()`, rồi nhân lại 255 và hiển thị.
- **Mục tiêu:**  
  Làm quen hiệu ứng tăng/giảm độ sáng phi tuyến, thấy rõ ảnh hưởng của tham số gamma.
## 1.3. Logarithmic Transformation
- **Lý thuyết:**  
  Dùng log để nén dải cường độ: `output = c × log(1 + input)`, với `c = 255 / log(1 + max_input)`.  
  Làm rõ vùng tối, nén các giá trị cao.
- **Đã làm:**  
  Tính hệ số `c`, sau đó áp dụng `np.log1p()` cho ảnh rồi co dãn về [0,255].
- **Mục tiêu:**  
  Hiểu ứng dụng của log trong xử lý ảnh tối/sáng không đều.
## 1.4. Histogram Equalization
- **Lý thuyết:**  
  Cân bằng histogram giúp phân bố đều độ sáng bằng cách tính CDF và ánh xạ lại pixel.
- **Đã làm:**  
  Tính histogram → CDF → chuẩn hóa → gán giá trị mới cho ảnh.
- **Mục tiêu:**  
  Biết cách cải thiện độ tương phản tự động.
## 1.5. Contrast Stretching
- **Lý thuyết:**  
  Kéo giãn cường độ theo công thức: `output = 255 × (input − min) / (max − min)`.  
  Dùng để mở rộng dải cường độ từ min/max về 0–255.
- **Đã làm:**  
  Tìm giá trị `min` và `max`, rồi áp dụng công thức tuyến tính cho toàn bộ ảnh.
- **Mục tiêu:**  
  Nắm được cách làm rõ ảnh bằng co giãn độ sáng.
## PHẦN 2 – BIẾN ĐỔI MIỀN TẦN SỐ
## 1.6.1. FFT – Phân tích ảnh
- **Lý thuyết:**  
  Dùng FFT để phân tích tần số trong ảnh.  
  Phép biến đổi Fourier 2D cho biết phổ tần số – vùng sáng là tần số thấp.
- **Đã làm:**  
  Dùng `fft2()`, dịch tâm phổ bằng `fftshift()`, hiển thị bằng `np.log1p(np.abs())`.
- **Mục tiêu:**  
  Làm quen với phổ ảnh, hiểu vùng tần số thấp/cao trong ảnh.
## 1.6.2. Bộ lọc Butterworth
- **Lý thuyết:**  
  Dùng công thức bộ lọc:  
  - Lowpass: làm mờ → giữ tần số thấp.  
  - Highpass: làm sắc nét → giữ tần số cao.
- **Đã làm:**  
  Tạo bộ lọc dạng vòng tròn theo khoảng cách đến tâm, nhân phổ FFT với bộ lọc → IFFT để tái tạo ảnh.
- **Mục tiêu:**  
  Biết cách tạo bộ lọc tần số và áp dụng làm mờ/làm nét ảnh.
## PHẦN BÀI TẬP TỔNG HỢP
## B1 – Tổ hợp các phép biến đổi điểm ảnh
- **Lý thuyết:**  
  Biến đổi điểm ảnh như: Inverse, Gamma, Log, Histogram Equalization, Contrast Stretching.
- **Đã làm:**  
  Áp dụng từng phép biến đổi lên ảnh đầu vào, so sánh kết quả trực quan. Sử dụng kết hợp Pillow + NumPy.
- **Mục tiêu:**  
  Hiểu rõ từng loại biến đổi, phân biệt tác động của từng phép lên ảnh.
## B2 – Biến đổi ảnh trong miền tần số
- **Lý thuyết:**  
  Dùng FFT để chuyển ảnh sang miền tần số, kết hợp với bộ lọc Butterworth (lowpass/highpass).
- **Đã làm:**  
  Tính FFT ảnh, áp dụng bộ lọc Butterworth bằng công thức khoảng cách, IFFT để tái tạo ảnh kết quả.
- **Mục tiêu:**  
  Thành thạo lọc tần số, hiểu khái niệm “lọc biên” và “làm mờ” trong miền tần số.
## B3 – Biến đổi ngẫu nhiên
- **Lý thuyết:**  
  - Hoán đổi kênh màu RGB.  
  - Chọn ngẫu nhiên 1 trong 5 phép biến đổi điểm ảnh.
- **Đã làm:**  
  Dùng `random.sample()` để hoán vị RGB. Dùng `random.choice()` chọn phép biến đổi áp dụng cho mỗi lần chạy.
- **Mục tiêu:**  
  Tạo sự đa dạng ảnh đầu ra, luyện cách kết hợp linh hoạt các phép biến đổi.
## B4 – Kết hợp tần số + không gian
- **Lý thuyết:**  
  Dùng lọc FFT kết hợp lọc không gian như Min/Max filter.  
  - Min Filter: làm mượt, khử nhiễu sáng.  
  - Max Filter: khử nhiễu tối.
- **Đã làm:**  
  Áp dụng bộ lọc Butterworth rồi tiếp tục dùng `minimum_filter` hoặc `maximum_filter` từ `scipy.ndimage`.
- **Mục tiêu:**  
  Biết cách phối hợp lọc miền tần số và miền không gian để tối ưu hóa xử lý ảnh.