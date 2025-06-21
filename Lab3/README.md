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
#### Lý thuyết:
- Tịnh tiến ảnh là thao tác dời toàn bộ nội dung ảnh theo hướng ngang hoặc dọc.
- Hiệu ứng sóng có thể tạo bằng cách dịch ngang từng dòng ảnh theo hàm sin, làm cho ảnh bị "uốn cong" tự nhiên.
#### Đã làm:
- Đọc ảnh quả kiwi và chuyển sang mảng số.
- Tịnh tiến ảnh sang phải 50 pixel, xuống dưới 30 pixel bằng cách ghi lại pixel vào mảng mới.
- Áp dụng hiệu ứng sóng bằng công thức `shift = 20 * sin(y / 20)` để dịch ngang từng dòng.
- Lưu ảnh kết quả sau biến đổi vào file `kiwi_wave.jpg`.
#### Mục tiêu:
- Biết cách tịnh tiến ảnh theo tọa độ hàng và cột.
- Làm quen với biến đổi tọa độ tạo hiệu ứng hình học.
- Hiểu cách sử dụng hàm `sin` để làm ảnh bị biến dạng theo quy luật.
### Câu 2
#### Lý thuyết:
- Có thể thao tác từng pixel để đổi màu ảnh theo quy luật tùy chọn.
- Gradient màu là kỹ thuật đổi màu dần dần theo một chiều (trên xuống hoặc trái sang phải).
- Ảnh RGBA cho phép xử lý cả màu và độ trong suốt (alpha).
#### Đã làm:
- Đọc ảnh đu đủ và dưa hấu, chuyển sang RGBA để xử lý cả phần trong suốt.
- Với đu đủ: tô màu từ đỏ (trên) đến xanh lá (dưới) theo tỉ lệ dòng ảnh.
- Với dưa hấu: tô từ vàng (trên) sang tím (dưới) bằng cách kết hợp các kênh R, G, B.
- Ghép hai ảnh đã đổi màu lại trên nền trong suốt.
- Lưu kết quả thành ảnh PNG (`ket_qua.png`).
#### Mục tiêu:
- Biết cách đổi màu ảnh theo chiều bằng công thức đơn giản.
- Làm quen với ảnh RGBA và xử lý kênh alpha.
- Thực hành tạo gradient màu tự định nghĩa.
### Câu 3
#### Lý thuyết:
- Xoay ảnh là phép biến đổi hình học làm thay đổi góc nhìn của ảnh.
- Khi xoay ảnh có thể chọn giữ nguyên kích thước ban đầu (`expand=False`) hoặc mở rộng khung.
- Phản chiếu dọc là lật ảnh theo chiều ngang, tức là lật trên xuống dưới.
#### Đã làm:
- Đọc ảnh núi và thuyền từ file.
- Xoay mỗi ảnh 45 độ mà không mở rộng khung ảnh.
- Áp dụng phản chiếu dọc (flip dọc) cho cả hai ảnh sau khi xoay.
- Ghép ảnh núi và thuyền lại cạnh nhau trên một canvas trắng.
- Lưu ảnh kết quả thành file `mountain_boat_mirror.jpg`.
#### Mục tiêu:
- Làm quen với phép xoay ảnh và kiểm soát kích thước sau xoay.
- Biết cách phản chiếu dọc một ảnh.
- Thực hành ghép nhiều đối tượng vào một ảnh tổng hợp.
### Câu 4
#### Lý thuyết:
- Phóng to ảnh là thao tác thay đổi kích thước ảnh theo hệ số nhất định.
- Khi phóng to nhiều, ảnh có thể bị vỡ nếu không dùng nội suy phù hợp.
- Biến dạng hình học như "uốn cong" ảnh có thể thực hiện bằng cách thay đổi vị trí pixel theo công thức toán học.
#### Đã làm:
- Đọc ảnh ngôi chùa và phóng to ảnh lên gấp 5 lần theo cả chiều ngang và dọc.
- Chuyển ảnh thành mảng để thao tác từng dòng.
- Áp dụng công thức sin để dịch ngang mỗi dòng, tạo hiệu ứng "uốn cong" tự nhiên.
- Ghi ảnh kết quả ra file `pagoda_warped.jpg`.
#### Mục tiêu:
- Biết cách phóng to ảnh bằng phép co giãn tỷ lệ.
- Thực hành biến đổi hình học bằng công thức thủ công.
- Hiểu cách làm ảnh biến dạng bằng cách thay đổi tọa độ pixel.
