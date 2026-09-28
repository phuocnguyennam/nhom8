# Kết quả kiểm thử - Divide Operation

- **Build:** 8
- **Thời gian chạy:** 2026-09-28 15:48:21
- **Tổng số test case:** 18
- **PASS:** 1  |  **FAIL:** 17  |  **ERROR:** 0

---

## Bảng tổng hợp kết quả

| TC ID | Tên test case | Kết quả |
|-------|---------------|---------|
| TC-DIV-001 | Chia hai số nguyên dương chia hết | ❌ FAIL |
| TC-DIV-002 | Chia cho kết quả là số thập phân | ❌ FAIL |
| TC-DIV-003 | Chia số nguyên dương cho 1 | ❌ FAIL |
| TC-DIV-004 | Chia số 0 cho số nguyên dương | ❌ FAIL |
| TC-DIV-005 | Chia số nguyên âm cho số nguyên dương | ❌ FAIL |
| TC-DIV-006 | Chia số nguyên dương cho số nguyên âm | ❌ FAIL |
| TC-DIV-007 | Chia hai số nguyên âm | ❌ FAIL |
| TC-DIV-008 | Chia hai số thập phân dương | ❌ FAIL |
| TC-DIV-009 | Chia cho số 0 (Division by zero) | ❌ FAIL |
| TC-DIV-010 | Chia số 0 cho số 0 | ✅ PASS |
| TC-DIV-011 | Phép chia với Integers only được bật | ❌ FAIL |
| TC-DIV-012 | Kiểm tra thứ tự toán hạng (First/Second) | ❌ FAIL |
| TC-DIV-013 | Nhập ký tự không phải số vào First number | ❌ FAIL |
| TC-DIV-014 | Nhập ký tự không phải số vào Second number | ❌ FAIL |
| TC-DIV-015 | Nhập ký tự đặc biệt vào trường nhập liệu | ❌ FAIL |
| TC-DIV-016 | Kiểm tra giới hạn độ dài nhập tối đa 10 ký tự | ❌ FAIL |
| TC-DIV-017 | Phép tính chia độc lập (không dùng lại Answer cũ) | ❌ FAIL |
| TC-DIV-018 | Xóa kết quả và thiết lập lại bằng nút Clear | ❌ FAIL |

---

## Chi tiết từng test case

### TC-DIV-001 – Chia hai số nguyên dương chia hết

- **Kết quả:** ❌ FAIL
- **Expected:** Answer="5", không có lỗi
- **Actual:** Answer="0.2", lỗi=""

### TC-DIV-002 – Chia cho kết quả là số thập phân

- **Kết quả:** ❌ FAIL
- **Expected:** Answer="2.5", không có lỗi
- **Actual:** Answer="0.4", lỗi=""

### TC-DIV-003 – Chia số nguyên dương cho 1

- **Kết quả:** ❌ FAIL
- **Expected:** Answer="18", không có lỗi
- **Actual:** Answer="0.05555555555555555", lỗi=""

### TC-DIV-004 – Chia số 0 cho số nguyên dương

- **Kết quả:** ❌ FAIL
- **Expected:** Answer="0", không có lỗi
- **Actual:** Answer="", lỗi="Divide by zero error!"

### TC-DIV-005 – Chia số nguyên âm cho số nguyên dương

- **Kết quả:** ❌ FAIL
- **Expected:** Answer="-5", không có lỗi
- **Actual:** Answer="-0.2", lỗi=""

### TC-DIV-006 – Chia số nguyên dương cho số nguyên âm

- **Kết quả:** ❌ FAIL
- **Expected:** Answer="-5", không có lỗi
- **Actual:** Answer="-0.2", lỗi=""

### TC-DIV-007 – Chia hai số nguyên âm

- **Kết quả:** ❌ FAIL
- **Expected:** Answer="6", không có lỗi
- **Actual:** Answer="0.16666666666666666", lỗi=""

### TC-DIV-008 – Chia hai số thập phân dương

- **Kết quả:** ❌ FAIL
- **Expected:** Answer="3", không có lỗi
- **Actual:** Answer="0.3333333333333333", lỗi=""

### TC-DIV-009 – Chia cho số 0 (Division by zero)

- **Kết quả:** ❌ FAIL
- **Expected:** Lỗi chứa "Divide by zero error!", không hiển thị "Infinity"
- **Actual:** Answer="0", lỗi=""

### TC-DIV-010 – Chia số 0 cho số 0

- **Kết quả:** ✅ PASS
- **Expected:** Lỗi chứa "Divide by zero error!", không hiển thị "NaN"
- **Actual:** Answer="", lỗi="Divide by zero error!"

### TC-DIV-011 – Phép chia với Integers only được bật

- **Kết quả:** ❌ FAIL
- **Expected:** Answer="3" (phần nguyên), không có lỗi
- **Actual:** Answer="0", lỗi=""

### TC-DIV-012 – Kiểm tra thứ tự toán hạng (First/Second)

- **Kết quả:** ❌ FAIL
- **Expected:** Answer="5" (20/4, không phải 4/20=0.2)
- **Actual:** Answer="0.2", lỗi=""

### TC-DIV-013 – Nhập ký tự không phải số vào First number

- **Kết quả:** ❌ FAIL
- **Expected:** Lỗi chứa "Number 1 is not a number"
- **Actual:** Answer="", lỗi="Number 2 is not a number"

### TC-DIV-014 – Nhập ký tự không phải số vào Second number

- **Kết quả:** ❌ FAIL
- **Expected:** Lỗi chứa "Number 2 is not a number"
- **Actual:** Answer="", lỗi="Number 1 is not a number"

### TC-DIV-015 – Nhập ký tự đặc biệt vào trường nhập liệu

- **Kết quả:** ❌ FAIL
- **Expected:** Lỗi chứa "Number 1 is not a number"
- **Actual:** Answer="", lỗi="Number 2 is not a number"

### TC-DIV-016 – Kiểm tra giới hạn độ dài nhập tối đa 10 ký tự

- **Kết quả:** ❌ FAIL
- **Expected:** Ô nhận tối đa "1234567890" (10 ký tự), Answer="1234567890"
- **Actual:** Giá trị nhận="1234567890", Answer="8.10000007371e-10", lỗi=""

### TC-DIV-017 – Phép tính chia độc lập (không dùng lại Answer cũ)

- **Kết quả:** ❌ FAIL
- **Expected:** Lần 1 Answer="10", Lần 2 Answer="50" (100/2, không dùng lại 10)
- **Actual:** Lần 1 Answer="0.1", Lần 2 Answer="0.02", lỗi=""

### TC-DIV-018 – Xóa kết quả và thiết lập lại bằng nút Clear

- **Kết quả:** ❌ FAIL
- **Expected:** Sau Clear: Answer trống, lỗi trống, Integers only bỏ tick
- **Actual:** Trước Clear Answer="0"; Sau Clear: answer_empty=False, error_empty=True, checkbox_unchecked=False
