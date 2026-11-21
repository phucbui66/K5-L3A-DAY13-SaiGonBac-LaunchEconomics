# Báo cáo cá nhân — Bùi Hữu Phúc

## 1. Thông tin thành viên

- Họ và tên: Bùi Hữu Phúc
- MSSV: 2A202603572
- Email: chưa cung cấp
- Vai trò: phụ trách phần 1 — nhiệm vụ A–B; người gắn nhãn độc lập thứ nhất trong nhiệm vụ C.

## 2. Phần việc phụ trách

Phần 1 gồm xây dựng mô hình chi phí mỗi việc thành công, phân tích theo loại yêu cầu, tính chi phí cố định và lập bảng độ nhạy. Tôi cũng cần tự gắn nhãn 20 ca lỗi trước khi so kết quả với thành viên thứ hai.

## 3. Nội dung phần việc

- Nhiệm vụ A: tính chi phí token, công cụ, xem lại và làm lại; chia tổng chi phí cho số yêu cầu thành công. Phân tích thêm theo từng loại yêu cầu và xét chi phí cố định.
- Nhiệm vụ B: so sánh các kịch bản giá token, thời gian nhân viên và giới hạn số lần chạy; tính thêm chi phí toàn hệ thống và kịch bản xem lại 100%.
- Phần gắn nhãn độc lập 20 ca: **chưa thực hiện**, cần hoàn thành trước khi trao đổi với thành viên thứ hai.

## 4. Bằng chứng và kết quả

- [Mã tính toán](../../src/lab13.py) chạy thành công; ba phép thử A1 cho kết quả 1,20; 1,25; 1,25.
- [Bảng chi phí](bang_chi_phi.md) ghi tổng chi phí 4.373.585 đồng và 978 việc thành công, tương ứng khoảng **4.472 đồng/việc simulated**.
- Khi giới hạn tối đa 2 lần chạy, chi phí toàn hệ thống là **6.901.220 đồng simulated**, thấp hơn hai kịch bản 1 và 3 lần trong bảng B3.
- Tử số bao gồm chi phí của mọi lần chạy, kể cả lần lỗi; mẫu số chỉ đếm việc thành công. Các số dùng phút xem lại hoặc làm lại giả lập được ghi nhãn simulated.

## 5. Công cụ AI và kiểm tra

Đã dùng Codex để hỗ trợ đọc đề, viết mã và tổng hợp phần A–B. Mã đã được chạy để đối chiếu ba phép thử A1 và các kết quả trong bảng; phép chia có thể kiểm tra lại bằng tay: 4.373.585 / 978 ≈ 4.472 đồng/việc simulated.

Trước khi nộp, tôi cần tự chạy lại mã, kiểm tra các phép tính và tự giải thích cách tính, ý nghĩa mẫu số và giới hạn của dữ liệu simulated.

## 6. Tự đánh giá

Phần A–B đã có mã và bảng kết quả để kiểm tra. Tôi cần hoàn thành gắn nhãn độc lập, tự rà soát kết quả và bổ sung phần tự đánh giá sau khi thực hiện các bước này.
