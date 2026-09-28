# TC-ADD-020: Cộng hai số thập phân có hai chữ số sau dấu phẩy

## Requirement ID
FR-ADD-02

## Module / Test type / Technique
Addition / Functional / Boundary Value Analysis

## Preconditions
- Trình duyệt đã mở trang web Basic Calculator (https://testsheepnz.github.io/BasicCalculator)
- Đang ở phiên bản Build: Prototype (0)
- Tùy chọn Integers only đang để Unchecked

## Test data
| Field | Value |
| --- | --- |
| Build | Prototype |
| First number | 10.25 |
| Second number | 5.5 |
| Operation | Add |
| Integers only | Unchecked |

## Test steps
1. Chọn Build: Prototype
2. Nhập '10.25' vào ô 'First number'
3. Nhập '5.5' vào ô 'Second number'
4. Chọn phép tính 'Add'
5. Xác nhận checkbox 'Integers only' KHÔNG được tích chọn
6. Nhấn nút 'Calculate'

## Expected result
Trường 'Answer' hiển thị chính xác kết quả số thực '15.75' (không bị làm tròn thành 15).

## Status / Related bugs
Not Run / None
