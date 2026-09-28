# TC-ADD-019: Kiểm tra khả năng xóa kết quả sau phép cộng bằng nút Clear

## Requirement ID
FR-CLR-01

## Module / Test type / Technique
Addition / Functional / State Reset

## Preconditions
- Trình duyệt đã mở trang web Basic Calculator (https://testsheepnz.github.io/BasicCalculator)
- Đang ở phiên bản Build: Prototype (0)

## Test data
| Field | Value |
| --- | --- |
| Build | Prototype |
| First number | 15 |
| Second number | 25 |
| Operation | Add |

## Test steps
1. Chọn Build: Prototype
2. Nhập '15' vào ô 'First number' và '25' vào ô 'Second number'
3. Chọn phép tính 'Add' và nhấn 'Calculate' để hiển thị kết quả '40'
4. Kiểm tra nút 'Clear' có trạng thái enabled và nhấp chuột vào nút 'Clear'

## Expected result
Nút 'Clear' bấm được bình thường (disabled = false). Sau khi bấm, trường 'Answer' được xóa rỗng.

## Status / Related bugs
Not Run / None
