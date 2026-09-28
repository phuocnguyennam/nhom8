# TC-ADD-008: Cộng hai số có tiền tố dấu dương (+)

## Requirement ID
FR-ADD-01

## Module / Test type / Technique
Addition / Functional / Equivalence Partitioning

## Preconditions
- Trình duyệt đã mở trang web Basic Calculator (https://testsheepnz.github.io/BasicCalculator)
- Đang ở phiên bản Build: Prototype (0)

## Test data
| Field | Value |
| --- | --- |
| Build | Prototype |
| First number | +25 |
| Second number | +15 |
| Operation | Add |
| Integers only | Unchecked |

## Test steps
1. Chọn Build: Prototype
2. Nhập '+25' vào ô 'First number'
3. Nhập '+15' vào ô 'Second number'
4. Chọn phép tính 'Add'
5. Nhấn nút 'Calculate'

## Expected result
Hệ thống tự động xử lý dấu dương, thực hiện 25 + 15 và hiển thị kết quả '40' trong ô 'Answer'.

## Status / Related bugs
Not Run / None
