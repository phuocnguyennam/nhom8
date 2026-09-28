# TC-DIV-011: Thực hiện phép chia khi bật tùy chọn Integers only

## Requirement ID
FR-DIV-03

## Module / Test type / Technique
Divide / Functional / Equivalence Partitioning

## Preconditions
- Người dùng đã truy cập trang web: https://testsheepnz.github.io/BasicCalculator.html
- Đã chọn Build tương ứng trên dropdown Build

## Test data
| First number | 7 |
| Second number | 2 |
| Operation | Divide |
| Integers only | Checked |

## Test steps
1. Chọn Build tương ứng trên dropdown "Build"
2. Nhập "7" vào ô "First number"
3. Nhập "2" vào ô "Second number"
4. Chọn "Divide" trong dropdown "Operation"
5. Tích chọn checkbox "Integers only"
6. Bấm nút "Calculate"

## Expected result
Trường "Answer" hiển thị phần nguyên của kết quả là "3" (thay vì giá trị thập phân "3.5").

## Status / Related bugs
Not Run / None
