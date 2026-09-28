# Kết quả kiểm thử - Divide Operation

- **Build:** 3
- **Thời gian chạy:** 2026-09-28 15:48:06
- **Tổng số test case:** 18
- **PASS:** 17  |  **FAIL:** 1  |  **ERROR:** 0

---

## Bảng tổng hợp kết quả

| TC ID | Tên test case | Kết quả |
|-------|---------------|---------|
| TC-DIV-001 | Chia hai số nguyên dương chia hết | ✅ PASS |
| TC-DIV-002 | Chia cho kết quả là số thập phân | ✅ PASS |
| TC-DIV-003 | Chia số nguyên dương cho 1 | ✅ PASS |
| TC-DIV-004 | Chia số 0 cho số nguyên dương | ✅ PASS |
| TC-DIV-005 | Chia số nguyên âm cho số nguyên dương | ✅ PASS |
| TC-DIV-006 | Chia số nguyên dương cho số nguyên âm | ✅ PASS |
| TC-DIV-007 | Chia hai số nguyên âm | ✅ PASS |
| TC-DIV-008 | Chia hai số thập phân dương | ✅ PASS |
| TC-DIV-009 | Chia cho số 0 (Division by zero) | ✅ PASS |
| TC-DIV-010 | Chia số 0 cho số 0 | ✅ PASS |
| TC-DIV-011 | Phép chia với Integers only được bật | ✅ PASS |
| TC-DIV-012 | Kiểm tra thứ tự toán hạng (First/Second) | ✅ PASS |
| TC-DIV-013 | Nhập ký tự không phải số vào First number | ✅ PASS |
| TC-DIV-014 | Nhập ký tự không phải số vào Second number | ✅ PASS |
| TC-DIV-015 | Nhập ký tự đặc biệt vào trường nhập liệu | ✅ PASS |
| TC-DIV-016 | Kiểm tra giới hạn độ dài nhập tối đa 10 ký tự | ✅ PASS |
| TC-DIV-017 | Phép tính chia độc lập (không dùng lại Answer cũ) | ✅ PASS |
| TC-DIV-018 | Xóa kết quả và thiết lập lại bằng nút Clear | ❌ FAIL |

---

## Chi tiết từng test case

### TC-DIV-001 – Chia hai số nguyên dương chia hết

- **Kết quả:** ✅ PASS
- **Expected:** Answer="5", không có lỗi
- **Actual:** Answer="5", lỗi=""

### TC-DIV-002 – Chia cho kết quả là số thập phân

- **Kết quả:** ✅ PASS
- **Expected:** Answer="2.5", không có lỗi
- **Actual:** Answer="2.5", lỗi=""

### TC-DIV-003 – Chia số nguyên dương cho 1

- **Kết quả:** ✅ PASS
- **Expected:** Answer="18", không có lỗi
- **Actual:** Answer="18", lỗi=""

### TC-DIV-004 – Chia số 0 cho số nguyên dương

- **Kết quả:** ✅ PASS
- **Expected:** Answer="0", không có lỗi
- **Actual:** Answer="0", lỗi=""

### TC-DIV-005 – Chia số nguyên âm cho số nguyên dương

- **Kết quả:** ✅ PASS
- **Expected:** Answer="-5", không có lỗi
- **Actual:** Answer="-5", lỗi=""

### TC-DIV-006 – Chia số nguyên dương cho số nguyên âm

- **Kết quả:** ✅ PASS
- **Expected:** Answer="-5", không có lỗi
- **Actual:** Answer="-5", lỗi=""

### TC-DIV-007 – Chia hai số nguyên âm

- **Kết quả:** ✅ PASS
- **Expected:** Answer="6", không có lỗi
- **Actual:** Answer="6", lỗi=""

### TC-DIV-008 – Chia hai số thập phân dương

- **Kết quả:** ✅ PASS
- **Expected:** Answer="3", không có lỗi
- **Actual:** Answer="3", lỗi=""

### TC-DIV-009 – Chia cho số 0 (Division by zero)

- **Kết quả:** ✅ PASS
- **Expected:** Lỗi chứa "Divide by zero error!", không hiển thị "Infinity"
- **Actual:** Answer="", lỗi="Divide by zero error!"

### TC-DIV-010 – Chia số 0 cho số 0

- **Kết quả:** ✅ PASS
- **Expected:** Lỗi chứa "Divide by zero error!", không hiển thị "NaN"
- **Actual:** Answer="", lỗi="Divide by zero error!"

### TC-DIV-011 – Phép chia với Integers only được bật

- **Kết quả:** ✅ PASS
- **Expected:** Answer="3" (phần nguyên), không có lỗi
- **Actual:** Answer="3", lỗi=""

### TC-DIV-012 – Kiểm tra thứ tự toán hạng (First/Second)

- **Kết quả:** ✅ PASS
- **Expected:** Answer="5" (20/4, không phải 4/20=0.2)
- **Actual:** Answer="5", lỗi=""

### TC-DIV-013 – Nhập ký tự không phải số vào First number

- **Kết quả:** ✅ PASS
- **Expected:** Lỗi chứa "Number 1 is not a number"
- **Actual:** Answer="", lỗi="Number 1 is not a number"

### TC-DIV-014 – Nhập ký tự không phải số vào Second number

- **Kết quả:** ✅ PASS
- **Expected:** Lỗi chứa "Number 2 is not a number"
- **Actual:** Answer="", lỗi="Number 2 is not a number"

### TC-DIV-015 – Nhập ký tự đặc biệt vào trường nhập liệu

- **Kết quả:** ✅ PASS
- **Expected:** Lỗi chứa "Number 1 is not a number"
- **Actual:** Answer="", lỗi="Number 1 is not a number"

### TC-DIV-016 – Kiểm tra giới hạn độ dài nhập tối đa 10 ký tự

- **Kết quả:** ✅ PASS
- **Expected:** Ô nhận tối đa "1234567890" (10 ký tự), Answer="1234567890"
- **Actual:** Giá trị nhận="1234567890", Answer="1234567890", lỗi=""

### TC-DIV-017 – Phép tính chia độc lập (không dùng lại Answer cũ)

- **Kết quả:** ✅ PASS
- **Expected:** Lần 1 Answer="10", Lần 2 Answer="50" (100/2, không dùng lại 10)
- **Actual:** Lần 1 Answer="10", Lần 2 Answer="50", lỗi=""

### TC-DIV-018 – Xóa kết quả và thiết lập lại bằng nút Clear

- **Kết quả:** ❌ FAIL
- **Expected:** Sau Clear: Answer trống, lỗi trống, Integers only bỏ tick
- **Actual:** Trước Clear Answer="5"; Sau Clear: answer_empty=False, error_empty=True, checkbox_unchecked=False
