# Bảng chi phí · Nhiệm vụ A và B

Nguồn: hai CSV của lab, tính bằng [lab13.py](../../src/lab13.py). Mọi kết quả dùng thời gian xem lại hoặc làm lại đều là **simulated**; chi phí chưa gồm cố định trừ A4.

## A1 · Ba phép thử

| Phép thử p = 0,8 | Kết quả |
| --- | ---: |
| Tối đa 2 lần | 1,20 |
| Chạy đến khi đúng | 1,25 |
| Hệ số chi phí, tối đa 3 lần | 1,25 |

## A2 · Chi phí từ trace

| Khoản | Giá trị | Nguồn / nhãn |
| --- | ---: | --- |
| Token | 245.585 đ | Mọi lần chạy |
| Tool | 84.000 đ | Mọi lần chạy |
| Trong đó lần 2 và 3 | 93.804 đ | Token và tool |
| Xem lại | 1.780.000 đ | 890 phút simulated |
| Làm lại | 2.264.000 đ | 1.132 phút simulated |
| Tổng | 4.373.585 đ | simulated |
| Việc thành công | 978 | 1.200 yêu cầu |
| Chi phí mỗi việc thành công | 4.472 đ | simulated |
| Hoá đơn token và tool / yêu cầu | 274,7 đ | 329.585 / 1.200 |

Chi phí mỗi việc thành công gấp 16,3 lần hoá đơn/yêu cầu; làm lại chiếm 51,8% tổng chi phí simulated. Tử số tính cả lần lỗi, mẫu số chỉ tính việc thành công.

So sánh cả hệ thống: (4.373.585 + 222 × 12.000) / 1.200 = 5.865 đ/yêu cầu, bằng 0,49 lần nhân viên tự làm (simulated).

## A3 · Theo loại

| Loại | Yêu cầu | Thành công | Lần chạy/yêu cầu | Chi phí/việc simulated | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: | ---: |
| noi_dia | 824 | 95,0% | 1,11 | 2.696 đ | 0,22 lần |
| hang_nang | 158 | 74,1% | 1,47 | 8.221 đ | 0,69 lần |
| quoc_te | 150 | 27,3% | 2,32 | 22.515 đ | 1,88 lần |
| doi_tac | 68 | 54,4% | 1,88 | 10.215 đ | 0,85 lần |

Quốc tế không đáng xử lý trong pilot: 22.515 đ/việc simulated; tỷ lệ ok theo lần 1–3 là 30,0%, 11,4%, 2,2% theo tài liệu đối chiếu, nên chạy lại kém hiệu quả.

## A4 · Chi phí cố định, phạm vi nội địa + hàng nặng

Giả định 45.000 yêu cầu/tháng là tổng lưu lượng với cơ cấu giống mẫu; 900/1.200 yêu cầu là việc thành công trong phạm vi. Chi phí biến đổi 3.072.513 / 900 = 3.414 đ/việc simulated.

| Tổng lượng/tháng | Việc thành công trong phạm vi | Cố định/việc | Cộng cố định simulated | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: |
| 45.000 | 33.750 | 1.185 đ | 4.599 đ | 0,38 lần |
| 22.500 | 16.875 | 2.370 đ | 5.784 đ | 0,48 lần |

Cả hai mức vẫn dưới 12.000 đ/việc simulated, nhưng phải tính riêng chi phí nhân viên xử lý ca không thành công khi so sánh toàn hệ thống.

## B1 · Độ nhạy

Cơ sở: 4.472 đ/việc simulated. Mỗi dòng thay một yếu tố; các chi phí dưới đây đều simulated.

| Kịch bản | Chi phí/việc | Thay đổi |
| --- | ---: | ---: |
| Giá token gấp đôi | 4.723 đ | +5,6% |
| Giá token một nửa | 4.346 đ | −2,8% |
| Xem lại gấp đôi | 6.292 đ | +40,7% |
| Xem lại một nửa | 3.562 đ | −20,3% |
| Làm lại gấp đôi | 6.787 đ | +51,8% |
| Làm lại một nửa | 3.315 đ | −25,9% |
| Lương tăng 25% | 5.506 đ | +23,1% |
| Tối đa 2 lần | 4.237 đ | −5,2% |
| Tối đa 1 lần | 4.111 đ | −8,1% |

## B2 · Kết hợp và xếp hạng

Token và xem lại cùng gấp đôi: 6.543 đ/việc, tăng 46,3% simulated. Ba tác động lớn nhất trong các kịch bản tăng: làm lại (+51,8%), xem lại (+40,7%), lương (+23,1%).

## B3 · Chi phí toàn hệ thống

Chi phí hệ thống = chi phí trợ lý + 12.000 đ × số yêu cầu không thành công; các chi phí là simulated.

| Tối đa | Trợ lý | Không thành công | Toàn hệ thống | Chi phí/việc thành công |
| --- | ---: | ---: | ---: | ---: |
| 1 lần | 3.621.781 đ | 319 | 7.449.781 đ | 4.111 đ |
| 2 lần | 4.093.220 đ | 234 | 6.901.220 đ | 4.237 đ |
| 3 lần | 4.373.585 đ | 222 | 7.037.585 đ | 4.472 đ |

Hai lần rẻ nhất cho toàn hệ thống; một lần có chi phí/việc thành công thấp nhất nhưng để thêm 85 ca cho nhân viên so với hai lần.

## B4 · Xem lại 100%

Trong 982 yêu cầu thuộc phạm vi, 948 có ít nhất một lần ok, 48 làm lại và 900 thành công. Giả định 5 phút xem lại và 9 phút làm lại: (224.513 + 948 × 5 × 2.000 + 48 × 9 × 2.000) / 900 = 11.743 đ/việc, bằng 0,98 lần 12.000 đ simulated.

Nếu làm lại 15,3 phút/ca simulated, chi phí là 12.415 đ/việc, bằng 1,03 lần 12.000 đ simulated. Pilot cần xác định mức giảm xem lại an toàn và thời gian xem lại thực tế.

