# TC-ADD-003: Cộng một số dương và một số âm (kết quả bằng 0)

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
| First number | 50 |
| Second number | -50 |
| Operation | Add |
| Integers only | Unchecked |

## Test steps
1. Chọn Build: Prototype
2. Nhập giá trị '50' vào ô 'First number'
3. Nhập giá trị '-50' vào ô 'Second number'
4. Chọn phép tính 'Add' tại ô dropdown 'Operation'
5. Nhấn nút 'Calculate'

## Expected result
Trường 'Answer' hiển thị giá trị '0'.

## Status / Related bugs
Not Run / None
