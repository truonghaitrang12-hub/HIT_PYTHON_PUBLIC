Câu 1:
-Python là ngôn ngữ thông dịch (Interpreted Language).
+Python thực thi chương trình từng dòng lệnh, không cần biên dịch toàn bộ mã nguồn thành tệp thực thi trước như C hoặc C++.
+Khi chạy chương trình, mã nguồn Python được chuyển thành bytecode (.pyc), sau đó máy ảo Python (Python Virtual Machine - PVM) sẽ thông dịch và thực thi bytecode.
+Nhờ vậy, Python dễ viết, dễ kiểm tra lỗi và có thể chạy trên nhiều hệ điều hành mà không cần biên dịch lại.
Câu 2:
1. Các kiểu dữ liệu cơ bảnSố nguyên (int):
 Các số không có phần thập phân ví dụ: (5, -10).
 Số thực (float): Các số có chứa dấu chấm thập phân (ví dụ: (3.14, -0.001)).
 Chuỗi (str): Văn bản được đặt trong dấu ngoặc kép hoặc đơn (ví dụ: "Python").
 Cấu trúc dữ liệu: Bao gồm List (có thể thay đổi), Tuple (không thể thay đổi), Set (tập hợp không trùng lặp) và Dictionary (lưu trữ theo cặp khóa-giá trị).
 2. Các toán tử trong PythonToán tử số học: 
 -Tính toán giá trị như cộng (+), trừ (-), nhân (*), chia (/) và chia lấy dư (%).
 -Toán tử gán: Dùng để gán giá trị cho biến (như = , +=, -=).
 -Toán tử so sánh: Trả về kết quả luận lý, kiểm tra bằng nhau (==), khác nhau (!=), lớn hơn (>), hoặc nhỏ hơn (<).-Toán tử logic: Kết hợp các điều kiện với and(,)or, hoặc phủ định với not.
 3. Mệnh đề điều kiện và vòng lặp
 -Mệnh đề điều kiện: Dùng if, elif, và else để rẽ nhánh luồng chương trình dựa trên biểu thức đúng/sai.
 +Vòng lặp:Vòng lặp for: Lặp qua một tập hợp (như danh sách hoặc chuỗi).
 +Vòng lặp while: Tiếp tục lặp đi lặp lại khối lệnh khi điều kiện vẫn còn đúng.
 4. Kiểu dữ liệu True, False (Boolean)
 -Trong Python, True (Đúng) và False (Sai) là các giá trị thuộc kiểu dữ liệu (bool).Chúng thường là kết quả của các phép so sánh (ví dụ: (5 > 3) sẽ trả về (True)) hoặc dùng để kiểm tra trạng thái.
 -Python còn xem xét một số giá trị (như số (0), chuỗi rỗng "", hoặc danh sách rỗng []) tương đương với (False), và các giá trị khác tương đương với (True).