# TC-DIV-004: Chia số 0 cho một số nguyên dương khác 0

## Requirement ID
FR-DIV-01

## Module / Test type / Technique
Divide / Functional / Boundary Value Analysis

## Preconditions
- Người dùng đã truy cập trang web: https://testsheepnz.github.io/BasicCalculator.html
- Đã chọn Build tương ứng trên dropdown Build

## Test data
| First number | 0 |
| Second number | 9 |
| Operation | Divide |
| Integers only | Unchecked |

## Test steps
1. Chọn Build tương ứng trên dropdown "Build"
2. Nhập "0" vào ô "First number"
3. Nhập "9" vào ô "Second number"
4. Chọn "Divide" trong dropdown "Operation"
5. Bấm nút "Calculate"

## Expected result
Trường "Answer" hiển thị giá trị "0". Không có thông báo lỗi hiển thị.

## Status / Related bugs
Not Run / None
