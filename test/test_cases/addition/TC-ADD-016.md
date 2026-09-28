# TC-ADD-016: Cộng số dạng ký hiệu khoa học (Scientific Exponential)

## Requirement ID
FR-ADD-01

## Module / Test type / Technique
Addition / Functional / Equivalence Partitioning

## Preconditions
- Trình duyệt đã mở trang web Basic Calculator (https://testsheepnz.github.io/BasicCalculator)
- Đang ở phiên bản Build: Prototype (0)

## Test data
| Field | Value |
| --- | --- |
| Build | Prototype |
| First number | 1e3 |
| Second number | 500 |
| Operation | Add |
| Integers only | Unchecked |

## Test steps
1. Chọn Build: Prototype
2. Nhập '1e3' vào ô 'First number'
3. Nhập '500' vào ô 'Second number'
4. Chọn phép tính 'Add'
5. Nhấn nút 'Calculate'

## Expected result
Hệ thống nhận diện định dạng số mũ 1000 + 500 và hiển thị kết quả '1500' trong ô 'Answer'.

## Status / Related bugs
Not Run / None
