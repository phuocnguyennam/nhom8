# TC-ADD-012: Cộng hai số có chứa khoảng trắng ở đầu hoặc cuối (Whitespace padding)

## Requirement ID
FR-ADD-01

## Module / Test type / Technique
Addition / Functional / Robustness Testing

## Preconditions
- Trình duyệt đã mở trang web Basic Calculator (https://testsheepnz.github.io/BasicCalculator)
- Đang ở phiên bản Build: Prototype (0)

## Test data
| Field | Value |
| --- | --- |
| Build | Prototype |
| First number |  30  |
| Second number |  70  |
| Operation | Add |
| Integers only | Unchecked |

## Test steps
1. Chọn Build: Prototype
2. Nhập ' 30 ' (có khoảng trắng trước và sau) vào ô 'First number'
3. Nhập ' 70 ' (có khoảng trắng trước và sau) vào ô 'Second number'
4. Chọn phép tính 'Add'
5. Nhấn nút 'Calculate'

## Expected result
JavaScript ép kiểu chuỗi có khoảng trắng thành số hợp lệ (30 + 70 = 100), trường 'Answer' hiển thị '100' mà không báo lỗi.

## Status / Related bugs
Not Run / None
