# TC-ADD-007: Cộng số 0 với số 0

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
| First number | 0 |
| Second number | 0 |
| Operation | Add |
| Integers only | Unchecked |

## Test steps
1. Chọn Build: Prototype
2. Nhập '0' vào ô 'First number'
3. Nhập '0' vào ô 'Second number'
4. Chọn phép tính 'Add'
5. Nhấn nút 'Calculate'

## Expected result
Trường 'Answer' hiển thị chính xác kết quả '0'.

## Status / Related bugs
Not Run / None
