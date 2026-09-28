# ĐÁNH GIÁ VÀ NHẬN XÉT VỀ CÔNG CỤ AI (AI CRITIQUE)

- **MSSV:** 23120073
- **Họ và tên:** Nguyễn Nam Phước
- **Học phần:** Kiểm thử Phần mềm (Software Testing)
- **Bài tập:** Kiểm thử ứng dụng Basic Calculator (`https://testsheepnz.github.io/BasicCalculator.html`)
- **Module kiểm thử:** Divide (Phép chia)

---

Trong quá trình thực hiện bài tập, AI mắc một số lỗi đáng chú ý. Cụ thể, khi viết script `div.py`, AI giả định rằng giá trị của tùy chọn "Divide" trong dropdown là chuỗi `"Divide"` thay vì số `"3"`, đồng thời nhầm tên nút Clear từ `resetButton` thành `clearButton`. Ngoài ra, lần chạy đầu tiên cho build 1 hoàn toàn thất bại với 18/18 ERROR do những sai sót này, khiến toàn bộ vòng kiểm thử phải lặp lại. Nguyên nhân sâu xa là AI thiên về suy luận từ ngữ nghĩa thay vì kiểm chứng thực tế — nó đọc mã nguồn HTML nhưng không chủ động chạy một bước khám phá DOM nhanh trước khi viết code. Đây là biểu hiện của thiên kiến "happy path thinking": AI mặc định rằng tên phần tử khớp với nhãn hiển thị, bỏ qua khả năng trang triển khai khác với cách đặt tên thông thường. Thêm vào đó, AI không phân biệt được lỗi thực sự của ứng dụng với hành vi thiết kế — ví dụ, kết quả PASS duy nhất của Build 8 ở TC-DIV-010 là "trùng hợp đúng" do bug hoán vị toán hạng tình cờ cho ra đáp án đúng với trường hợp `0/0`, nhưng AI vẫn báo cáo là PASS mà không có chú thích. Từ những trải nghiệm này, bài học quan trọng nhất là: không nên để AI tự suy luận về môi trường thực thi — cần yêu cầu AI xác minh DOM thực tế trước khi sinh code, đặt ra tiêu chí phân loại lỗi rõ ràng từ đầu, và luôn đọc ít nhất một mẫu đại diện từ kết quả tự động trước khi kết luận.
