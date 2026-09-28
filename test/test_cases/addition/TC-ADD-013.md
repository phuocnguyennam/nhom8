# TC-ADD-013: Cộng hai số lớn có 9 chữ số

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
| First number | 100000000 |
| Second number | 200000000 |
| Operation | Add |
| Integers only | Unchecked |

## Test steps
1. Chọn Build: Prototype
2. Nhập '100000000' vào ô 'First number'
3. Nhập '200000000' vào ô 'Second number'
4. Chọn phép tính 'Add'
5. Nhấn nút 'Calculate'

## Expected result
Trường 'Answer' hiển thị kết quả chính xác '300000000'.

## Status / Related bugs
Not Run / None
