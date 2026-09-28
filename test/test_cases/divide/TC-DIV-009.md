# TC-DIV-009: Chia cho số 0 (Division by zero)

## Requirement ID
FR-DIV-02

## Module / Test type / Technique
Divide / Functional / Boundary Value Analysis & Error Guessing

## Preconditions
- Người dùng đã truy cập trang web: https://testsheepnz.github.io/BasicCalculator.html
- Đã chọn Build tương ứng trên dropdown Build

## Test data
| First number | 10 |
| Second number | 0 |
| Operation | Divide |
| Integers only | Unchecked |

## Test steps
1. Chọn Build tương ứng trên dropdown "Build"
2. Nhập "10" vào ô "First number"
3. Nhập "0" vào ô "Second number"
4. Chọn "Divide" trong dropdown "Operation"
5. Bấm nút "Calculate"

## Expected result
Hệ thống chặn phép tính và hiển thị thông báo lỗi màu đỏ tại errorMsgField: "Divide by zero error!". Không trả về kết quả "Infinity" tại ô Answer.

## Status / Related bugs
Not Run / None
