# TC-ADD-002: Cộng hai số nguyên âm

## Requirement ID
FR-ADD-01

## Module / Test type / Technique
Addition / Functional / Boundary Value Analysis

## Preconditions
- Trình duyệt đã mở trang web Basic Calculator (https://testsheepnz.github.io/BasicCalculator)
- Đang ở phiên bản Build: Prototype (0)

## Test data
| Field | Value |
| --- | --- |
| Build | Prototype |
| First number | -10 |
| Second number | -20 |
| Operation | Add |
| Integers only | Unchecked |

## Test steps
1. Chọn Build: Prototype
2. Nhập giá trị '-10' vào ô 'First number'
3. Nhập giá trị '-20' vào ô 'Second number'
4. Chọn phép tính 'Add' tại ô dropdown 'Operation'
5. Nhấn nút 'Calculate'

## Expected result
Trường 'Answer' hiển thị chính xác kết quả '-30'. Không xuất hiện lỗi xác thực.

## Status / Related bugs
Not Run / None
