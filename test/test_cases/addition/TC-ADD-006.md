# TC-ADD-006: Cộng số đạt giới hạn độ dài 10 chữ số

## Requirement ID
FR-ADD-03

## Module / Test type / Technique
Addition / Functional / Boundary Value Analysis

## Preconditions
- Trình duyệt đã mở trang web Basic Calculator (https://testsheepnz.github.io/BasicCalculator)
- Đang ở phiên bản Build: Prototype (0)

## Test data
| Field | Value |
| --- | --- |
| Build | Prototype |
| First number | 999999999 |
| Second number | 1 |
| Operation | Add |
| Integers only | Unchecked |

## Test steps
1. Chọn Build: Prototype
2. Nhập '999999999' vào ô 'First number'
3. Nhập '1' vào ô 'Second number'
4. Chọn phép tính 'Add'
5. Nhấn nút 'Calculate'

## Expected result
Trường 'Answer' hiển thị chính xác '1000000000'.

## Status / Related bugs
Not Run / None
