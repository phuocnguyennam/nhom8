# TC-ADD-010: Cộng hai số thập phân âm cho kết quả có phần lẻ

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
| First number | -3.25 |
| Second number | -2.5 |
| Operation | Add |
| Integers only | Unchecked |

## Test steps
1. Chọn Build: Prototype
2. Nhập '-3.25' vào ô 'First number'
3. Nhập '-2.5' vào ô 'Second number'
4. Chọn phép tính 'Add'
5. Đảm bảo checkbox 'Integers only' KHÔNG được tích chọn
6. Nhấn nút 'Calculate'

## Expected result
Trường 'Answer' hiển thị kết quả số thập phân âm chính xác là '-5.75'.

## Status / Related bugs
Not Run / None
