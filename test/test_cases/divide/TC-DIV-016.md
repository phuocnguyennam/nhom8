# TC-DIV-016: Kiểm tra giới hạn độ dài nhập tối đa 10 ký tự

## Requirement ID
FR-DIV-05

## Module / Test type / Technique
Divide / Functional / Boundary Value Analysis

## Preconditions
- Người dùng đã truy cập trang web: https://testsheepnz.github.io/BasicCalculator.html
- Đã chọn Build tương ứng trên dropdown Build

## Test data
| First number | 9999999999 |
| Second number | 1 |
| Operation | Divide |
| Integers only | Unchecked |

## Test steps
1. Chọn Build tương ứng trên dropdown "Build"
2. Nhập chuỗi 11 ký tự "12345678901" vào ô "First number"
3. Kiểm tra giá trị thực tế được nhận trong ô "First number"
4. Nhập "1" vào ô "Second number"
5. Chọn "Divide" trong dropdown "Operation"
6. Bấm nút "Calculate"

## Expected result
Ô "First number" chỉ cho phép tối đa 10 ký tự (chỉ nhận "1234567890"). Phép tính thực hiện thành công với kết quả "1234567890".

## Status / Related bugs
Not Run / None
