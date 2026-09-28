# TC-ADD-015: Cộng hai số thập phân kết hợp tùy chọn Integers only

## Requirement ID
FR-ADD-02

## Module / Test type / Technique
Addition / Functional / Decision Table

## Preconditions
- Trình duyệt đã mở trang web Basic Calculator (https://testsheepnz.github.io/BasicCalculator)
- Đang ở phiên bản Build: Prototype (0)

## Test data
| Field | Value |
| --- | --- |
| Build | Prototype |
| First number | 15.8 |
| Second number | 4.3 |
| Operation | Add |
| Integers only | Checked |

## Test steps
1. Chọn Build: Prototype
2. Nhập '15.8' vào ô 'First number'
3. Nhập '4.3' vào ô 'Second number'
4. Chọn phép tính 'Add'
5. Tích chọn checkbox 'Integers only'
6. Nhấn nút 'Calculate'

## Expected result
Tổng số thực là 20.1 được ép kiểu số nguyên thành '20' và hiển thị trong ô 'Answer'.

## Status / Related bugs
Not Run / None
