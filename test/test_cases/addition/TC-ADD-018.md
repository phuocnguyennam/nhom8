# TC-ADD-018: Xác thực Second number chứa ký tự chữ cái khi thực hiện phép cộng

## Requirement ID
FR-VAL-02

## Module / Test type / Technique
Addition / Negative Testing / Error Guessing

## Preconditions
- Trình duyệt đã mở trang web Basic Calculator (https://testsheepnz.github.io/BasicCalculator)
- Đang ở phiên bản Build: Prototype (0)

## Test data
| Field | Value |
| --- | --- |
| Build | Prototype |
| First number | 10 |
| Second number | xyz |
| Operation | Add |

## Test steps
1. Chọn Build: Prototype
2. Nhập '10' vào ô 'First number'
3. Nhập 'xyz' vào ô 'Second number'
4. Chọn phép tính 'Add'
5. Nhấn nút 'Calculate'

## Expected result
Hệ thống dừng tính toán và hiển thị thông báo lỗi: 'Number 2 is not a number'.

## Status / Related bugs
Not Run / None
