# Test Run: Module Addition - Build 2

## 1. Thông tin đợt kiểm thử
- **Đợt kiểm thử:** Test Run Addition - Build 2
- **Hệ thống kiểm thử:** [Basic Calculator](https://testsheepnz.github.io/BasicCalculator)
- **Phiên bản Build:** Build 2 (Hoán đổi hành vi giữa Add (0) và Concatenate (4))
- **Module:** `addition` (Phép cộng)
- **Số lượng Test Cases:** 20 test cases (`TC-ADD-001` đến `TC-ADD-020`)
- **Thời gian thực thi:** 2026-09-28 16:00:05
- **Công cụ thực thi:** Python Test Runner (`add.py`)

## 2. Kết quả tổng quan (Execution Summary)
- **Tổng số Test Cases thực thi:** 20
- **Passed:** 1 (5.0%)
- **Failed:** 19 (95.0%)
- **Blocked / Skipped:** 0 (0%)
- **Đánh giá tổng thể:** ❌ KHÔNG ĐẠT (Phát hiện 19 lỗi)

## 3. Bảng chi tiết kết quả thực thi (Execution Details)

| Test Case ID | Tên kịch bản kiểm thử | Req ID | Phép tính (num1 + num2) | Integers Only | Kết quả mong đợi | Kết quả thực tế | Trạng thái |
| :--- | :--- | :--- | :--- | :---: | :--- | :--- | :---: |
| `TC-ADD-001` | Cộng hai số nguyên dương hợp lệ | `FR-ADD-01` | `15 + 25` | No | `40` | `1525` | ❌ **FAILED** |
| `TC-ADD-002` | Cộng hai số nguyên âm | `FR-ADD-01` | `-10 + -20` | No | `-30` | `-10-20` | ❌ **FAILED** |
| `TC-ADD-003` | Cộng một số dương và một số âm (kết quả bằng 0) | `FR-ADD-01` | `50 + -50` | No | `0` | `50-50` | ❌ **FAILED** |
| `TC-ADD-004` | Cộng số nguyên với số 0 | `FR-ADD-01` | `1234 + 0` | No | `1234` | `12340` | ❌ **FAILED** |
| `TC-ADD-005` | Cộng hai số thập phân dương cho kết quả có phần lẻ | `FR-ADD-02` | `5.5 + 2.3` | No | `7.8` | `5.52.3` | ❌ **FAILED** |
| `TC-ADD-006` | Cộng số đạt giới hạn độ dài 10 chữ số | `FR-ADD-03` | `999999999 + 1` | No | `1000000000` | `9999999991` | ❌ **FAILED** |
| `TC-ADD-007` | Cộng số 0 với số 0 | `FR-ADD-01` | `0 + 0` | No | `0` | `00` | ❌ **FAILED** |
| `TC-ADD-008` | Cộng hai số có tiền tố dấu dương (+) | `FR-ADD-01` | `+25 + +15` | No | `40` | `+25+15` | ❌ **FAILED** |
| `TC-ADD-009` | Cộng các số có chữ số 0 ở đầu (Leading Zeros) | `FR-ADD-01` | `0007 + 0080` | No | `87` | `00070080` | ❌ **FAILED** |
| `TC-ADD-010` | Cộng hai số thập phân âm cho kết quả có phần lẻ | `FR-ADD-02` | `-3.25 + -2.5` | No | `-5.75` | `-3.25-2.5` | ❌ **FAILED** |
| `TC-ADD-011` | Cộng số thập phân dương và số thập phân âm triệt tiêu | `FR-ADD-02` | `14.5 + -14.5` | No | `0` | `14.5-14.5` | ❌ **FAILED** |
| `TC-ADD-012` | Cộng hai số có khoảng trắng ở đầu hoặc cuối | `FR-ADD-01` | ` 30  +  70 ` | No | `100` | ` 30  70 ` | ❌ **FAILED** |
| `TC-ADD-013` | Cộng hai số lớn có 9 chữ số | `FR-ADD-03` | `100000000 + 200000000` | No | `300000000` | `100000000200000000` | ❌ **FAILED** |
| `TC-ADD-014` | Cộng số lớn với số âm lớn triệt tiêu | `FR-ADD-01` | `999999999 + -999999998` | No | `1` | `999999999-999999998` | ❌ **FAILED** |
| `TC-ADD-015` | Cộng hai số thập phân dương với Integers only tắt | `FR-ADD-02` | `15.8 + 4.3` | No | `20.1` | `15.84.3` | ❌ **FAILED** |
| `TC-ADD-016` | Cộng số dạng ký hiệu khoa học (Scientific Exponential) | `FR-ADD-01` | `1e3 + 500` | No | `1500` | `1e3500` | ❌ **FAILED** |
| `TC-ADD-017` | Xác thực First number chứa ký tự chữ cái khi cộng | `FR-VAL-01` | `abc + 10` | No | `Error: Number 1 is not a number` | `abc10` | ❌ **FAILED** |
| `TC-ADD-018` | Xác thực Second number chứa ký tự chữ cái khi cộng | `FR-VAL-02` | `10 + xyz` | No | `Error: Number 2 is not a number` | `10xyz` | ❌ **FAILED** |
| `TC-ADD-019` | Kiểm tra khả năng xóa kết quả sau phép cộng bằng nút Clear | `FR-CLR-01` | `15 + 25` | No | `Clear Success (Answer cleared)` | `Clear Success (Answer cleared)` | ✅ **PASSED** |
| `TC-ADD-020` | Cộng hai số thập phân có hai chữ số sau dấu phẩy | `FR-ADD-02` | `10.25 + 5.5` | No | `15.75` | `10.255.5` | ❌ **FAILED** |

## 4. Danh sách Bug / Lỗi phát hiện (Defects Log)

| Bug ID | Test Case | Phép tính đầu vào | Kết quả mong đợi | Kết quả thực tế | Nguyên nhân lỗi | Mức độ |
| :--- | :--- | :--- | :--- | :--- | :--- | :---: |
| `BUG-ADD-B2-001` | `TC-ADD-001` | `15 + 25` | `40` | `1525` | Hoán đổi hành vi giữa Add (0) và Concatenate (4) | **High** |
| `BUG-ADD-B2-002` | `TC-ADD-002` | `-10 + -20` | `-30` | `-10-20` | Hoán đổi hành vi giữa Add (0) và Concatenate (4) | **High** |
| `BUG-ADD-B2-003` | `TC-ADD-003` | `50 + -50` | `0` | `50-50` | Hoán đổi hành vi giữa Add (0) và Concatenate (4) | **High** |
| `BUG-ADD-B2-004` | `TC-ADD-004` | `1234 + 0` | `1234` | `12340` | Hoán đổi hành vi giữa Add (0) và Concatenate (4) | **High** |
| `BUG-ADD-B2-005` | `TC-ADD-005` | `5.5 + 2.3` | `7.8` | `5.52.3` | Hoán đổi hành vi giữa Add (0) và Concatenate (4) | **High** |
| `BUG-ADD-B2-006` | `TC-ADD-006` | `999999999 + 1` | `1000000000` | `9999999991` | Hoán đổi hành vi giữa Add (0) và Concatenate (4) | **High** |
| `BUG-ADD-B2-007` | `TC-ADD-007` | `0 + 0` | `0` | `00` | Hoán đổi hành vi giữa Add (0) và Concatenate (4) | **High** |
| `BUG-ADD-B2-008` | `TC-ADD-008` | `+25 + +15` | `40` | `+25+15` | Hoán đổi hành vi giữa Add (0) và Concatenate (4) | **High** |
| `BUG-ADD-B2-009` | `TC-ADD-009` | `0007 + 0080` | `87` | `00070080` | Hoán đổi hành vi giữa Add (0) và Concatenate (4) | **High** |
| `BUG-ADD-B2-010` | `TC-ADD-010` | `-3.25 + -2.5` | `-5.75` | `-3.25-2.5` | Hoán đổi hành vi giữa Add (0) và Concatenate (4) | **High** |
| `BUG-ADD-B2-011` | `TC-ADD-011` | `14.5 + -14.5` | `0` | `14.5-14.5` | Hoán đổi hành vi giữa Add (0) và Concatenate (4) | **High** |
| `BUG-ADD-B2-012` | `TC-ADD-012` | ` 30  +  70 ` | `100` | ` 30  70 ` | Hoán đổi hành vi giữa Add (0) và Concatenate (4) | **High** |
| `BUG-ADD-B2-013` | `TC-ADD-013` | `100000000 + 200000000` | `300000000` | `100000000200000000` | Hoán đổi hành vi giữa Add (0) và Concatenate (4) | **High** |
| `BUG-ADD-B2-014` | `TC-ADD-014` | `999999999 + -999999998` | `1` | `999999999-999999998` | Hoán đổi hành vi giữa Add (0) và Concatenate (4) | **High** |
| `BUG-ADD-B2-015` | `TC-ADD-015` | `15.8 + 4.3` | `20.1` | `15.84.3` | Hoán đổi hành vi giữa Add (0) và Concatenate (4) | **High** |
| `BUG-ADD-B2-016` | `TC-ADD-016` | `1e3 + 500` | `1500` | `1e3500` | Hoán đổi hành vi giữa Add (0) và Concatenate (4) | **High** |
| `BUG-ADD-B2-017` | `TC-ADD-017` | `abc + 10` | `Error: Number 1 is not a number` | `abc10` | Hoán đổi hành vi giữa Add (0) và Concatenate (4) | **High** |
| `BUG-ADD-B2-018` | `TC-ADD-018` | `10 + xyz` | `Error: Number 2 is not a number` | `10xyz` | Hoán đổi hành vi giữa Add (0) và Concatenate (4) | **High** |
| `BUG-ADD-B2-019` | `TC-ADD-020` | `10.25 + 5.5` | `15.75` | `10.255.5` | Hoán đổi hành vi giữa Add (0) và Concatenate (4) | **High** |

## 5. Kết luận & Đề xuất (Conclusion & Recommendation)
- **Đánh giá chi tiết về hành vi của Build 2:**
  - Hoán đổi hành vi giữa Add (0) và Concatenate (4).
  - Đã phát hiện chính xác 19 lỗi trên Build 2 thông qua bộ test case kiểm thử.
  - **Đề xuất:** Gửi báo cáo bug sang đội ngũ phát triển và REJECT phiên bản build này.
