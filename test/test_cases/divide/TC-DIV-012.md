# TC-DIV-012: Kiểm tra thứ tự toán hạng của phép chia (First number chia Second number)

## Requirement ID
FR-DIV-01

## Module / Test type / Technique
Divide / Functional / Equivalence Partitioning

## Preconditions
- Người dùng đã truy cập trang web: https://testsheepnz.github.io/BasicCalculator.html
- Đã chọn Build tương ứng trên dropdown Build

## Test data
| First number | 20 |
| Second number | 4 |
| Operation | Divide |
| Integers only | Unchecked |

## Test steps
1. Chọn Build tương ứng trên dropdown "Build"
2. Nhập "20" vào ô "First number"
3. Nhập "4" vào ô "Second number"
4. Chọn "Divide" trong dropdown "Operation"
5. Bấm nút "Calculate"

## Expected result
Trường "Answer" hiển thị giá trị "5" (phép tính 20 / 4), không bị hoán đổi vị trí toán hạng (thành 4 / 20 = 0.2).

## Status / Related bugs
Not Run / None
