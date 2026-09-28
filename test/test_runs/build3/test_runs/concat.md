# Test Run: Module Concatenate - Build 3

## 1. Thông tin đợt kiểm thử
- **Đợt kiểm thử:** Test Run Concatenate - Build 3
- **Hệ thống kiểm thử:** [Basic Calculator](https://testsheepnz.github.io/BasicCalculator.html)
- **Phiên bản Build:** Build 3
- **Module:** `concatenate` (Phép nối chuỗi)
- **Số lượng Test Cases:** 20 test cases (`TC-CONCAT-001` đến `TC-CONCAT-020`)
- **Thời gian thực thi:** 2026-09-28 19:56:05
- **Công cụ thực thi:** Python Selenium Test Runner (`concat.py`)

## 2. Kết quả tổng quan (Execution Summary)
- **Tổng số Test Cases thực thi:** 20
- **Passed:** 15 (75.0%)
- **Failed:** 5 (25.0%)
- **Error / Skipped:** 0 (0.0%)
- **Đánh giá tổng thể:** ❌ KHÔNG ĐẠT (Phát hiện 5 lỗi)

## 3. Bảng chi tiết kết quả thực thi (Execution Details)

| Test Case ID | Tên kịch bản kiểm thử | num1 | num2 | Kết quả mong đợi | Kết quả thực tế | Trạng thái |
| :--- | :--- | :--- | :--- | :--- | :--- | :---: |
| `TC-CONCAT-001` | Concatenate two positive integers | `5` | `7` | `57` | `57` | ✅ **PASSED** |
| `TC-CONCAT-002` | Concatenate two negative integers | `-3` | `-8` | `-3-8` | `-3-8` | ✅ **PASSED** |
| `TC-CONCAT-003` | Concatenate positive and negative integers | `4` | `-9` | `4-9` | `4-9` | ✅ **PASSED** |
| `TC-CONCAT-004` | Concatenate negative and positive integers | `-6` | `2` | `-62` | `-62` | ✅ **PASSED** |
| `TC-CONCAT-005` | Concatenate two zeros | `0` | `0` | `00` | `00` | ✅ **PASSED** |
| `TC-CONCAT-006` | Concatenate positive integer and zero | `15` | `0` | `150` | `150` | ✅ **PASSED** |
| `TC-CONCAT-007` | Concatenate zero and positive integer | `0` | `42` | `042` | `042` | ✅ **PASSED** |
| `TC-CONCAT-008` | Concatenate two positive decimal numbers | `3.14` | `2.71` | `3.142.71` | `3.142.71` | ✅ **PASSED** |
| `TC-CONCAT-009` | Concatenate two negative decimal numbers | `-1.5` | `-2.5` | `-1.5-2.5` | `-1.5-2.5` | ✅ **PASSED** |
| `TC-CONCAT-010` | Concatenate integer and decimal number | `10` | `5.5` | `105.5` | `105.5` | ✅ **PASSED** |
| `TC-CONCAT-011` | Concatenate decimal number and integer | `7.25` | `100` | `7.25100` | `7.25100` | ✅ **PASSED** |
| `TC-CONCAT-012` | Concatenate very large numbers | `999999999999999` | `888888888888888` | `999999999999999888888888888888` | `99999999998888888888` | ❌ **FAILED** |
| `TC-CONCAT-013` | Concatenate alphabetic strings | `abc` | `def` | `abcdef` | `` | ❌ **FAILED** |
| `TC-CONCAT-014` | Concatenate alphanumeric string and integer | `test` | `123` | `test123` | `` | ❌ **FAILED** |
| `TC-CONCAT-015` | Concatenate integer and alphanumeric string | `456` | `xyz` | `456xyz` | `` | ❌ **FAILED** |
| `TC-CONCAT-016` | Concatenate special characters | `!@#` | `$%^` | `!@#$%^` | `` | ❌ **FAILED** |
| `TC-CONCAT-017` | Leave first number empty, provide second number | *(empty)* | `50` | `50` | `50` | ✅ **PASSED** |
| `TC-CONCAT-018` | Provide first number, leave second number empty | `100` | *(empty)* | `100` | `100` | ✅ **PASSED** |
| `TC-CONCAT-019` | Leave both numbers empty | *(empty)* | *(empty)* | `` | `` | ✅ **PASSED** |
| `TC-CONCAT-020` | Concatenate two decimal numbers (integer-only N/A) | `4.8` | `2.3` | `4.82.3` | `4.82.3` | ✅ **PASSED** |

## 4. Danh sách Bug / Lỗi phát hiện (Defects Log)

| Bug ID | Test Case | num1 | num2 | Kết quả mong đợi | Kết quả thực tế | Mức độ |
| :--- | :--- | :--- | :--- | :--- | :--- | :---: |
| `BUG-CONCAT-B3-001` | `TC-CONCAT-012` | `999999999999999` | `888888888888888` | `999999999999999888888888888888` | `99999999998888888888` | **High** |
| `BUG-CONCAT-B3-002` | `TC-CONCAT-013` | `abc` | `def` | `abcdef` | `` | **High** |
| `BUG-CONCAT-B3-003` | `TC-CONCAT-014` | `test` | `123` | `test123` | `` | **High** |
| `BUG-CONCAT-B3-004` | `TC-CONCAT-015` | `456` | `xyz` | `456xyz` | `` | **High** |
| `BUG-CONCAT-B3-005` | `TC-CONCAT-016` | `!@#` | `$%^` | `!@#$%^` | `` | **High** |

## 5. Kết luận & Đề xuất (Conclusion & Recommendation)
- Phát hiện **5** lỗi trên Build 3 cho module Concatenate.
- **Đề xuất:** Gửi báo cáo bug sang đội ngũ phát triển và REJECT phiên bản build này.
