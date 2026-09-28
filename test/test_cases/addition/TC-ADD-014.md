# TC-ADD-014: Cộng số lớn với số âm lớn triệt tiêu

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
| First number | 999999999 |
| Second number | -999999998 |
| Operation | Add |
| Integers only | Unchecked |

## Test steps
1. Chọn Build: Prototype
2. Nhập '999999999' vào ô 'First number'
3. Nhập '-999999998' vào ô 'Second number'
4. Chọn phép tính 'Add'
5. Nhấn nút 'Calculate'

## Expected result
Trường 'Answer' hiển thị kết quả '1'.

## Status / Related bugs
Not Run / None
