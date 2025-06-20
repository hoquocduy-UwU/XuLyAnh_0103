# Báo cáo Lab Xử Lý Ảnh - LAB 3
## PHẦN THỰC HÀNH TRÊN LỚP
### Câu 1
#### Lý thuyết:
- Ảnh được lưu dưới dạng ma trận, có thể là xám (2D) hoặc màu (3D).
- Có thể cắt vùng ảnh bằng cách chọn hàng và cột theo tọa độ.
- Thường dùng để trích vùng cần xử lý, ví dụ khuôn mặt, trái cây,...
#### Đã làm:
- Dùng slicing cắt vùng nhỏ từ ảnh gốc.
- Hiển thị và lưu vùng ảnh vừa cắt.
#### Mục tiêu:
- Biết cắt ảnh theo chỉ số hàng và cột.
- Hiểu cách thao tác ảnh như ma trận.
### Câu 2
#### Lý thuyết:
- Tịnh tiến ảnh là di chuyển ảnh sang trái, phải, lên, xuống.
- Sau khi dịch ảnh có thể xuất hiện vùng trống màu đen.
#### Đã làm:
- Dùng thư viện dịch ảnh xuống và qua phải.
- Hiển thị ảnh sau khi dịch.
#### Mục tiêu:
- Làm quen với dịch ảnh.
- Biết ảnh sau khi tịnh tiến có thể bị mất dữ liệu.
### Câu 3
#### Lý thuyết:
- Zoom là phóng to hoặc thu nhỏ ảnh.
- Khi thay đổi kích thước cần dùng nội suy để làm mượt.
#### Đã làm:
- Thử phóng to và thu nhỏ ảnh bằng nhiều tỉ lệ khác nhau.
- Zoom toàn bộ ảnh và zoom theo từng chiều riêng biệt.
#### Mục tiêu:
- Hiểu kỹ thuật zoom ảnh.
- So sánh kết quả khi dùng các tỉ lệ khác nhau.
### Câu 4
#### Lý thuyết:
- Xoay ảnh quanh tâm một góc nhất định.
- Có thể chọn giữ nguyên kích thước cũ hoặc mở rộng khung ảnh.
#### Đã làm:
- Xoay ảnh với góc 20 độ hai cách: có reshape và không reshape.
- So sánh ảnh bị cắt và ảnh được mở rộng.
#### Mục tiêu:
- Biết xoay ảnh bằng thư viện.
- Nhận biết sự khác nhau khi reshape.
### Câu 5
#### Lý thuyết:
- Ảnh nhị phân chỉ có 0 và 1 (đen trắng).
- Dilation giúp vùng trắng được mở rộng.
#### Đã làm:
- Chuyển ảnh màu thành xám rồi thành nhị phân.
- Áp dụng phép giãn với 1 và 3 lần lặp.
#### Mục tiêu:
- Hiểu cách tạo ảnh nhị phân.
- Quan sát sự thay đổi vùng sáng sau khi giãn.
### Câu 6
#### Lý thuyết:
- Biến dạng ngẫu nhiên là làm méo ảnh nhẹ bằng cách thay đổi vị trí pixel ngẫu nhiên trong phạm vi nhỏ.
#### Đã làm:
- Tạo ma trận dịch ngẫu nhiên và áp dụng lên ảnh.
- Xem kết quả ảnh bị nhiễu nhẹ.
#### Mục tiêu:
- Làm quen với kỹ thuật biến dạng ảnh.
- Thấy được ảnh bị méo khi đổi tọa độ.
### Câu 7
#### Lý thuyết:
- Có thể tự định nghĩa hàm biến đổi ảnh bằng công thức.
- Hàm cos giúp tạo ra hiệu ứng sóng.
#### Đã làm:
- Tạo hàm biến đổi ảnh bằng công thức cos.
- Áp dụng lên ảnh xám và hiển thị kết quả.
#### Mục tiêu:
- Thực hành tạo hiệu ứng biến dạng bằng hàm tự viết.
- Hiểu ảnh có thể bị làm cong theo quy luật.
## PHẦN BÀI TẬP
### Câu 1
- Cắt vùng ảnh có quả kiwi.
- Dịch quả kiwi sang phải 30 pixel.
- Lưu ảnh kết quả.
### Câu 2
- Cắt vùng ảnh có đu đủ và dưa hấu.
- Chuyển đu đủ sang HSV, dưa hấu sang ảnh xám.
- Lưu hai ảnh kết quả.
### Câu 3
- Cắt vùng có núi và thuyền trong ảnh vịnh Hạ Long.
- Xoay mỗi vùng 45 độ.
- Lưu lại hai ảnh đã xoay.
### Câu 4
- Cắt ảnh ngôi chùa từ ảnh gốc.
- Phóng to ảnh gấp 5 lần theo cả chiều ngang và dọc.
- Dùng nội suy bậc 3 để giữ chất lượng.
- Lưu ảnh sau khi phóng.
> Các bài thực hành sử dụng Python với thư viện OpenCV, scipy, imageio và matplotlib.
