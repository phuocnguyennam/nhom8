# TC-ADD-009: Cộng các số có chữ số 0 ở đầu (Leading Zeros)

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
| First number | 0007 |
| Second number | 0080 |
| Operation | Add |
| Integers only | Unchecked |

## Test steps
1. Chọn Build: Prototype
2. Nhập '0007' vào ô 'First number'
3. Nhập '0080' vào ô 'Second number'
4. Chọn phép tính 'Add'
5. Nhấn nút 'Calculate'

## Expected result
Hệ thống loại bỏ các chữ số 0 thừa ở đầu và thực hiện phép tính 7 + 80 = 87, trường 'Answer' hiển thị '87'.

## Status / Related bugs
Not Run / None
