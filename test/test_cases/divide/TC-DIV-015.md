# TC-DIV-015: Nhập ký tự đặc biệt vào trường nhập liệu

## Requirement ID
FR-DIV-04

## Module / Test type / Technique
Divide / Functional / Negative Testing & Error Guessing

## Preconditions
- Người dùng đã truy cập trang web: https://testsheepnz.github.io/BasicCalculator.html
- Đã chọn Build tương ứng trên dropdown Build

## Test data
| First number | @#$ |
| Second number | 2 |
| Operation | Divide |
| Integers only | Unchecked |

## Test steps
1. Chọn Build tương ứng trên dropdown "Build"
2. Nhập "@#$" vào ô "First number"
3. Nhập "2" vào ô "Second number"
4. Chọn "Divide" trong dropdown "Operation"
5. Bấm nút "Calculate"

## Expected result
Hệ thống hiển thị thông báo lỗi màu đỏ tại errorMsgField: "Number 1 is not a number".

## Status / Related bugs
Not Run / None
