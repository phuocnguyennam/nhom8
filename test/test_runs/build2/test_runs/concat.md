# Test Run: Module Concatenate - Build 2

## 1. Thông tin đợt kiểm thử
- **Đợt kiểm thử:** Test Run Concatenate - Build 2
- **Hệ thống kiểm thử:** [Basic Calculator](https://testsheepnz.github.io/BasicCalculator.html)
- **Phiên bản Build:** Build 2
- **Module:** `concatenate` (Phép nối chuỗi)
- **Số lượng Test Cases:** 20 test cases (`TC-CONCAT-001` đến `TC-CONCAT-020`)
- **Thời gian thực thi:** 2026-09-28 19:54:48
- **Công cụ thực thi:** Python Selenium Test Runner (`concat.py`)

## 2. Kết quả tổng quan (Execution Summary)
- **Tổng số Test Cases thực thi:** 20
- **Passed:** 2 (10.0%)
- **Failed:** 18 (90.0%)
- **Error / Skipped:** 0 (0.0%)
- **Đánh giá tổng thể:** ❌ KHÔNG ĐẠT (Phát hiện 18 lỗi)

## 3. Bảng chi tiết kết quả thực thi (Execution Details)

| Test Case ID | Tên kịch bản kiểm thử | num1 | num2 | Kết quả mong đợi | Kết quả thực tế | Trạng thái |
| :--- | :--- | :--- | :--- | :--- | :--- | :---: |
| `TC-CONCAT-001` | Concatenate two positive integers | `5` | `7` | `57` | `12` | ❌ **FAILED** |
| `TC-CONCAT-002` | Concatenate two negative integers | `-3` | `-8` | `-3-8` | `-11` | ❌ **FAILED** |
| `TC-CONCAT-003` | Concatenate positive and negative integers | `4` | `-9` | `4-9` | `-5` | ❌ **FAILED** |
| `TC-CONCAT-004` | Concatenate negative and positive integers | `-6` | `2` | `-62` | `-4` | ❌ **FAILED** |
| `TC-CONCAT-005` | Concatenate two zeros | `0` | `0` | `00` | `0` | ❌ **FAILED** |
| `TC-CONCAT-006` | Concatenate positive integer and zero | `15` | `0` | `150` | `15` | ❌ **FAILED** |
| `TC-CONCAT-007` | Concatenate zero and positive integer | `0` | `42` | `042` | `42` | ❌ **FAILED** |
| `TC-CONCAT-008` | Concatenate two positive decimal numbers | `3.14` | `2.71` | `3.142.71` | `5.85` | ❌ **FAILED** |
| `TC-CONCAT-009` | Concatenate two negative decimal numbers | `-1.5` | `-2.5` | `-1.5-2.5` | `-4` | ❌ **FAILED** |
| `TC-CONCAT-010` | Concatenate integer and decimal number | `10` | `5.5` | `105.5` | `15.5` | ❌ **FAILED** |
| `TC-CONCAT-011` | Concatenate decimal number and integer | `7.25` | `100` | `7.25100` | `107.25` | ❌ **FAILED** |
| `TC-CONCAT-012` | Concatenate very large numbers | `999999999999999` | `888888888888888` | `999999999999999888888888888888` | `18888888887` | ❌ **FAILED** |
| `TC-CONCAT-013` | Concatenate alphabetic strings | `abc` | `def` | `abcdef` | `` | ❌ **FAILED** |
| `TC-CONCAT-014` | Concatenate alphanumeric string and integer | `test` | `123` | `test123` | `` | ❌ **FAILED** |
| `TC-CONCAT-015` | Concatenate integer and alphanumeric string | `456` | `xyz` | `456xyz` | `` | ❌ **FAILED** |
| `TC-CONCAT-016` | Concatenate special characters | `!@#` | `$%^` | `!@#$%^` | `` | ❌ **FAILED** |
| `TC-CONCAT-017` | Leave first number empty, provide second number | *(empty)* | `50` | `50` | `50` | ✅ **PASSED** |
| `TC-CONCAT-018` | Provide first number, leave second number empty | `100` | *(empty)* | `100` | `100` | ✅ **PASSED** |
| `TC-CONCAT-019` | Leave both numbers empty | *(empty)* | *(empty)* | `` | `0` | ❌ **FAILED** |
| `TC-CONCAT-020` | Concatenate two decimal numbers (integer-only N/A) | `4.8` | `2.3` | `4.82.3` | `7.1` | ❌ **FAILED** |

## 4. Danh sách Bug / Lỗi phát hiện (Defects Log)

| Bug ID | Test Case | num1 | num2 | Kết quả mong đợi | Kết quả thực tế | Mức độ |
| :--- | :--- | :--- | :--- | :--- | :--- | :---: |
| `BUG-CONCAT-B2-001` | `TC-CONCAT-001` | `5` | `7` | `57` | `12` | **High** |
| `BUG-CONCAT-B2-002` | `TC-CONCAT-002` | `-3` | `-8` | `-3-8` | `-11` | **High** |
| `BUG-CONCAT-B2-003` | `TC-CONCAT-003` | `4` | `-9` | `4-9` | `-5` | **High** |
| `BUG-CONCAT-B2-004` | `TC-CONCAT-004` | `-6` | `2` | `-62` | `-4` | **High** |
| `BUG-CONCAT-B2-005` | `TC-CONCAT-005` | `0` | `0` | `00` | `0` | **High** |
| `BUG-CONCAT-B2-006` | `TC-CONCAT-006` | `15` | `0` | `150` | `15` | **High** |
| `BUG-CONCAT-B2-007` | `TC-CONCAT-007` | `0` | `42` | `042` | `42` | **High** |
| `BUG-CONCAT-B2-008` | `TC-CONCAT-008` | `3.14` | `2.71` | `3.142.71` | `5.85` | **High** |
| `BUG-CONCAT-B2-009` | `TC-CONCAT-009` | `-1.5` | `-2.5` | `-1.5-2.5` | `-4` | **High** |
| `BUG-CONCAT-B2-010` | `TC-CONCAT-010` | `10` | `5.5` | `105.5` | `15.5` | **High** |
| `BUG-CONCAT-B2-011` | `TC-CONCAT-011` | `7.25` | `100` | `7.25100` | `107.25` | **High** |
| `BUG-CONCAT-B2-012` | `TC-CONCAT-012` | `999999999999999` | `888888888888888` | `999999999999999888888888888888` | `18888888887` | **High** |
| `BUG-CONCAT-B2-013` | `TC-CONCAT-013` | `abc` | `def` | `abcdef` | `` | **High** |
| `BUG-CONCAT-B2-014` | `TC-CONCAT-014` | `test` | `123` | `test123` | `` | **High** |
| `BUG-CONCAT-B2-015` | `TC-CONCAT-015` | `456` | `xyz` | `456xyz` | `` | **High** |
| `BUG-CONCAT-B2-016` | `TC-CONCAT-016` | `!@#` | `$%^` | `!@#$%^` | `` | **High** |
| `BUG-CONCAT-B2-017` | `TC-CONCAT-019` | *(empty)* | *(empty)* | `` | `0` | **High** |
| `BUG-CONCAT-B2-018` | `TC-CONCAT-020` | `4.8` | `2.3` | `4.82.3` | `7.1` | **High** |

## 5. Kết luận & Đề xuất (Conclusion & Recommendation)
- Phát hiện **18** lỗi trên Build 2 cho module Concatenate.
- **Đề xuất:** Gửi báo cáo bug sang đội ngũ phát triển và REJECT phiên bản build này.
